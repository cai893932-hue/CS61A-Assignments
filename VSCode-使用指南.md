# 用 VS Code 提升 CS61A 编程体验

> 仓库：`https://github.com/cai893932-hue/CS61A-Assignments`
> README 原文相关段落：
>
> > "Ensure you have Python installed on your system to run the assignments. CS61A primarily uses Python 3."
> > "Use a code editor like VS Code or PyCharm for an enhanced coding experience."
> > "python3 ok -q <function_name> --local" / "python3 ok --local"

本目录下的 `.vscode/` 已经配好，可直接复制到你的 `CS61A-Assignments` 仓库根目录使用。

---

## 0. 仓库结构（实测）

```
CS61A-Assignments/
├── HW/hw01 ... hw10/      # 作业（每题一个 .py + 一个 .ok 测试包 + ok 可执行文件）
├── Lab/lab00 ... lab12/   # 实验
├── Project/               # cats / hog / ants / scheme
│   ├── cats/  (cats.py, cats_gui.py, score.py, ucb.py, utils.py, tests/)
│   ├── hog/   (hog.py, hog_gui.py, dice.py, default_graphics.py, ucb.py)
│   ├── ants/  (ants.py, ucb.py)
│   └── scheme/(scheme.py + scheme_*.py 一堆模块 + editor/)
└── README.md
```

注意：**README 里写的是 `hw/hw01`、`lab/lab01`，但仓库实际目录是大写的 `HW/`、`Lab/`**。Windows 上大小写不敏感，Linux/macOS 上要留意。

每个作业目录里有：
- `hw01.py` —— 你的作答文件
- `hw01.ok` —— 测试用例数据（PK 头，本质是 zip）
- `ok` —— 可执行的自测脚本（`python ok --local`）
- `tests/` —— 测试辅助模块

`ok` 是 zipapp，在 Windows 上**不能**直接 `./ok`，要用 `python ok ...`；README 里的 `python3 ok` 在 Windows 上也常常失效（只有 `python`）。实测本机 `python3` 存在，但为稳妥起见统一用 `python`。

---

## 1. 必装扩展

| 扩展 | ID | 作用 |
|---|---|---|
| Python | `ms-python.python` | 语言支持、调试、虚拟环境 |
| Pylance | `ms-python.vscode-python-pylance` | 类型提示、跳转、悬停补全（CS61A 大量使用高阶函数，提示很关键） |
| Python Debugger | `ms-python.debugpy` | F5 断点调试 |
| Ruff | `charliermarsh.ruff` | 极速 lint + format，比 flake8/black 快一个数量级 |
| GitLens | `eamodio.gitlens` | 行级历史，看自己作业的 diff |
| Error Lens | `usernamehw.errorlens` | 把报错直接显示在行尾 |
| Python Formatter | `ms-python.python-formatter` | 保存时格式化 |
| isort | `ms-python.isort` | import 排序 |

`.vscode/extensions.json` 已写好推荐列表，打开项目时 VS Code 会提示"安装工作区推荐的扩展"，一键装齐。

---

## 2. 已配好的 `.vscode/` 内容

### settings.json
- 关闭 Pylance 严格模式（`basic`），CS61A 里大量动态/鸭子类型写法，strict 会狂报误报。
- `extraPaths` 加入 `HW` / `Lab` / `Project`，解决 `from ucb import *`、`from scheme_forms import *` 这类**同级导入找不到**的问题——这是新手最常见的"红色波浪线其实能跑"问题。
- 80 字符行标尺 + 保存时格式化，对齐 CS61A 官方风格。
- 排除 `__pycache__` / `.pytest_cache` / `*.pyc`。

### tasks.json（Ctrl+Shift+B 或 Terminal → Run Task）
| 任务 | 作用 |
|---|---|
| `ok: test current file` | 在**当前文件所在目录**跑 `python ok --local`，跑完整份作业 |
| `ok: test with -v (verbose)` | 同上但打印每题细节 |
| `ok: test single question (edit name below)` | 把 `FUNCTION_NAME` 改成函数名，跑单题 |
| `python: run current file` | 直接运行当前 .py |

关键点：任务用 `${relativeFileDirname}` 作为 cwd，所以**只要光标在 `HW/hw03/hw03.py` 里按 Ctrl+Shift+P → Run Task，就能自动定位到 `HW/hw03/ok`**，不用手动 cd。

### launch.json（F5 调试）
| 配置 | 用途 |
|---|---|
| `Python: 当前文件` | 调试你正在写的 .py |
| `Python: 项目入口 (如 cats.py / hog.py)` | 调试项目主程序，带 `--local` |
| `Python: 调试测试 (ok --local)` | 在测试运行时下断点，定位是哪一步炸的 |
| `Python: 附加到进程` | attach 到 5678 端口（配合 `debugpy.listen()`） |

---

## 3. 实战工作流

### 日常刷题循环
1. `Ctrl+Shift+P` → `Tasks: Run Test Task` 或直接按 `Ctrl+Shift+B` → 选 `ok: test current file`。
2. 看 Dedicated 面板输出，逐题 PASS/FAIL。
3. 失败时按 F5 选 `Python: 调试测试 (ok --local)`，在 `ok` 内部下断点。
4. `Ctrl+Shift+G` 看 GitLens diff，确认只改了该改的文件。

### 单题调试
```bash
python ok -q a_plus_abs_b --local     # 跑一题
python ok -q a_plus_abs_b -v --local  # 带细节
python ok --local                     # 跑整份
```

### Scheme 项目（Project/scheme）
CS61A 的 Scheme 项目有自定义 `.scm` tokenizer/parser/evaluator 体系。用 VS Code 时：
- 装 `matthewp.rio` 之外的 Scheme 语法高亮扩展（如 `marcushietmann.scheme-syntax` 或 `sk-/scheme-syntax`）高亮 `.scm`。
- `scheme.py` 之外还有 `scheme_tokens.py` / `scheme_parser` / `scheme_eval_apply.py` 等一堆模块，**务必靠 `extraPaths` 里的 `Project/scheme` 目录做导入解析**。
- 官方项目自带 `Project/scheme/editor/` 目录——那是官方推荐的 Scheme 编辑器（浏览器端），配 VS Code 用它来写 `.scm` 效果更好：写完存盘，终端里 `python scheme.py` 加载测试。

### Cats / Ants 这类有 GUI 的项目
```bash
cd Project/cats
python cats.py          # 官方原版（会报错，因为你要改）
python cats_gui.py      # 本地评分 GUI
python hog_gui.py
```
- GUI 项目调试建议在 `cats_gui.py` 里下断点。
- 动画/图片资源在 `Project/cats/images/`、`favicons/`。
- `ants` 项目要调 `ants.py` 里的 `make_ants()`（通常被注释掉了），把它取消注释才能看到蚂蚁。

---

## 4. 提效技巧

1. **别用 `print` 调试，用 Debugger**。CS61A 的测试是 pytest/doctest 混合，`print` 只会污染输出。F5 + 变量面板（Debug 侧栏 Variables / Watch）能直接看递归栈里的闭包、`self`、环境帧。
2. **Pylance 悬停看类型**。CS61A 考的是高阶函数，`# type: (int) -> int` 这类类型标注在 61A 里虽不是强制，但配合 Pylance 能提前发现 `(lambda x: x)(1, 2)` 这类参数个数错误。
3. **Ruff 代替手工检查**。CS61A 评分不查风格，但 Ruff 能抓到你作业里的真实 bug：未使用的变量（多半是拼错的函数名）、可变默认参数、裸 `except`。
4. **WIP commits**。每做完一题就 `git commit -m "hw03: a_plus_abs_b done"`，期末回头看 commit 历史就是一份学习轨迹（也能防误删代码）。
5. **Rover/文件搜索替代翻目录**。`Ctrl+P` 输入 `ucb.py` 秒跳；`Ctrl+Shift+F` 全局搜 `a_plus_abs_b` 看它被谁调用。
6. **Jupyter 单独开一个 scratch 文件**探索思路：新建 `scratch.ipynb`，用 `# %%` 单元格快速验证思路，确认无误再抄进正式作业文件。
7. **终端用 VS Code 内置的**（`Ctrl+` `），这样 `python` 解释器与编辑器一致，不会出现"终端能跑、编辑器报红"。

---

## 5. 常见坑

| 现象 | 原因 | 解法 |
|---|---|---|
| `from ucb import *` 报红 | 同级目录不在 sys.path | settings.json 的 `extraPaths` 已配 `HW/Lab/Project` |
| `./ok: Permission denied` | Windows 无执行位 | 用 `python ok` |
| `python3` 命令不存在 | Windows 只有 `python` | 用 `python` |
| Pylance 满屏红波浪线 | strict 模式 + 高阶函数 | 保持 `typeCheckingMode: basic` |
| 终端 `python` 与编辑器解释器不一致 | 多版本 Python | `Ctrl+Shift+P` → Python: Select Interpreter，选同一个 |
| `ok` 报 "Test not found" | 题目名写错或大小写不符 | 错误信息会列出所有可用题目名，照抄 |

---

## 6. 一键安装步骤

```bash
# 1. Fork 后克隆
git clone https://github.com/<你的用户名>/CS61A-Assignments.git
cd CS61A-Assignments

# 2. 复制配置
#    把本目录 .vscode/ 整个复制到仓库根目录

# 3. 创建虚拟环境（可选但推荐）
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 4. 打开
code .

# 5. VS Code 右下角选择 .venv 里的解释器，Ctrl+Shift+P 装齐推荐扩展

# 6. 开始
cd HW/hw01 && python ok --local
```
