"""
CS61A 一键测试脚本（不需要任何快捷键，双击或命令行运行都行）

用法（在项目根目录 CS61A-Assignments 下）：
    python test.py              # 自动检测你正在编辑的文件，跑对应作业的全部测试
    python test.py hw01         # 跑指定作业
    python test.py hw01 hailstone   # 只跑某一题
    python test.py --list       # 列出所有作业/实验/项目
    python test.py --all        # 跑所有作业

设计目标：完全不需要 Ctrl+Shift 系列的快捷键。
"""

import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

# 作业目录的命名规则，例如 HW/hw01、Lab/lab07、Project/cats
NAME_RE = re.compile(r"^(hw|lab)\d+$|^[a-z]+$")


def find_all_tasks():
    """扫描出所有含 ok 可执行文件的目录。"""
    tasks = []
    for top in ("HW", "Lab", "Project"):
        base = os.path.join(ROOT, top)
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            d = os.path.join(base, name)
            ok = os.path.join(d, "ok")
            if os.path.isfile(ok) or os.path.isdir(ok):
                tasks.append((f"{top}/{name}", d))
    return tasks


def detect_current_file():
    """
    猜测你正在编辑哪个作业：
    1) 读 VS Code 记录的最后打开文件
    2) 读最近修改过的 .py 文件
    """
    # 方法 1：VS Code 的最近打开记录
    try:
        vscdb = os.path.expanduser(
            r"~\AppData\Roaming\Code\User\globalStorage\state.vscdb"
        )
        import sqlite3

        conn = sqlite3.connect(vscdb)
        rows = conn.execute(
            "select value from ItemTable where key like '%history%' or key like '%recent%'"
        ).fetchall()
        conn.close()
        for (raw,) in rows:
            for m in re.finditer(
                r"[A-Za-z]:[\\/][^\"'\s]*?CS61A-Assignments[\\/][^\"'\s]*", raw
            ):
                p = m.group(0)
                task = match_task_of_file(p)
                if task:
                    return task
    except Exception:
        pass

    # 方法 2：最近修改的 .py
    best = None
    best_time = 0
    for top in ("HW", "Lab", "Project"):
        base = os.path.join(ROOT, top)
        if not os.path.isdir(base):
            continue
        for dirpath, _dirnames, filenames in os.walk(base):
            if "ok" not in os.listdir(dirpath) and not os.path.exists(
                os.path.join(dirpath, "ok")
            ):
                continue
            for fn in filenames:
                if fn.endswith(".py"):
                    fp = os.path.join(dirpath, fn)
                    try:
                        t = os.path.getmtime(fp)
                    except OSError:
                        continue
                    if t > best_time:
                        best_time = t
                        best = dirpath
    if best:
        return os.path.relpath(best, ROOT).replace("\\", "/")
    return None


def match_task_of_file(path):
    """给出一个文件路径，返回它所属的作业目录（如 HW/hw01）。"""
    p = path.replace("\\", "/")
    for task, d in find_all_tasks():
        d = d.replace("\\", "/")
        if p.startswith(d + "/"):
            return task
    return None


def run_ok(task_dir, questions=None, verbose=False):
    """在指定作业目录里跑 ok。"""
    exe = os.path.join(ROOT, ".venv", "Scripts", "python.exe")
    if not os.path.exists(exe):
        exe = sys.executable

    args = [exe, "ok"]
    if verbose:
        args.append("-v")
    for q in questions or []:
        args += ["-q", q]
    args.append("--local")

    print("=" * 60)
    print(f"  正在运行: {os.path.relpath(task_dir, ROOT)}")
    print(f"  命令: python ok {' '.join(questions or [])} --local")
    print("=" * 60)
    try:
        return subprocess.call(args, cwd=task_dir)
    except KeyboardInterrupt:
        print("\n已中断。")
        return 1


def main():
    args = sys.argv[1:]

    if not args:
        # 无参数：自动检测
        task = detect_current_file()
        if not task:
            print("没能自动检测出你在做哪份作业。")
            print("请这样用：python test.py hw01")
            print("或者用 python test.py --list 看看所有可选项。")
            return 1
        print(f"自动检测到你在做: {task}\n")
        return run_ok(os.path.join(ROOT, task.replace("/", os.sep)))

    if args[0] in ("--list", "-l"):
        print("\n所有可测试的作业：\n")
        for t, _d in find_all_tasks():
            print(f"  {t}")
        print("\n用法: python test.py <名字> [题目名]")
        return 0

    if args[0] in ("--all", "-a"):
        rc = 0
        for t, d in find_all_tasks():
            print()
            rc |= run_ok(d)
        return rc

    # python test.py hw01 [q1 q2 ...]
    name = args[0]
    qs = args[1:]
    tasks = {t.replace("\\", "/"): d for t, d in find_all_tasks()}

    # 允许只写 hw01 或 01 这样的简写
    for t in tasks:
        if t.split("/")[-1] == name or t == name:
            return run_ok(tasks[t], qs)

    print(f"没找到作业 '{name}'。")
    print("用 python test.py --list 看看所有可选项。")
    return 1


if __name__ == "__main__":
    sys.exit(main())
