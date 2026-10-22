# CS61A 零基础上手指南（Windows + VS Code）

> 面向"连终端都不会用"的你。照着做，一步一步来，每步都有"你会看到什么"。

---

## ✅ 好消息：你已经不用克隆了

我检查过了，你的电脑上**已经有这个仓库了**：

```
C:\Users\86199\CS61A-Assignments
```

而且我已经替你把这些都做好了：

| 我做好的事 | 状态 |
|---|---|
| 仓库已在本地 | ✅ 完成 |
| 虚拟环境 `.venv`（Python 3.14.7，自带 tkinter） | ✅ 完成 |
| VSCode 配置 `.vscode/`（4 个文件） | ✅ 完成 |
| 必要扩展（Python/Pylance/Ruff/GitLens/ErrorLens/isort）已装 | ✅ 完成 |
| `git` 已在 PATH（2.55.0） | ✅ 已有 |
| 61A-bot 交互弹窗已关掉（HW/Lab/Project **全部 27 个目录**都关好了） | ✅ 完成 |
| `.gitignore` 加上 `.venv/`、`__pycache__/`、`.ok_disabled` | ✅ 完成 |
| 环境配置已 `git commit`（存档了，可回滚） | ✅ 完成 |

**所以你现在只需要做一件事：打开它。** 下面从"打开"开始教。

---

## 第 1 步：打开项目（3 种方式，任选）

### 方式 A：双击（最简单）

1. 打开**文件资源管理器**（Windows 那个文件夹图标，在任务栏上）。
2. 地址栏点一下，直接粘贴这个路径再回车：
   ```
   C:\Users\86199\CS61A-Assignments
   ```
3. 在这个文件夹里**空白处右键 → 在终端中打开** 或 **在文件夹位置打开 VS Code**。
   - 看到 "在终端中打开" 就选它，VSCode 会自己弹出来并已经打开这个项目。

### 方式 B：从 VSCode 里打开（推荐，能看懂自己在哪）

1. 桌面双击 **Visual Studio Code**（有快捷方式）。
2. 启动后是**欢迎页**，中间有一排大按钮。点最左边那个 **「打开文件夹 / Open Folder」**。
   - ⚠️ 一定选"打开文件夹"，不要选"打开文件"。选文件夹才能用我们配好的 `.vscode/`。
3. 弹出的文件选择框里，地址栏粘贴：
   ```
   C:\Users\86199\CS61A-Assignments
   ```
4. 按回车 / 点"选择文件夹"。

### 方式 C：命令行（最快，习惯后最顺手）

在任意终端里敲：
```powershell
cd C:\Users\86199\CS61A-Assignments
code .
```
（`code .` 末尾的点和空格不能少，意思是"打开当前文件夹"。）

**怎么开终端：**
- 桌面右键 → 终端 / Windows Terminal / PowerShell
- 或按 `Win + R`，输入 `powershell`，回车
- 或在 VSCode 里按 `Ctrl + `` ` （Esc 下面那个反引号键）

**你会看到：** VSCode 窗口，左边是文件树（能看到 `HW`、`Lab`、`Project`、`README.md`），中间是编辑区，底部有一条黑色横条（终端）。

---

## 第 2 步：认一下 VSCode 的界面

```
┌──────────────────────────────────────────────────────────┐
│ ① 标题栏：CS61A-Assignments                    [搜索框🔍]  │  ← 搜文件/命令
├──────────┬───────────────────────────────────────────────┤
│          │                                               │
│ ② 活动栏 │  ③ 编辑区：你正在写的代码                      │
│  文件    │                                               │
│  搜索    │                                               │
│  源代码  │                                               │
│  运行    │                                               │
│  扩展    │                                               │
│          │                                               │
├──────────┴───────────────────────────────────────────────┤
│ ④ 面板：终端 / 问题 / 输出 / 调试控制台                    │  ← Ctrl+` 切换
└──────────────────────────────────────────────────────────┘
```

**必记的 6 个快捷键：**

| 按键 | 作用 | 什么时候用 |
|---|---|---|
| `Ctrl + `` ` | 打开/收起下面的终端 | 要敲 `python ok` 的时候 |
| `Ctrl + Shift + P` | **命令面板**（万能搜索框） | 不记得快捷键时，输关键词就有 |
| `Ctrl + P` | 快速跳文件 | 输入 `hw01` 直接到文件 |
| `Ctrl + Shift + B` | 运行构建任务（= 跑测试） | 做完题测一下 |
| `F5` | 调试（断点） | 想知道哪行错了 |
| `Ctrl + S` | 保存 | 巨重要 |

> 记不住很正常。**`Ctrl + Shift + P` 是万能钥匙**：任何操作不知道怎么做，就打开它，输关键词（比如 "interpreter"、"terminal"、"run task"），选列表里的那一项。

---

## 第 3 步：确认 Python 解释器（你说的"不会切换 Python"）

### 什么是"解释器"

Python 本身只是一门语言，真正干活的是**解释器**（一个叫 `python.exe` 的程序）。你电脑上装了**好几个** Python，所以 VSCode 需要你告诉它"用哪一个"。这就是"切换解释器"。

你现在要选的是这个（我已经在 `.venv` 里装好了）：

```
C:\Users\86199\CS61A-Assignments\.venv\Scripts\python.exe
```

### 怎么切（图形界面，不用敲命令）

1. 看 VSCode **窗口最底部的状态栏**（最下面那条窄窄的横条），靠左或靠右有个写着 **`Python 3.14.7`** 或者类似文字的小方块。
2. **用鼠标点它**（不用按快捷键）。
3. 会弹出一个列表框，标题是 **"Select Python Interpreter" / "选择 Python 解释器"**。列表里每一条是一行路径。
4. 找到带 **`.venv`** 的那条，路径应该长这样：
   ```
   C:\Users\86199\CS61A-Assignments\.venv\Scripts\python.exe
   ```
5. **点它**。选完底部状态栏显示的版本会变。
6. 之后 VSCode 的终端里 `python` 就自动指向它了，不用你再操心。

> 底部没显示 Python 字样？说明扩展还没加载完，等两秒；还是没有，就按 `Ctrl+Shift+P` → 输入 `interpreter` → 选 **Python: Select Interpreter**。

### 顺带一提：你的电脑上有哪些 Python

我查过了（供你辨认，别被列表里一堆选项吓到）：

| 路径 | 版本 | 能不能用 |
|---|---|---|
| `C:\Users\86199\CS61A-Assignments\.venv\Scripts\python.exe` | 3.14.7 | ✅ **选这个**（我新建的，干净、有 tkinter） |
| `C:\Users\86199\AppData\Local\Python\bin\python.exe` | 3.14.7 | ✅ 也能用（建 .venv 用的就是它） |
| `C:\Users\86199\AppData\Local\Microsoft\WindowsApps\python.exe` | 3.13.14 | ⚠️ 是微软商店的"跳转别名"，偶尔会有怪问题，不建议选 |
| `C:\Users\86199\.workbuddy\binaries\python\...` | 3.13.12 | ❌ 这是 WorkBuddy 自己的，**没有 tkinter**，不能用来跑 cats/hog 的 GUI |

`.venv` 这个名字是"virtual environment"（虚拟环境）的缩写——一个独立的、干净的 Python 小房间，跟别的项目互不干扰。这是 Python 世界的标准做法。

---

## 第 4 步：打开你的第一份作业

1. 左边**活动栏**点最上面那个 📁 **文件图标**（"资源管理器"）。
2. 文件树里展开 **`HW`** → 展开 **`hw01`**。
3. 点 **`hw01.py`**。中间会打开代码。

你会看到这样的内容：

```python
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.
    ...
    """
    if b < 0:
        f = _____          # ← 这里是要你填的空
    else:
        f = _____
    return f(a, b)
```

**`_____`（5 个下划线）就是留给你填的空。** 它本身是合法的 Python 变量名（合法但没定义），所以在你写对之前，报错是 `NameError: name '_____' is not defined` —— **这说明你的编辑器认出它是代码了，只是你还没填**。这很正常！

---

## 第 5 步：跑测试（两种方式）

### 方式 A：图形化，一键（推荐先用这个）

1. 先按 `Ctrl + S` **保存**（不保存测的是旧代码！）。
2. 按 **`Ctrl + Shift + B`**。
3. VSCode 会弹出一个任务列表，选 **`ok: test current file`**。
4. 底部弹出一个黑色面板（叫"专用终端"），显示测试结果。

**你会看到类似：**
```
=====================================================================
Assignment: Homework 1
OK, version v1.18.1
=====================================================================

a_plus_abs_b ....................................... PASS
hailstone ......................................... FAIL
Test summary
    1 test cases passed before encountering first failed test case
```

`PASS` = 过了，`FAIL` = 没过。**第一个 FAIL 出现时 ok 会自动停**（这是它故意的，一次只让你专注一个错）。

### 方式 B：手动敲命令（更灵活，值得学）

1. 按 `Ctrl + `` ` 打开底部终端。
2. 敲：
   ```powershell
   cd HW\hw01
   ```
3. 敲：
   ```powershell
   python ok --local
   ```
4. 只想测一题（比如测 `hailstone`）：
   ```powershell
   python ok -q hailstone --local
   ```
5. 想知道有哪些题可以测：
   ```powershell
   python ok --tests
   ```
   （我实测过，会列出：`a_plus_abs_b`、`a_plus_abs_b_syntax_check`、`hailstone`、`largest_factor`、`two_of_three`、`two_of_three_syntax_check`）

> **Windows 终端里用反斜杠 `\`**（`HW\hw01`），不是斜杠 `/`。敲错会报"找不到路径"。

**关于 61A-bot 弹窗：** 第一次在某个作业目录跑测试时，ok 可能会问你要不要 AI 调试帮助：

```
[61A-bot]: Would you like to receive debugging help (d) or ...?
```

**输入 `never` 然后回车**，这个作业就再也不会烦你了。我已经帮你在所有 HW / Lab / Project 目录都预先关掉了，你现在直接跑测试不会有弹窗。

**关于 `python` vs `python3`：** README 里写的是 `python3 ok`，但 **Windows 上请一律用 `python ok`**。我实测过 `python3` 在你机器上虽然存在，但不稳。

**关于 `--local`：** 这个参数让 ok 不联网、不上传你的代码，纯本地跑。**每次都加上**，是官方推荐的自测方式。

---

## 第 6 步：让报错变得能看懂

第一次跑必然满屏红字。别慌，ok 的输出格式是固定的：

```
# Error: expected
#     5
# but got
#     Traceback (most recent call last):
#       ...
#     NameError: name '_____' is not defined
```

读法：
- **`expected 5`** —— 正确答案是 5
- **`but got ...`** —— 你实际得到的东西
- **`NameError: name '_____' is not defined`** —— **真正的错因在这里**：你还在用 `_____` 这个占位符。填上真代码就好。

**最常见的三个错：**

| 报错关键字 | 意思 | 怎么办 |
|---|---|---|
| `NameError: name '_____' is not defined` | 还有空没填 | 把 `_____` 换成真代码 |
| `IndentationError` | 缩进不对 | Python 严格要求**每层缩进 4 个空格**，别用 Tab |
| `SyntaxError` | 语法错 | 看报错那行的 `^` 指针指的位置 |

**缩进的坑：** 千万不要按 Tab 键缩进。在 VSCode 里按 **空格键**（可以按 4 次），或者直接按 `Enter` 后 VSCode 会自动帮你缩进。

---

## 第 7 步：用断点调试（知道哪一行错了）

当报错看不出问题在哪时：

1. 在代码行号左边点一下 → 出现**红点**（这就是断点）。
2. 按 **`F5`**。
3. VSCode 会先问你选哪个配置，选 **`Python: 当前文件`**。
4. 代码会停在你设断点的那一行。**黄色高亮** = 当前执行到这。
5. 屏幕下半部分出现 **调试控制台** 和 **变量区**：
   - **变量 / Variables**：能看到当前函数里每个变量的值（萌新最需要的就是这个）
   - **监视 / Watch**：可以自己敲一个表达式，实时看它的值（比如敲 `n` 看循环变量）
6. 逐行执行：按 **F10**（单步跳过）/ **F11**（单步进入）。
7. 结束：按 `Shift + F5`，或点调试控制台方块的 ■。

**变量区是 CS61A 的救命工具。** 递归、闭包、生成器这些概念，看变量值比盯着代码猜快十倍。

---

## 第 8 步：写代码时的顺手操作

| 想做什么 | 怎么做 |
|---|---|
| 自动补全 | 输入几个字母后按 **`Tab`**，或者 **`Ctrl + Space`** 呼出提示列表 |
| 快速跳到定义 | 鼠标悬停在函数名上 → 点弹出的 **`Go to Definition`**；或 `F12` |
| 查函数用法 | 悬停在名字上 → 弹窗里就是文档；`Ctrl + K` `Ctrl + I` 看完整文档 |
| 快速重命名 | `F2` → 改名字 → 回车，**所有引用处一起改** |
| 格式化代码 | `Shift + Alt + F`（已配置 Ruff，保存时也会自动格式化） |
| 跳到某个文件 | `Ctrl + P` → 输入 `hw03` |
| 全局搜某个词 | `Ctrl + Shift + F` → 输入关键词 |
| 看自己改了啥 | `Ctrl + Shift + G`（GitLens），或左侧源代码管理图标 |
| 保存全部 | `Ctrl + K` `S` |

---

## 第 9 步：每天的固定流程（照抄就行）

```
早上：
  1. 打开 VSCode（如果关了）
  2. 打开文件夹 C:\Users\86199\CS61A-Assignments
  3. 确认底部状态栏的 Python 版本

做题：
  4. 左边点 HW\hw01\hw01.py（或你要做的那个）
  5. 改代码
  6. Ctrl + S 保存
  7. Ctrl + Shift + B → 选 "ok: test current file"
  8. 看结果。PASS 就下一题；FAIL 就看 but got 的报错
  9. 实在看不懂 → F5 加断点看变量

提交/存档（每做完一题）：
  10. 左侧源代码管理图标 → 消息框里写 "hw01: 完成 a_plus_abs_b" → 点 ✓ 提交
```

第 10 步很重要：CS61A 期末复习全靠这一串提交记录，帮你留住学习轨迹，也防手滑删代码。

---

## 第 10 步：项目作业（cats / hog / ants / scheme）额外说明

这些是图形界面/大型项目，跑法不一样。

### cats（猜数字游戏）
```powershell
cd Project\cats
python cats_gui.py
```
弹出的窗口里填 1-100 的数字，程序会给出反馈（高了/低了）。
调试：在 `cats.py` 里加断点，按 F5。

### hog（掷骰子游戏）
```powershell
cd Project\hog
python hog_gui.py
```
⚠️ 这个 GUI 需要 `tkinter`。你已经选了 `.venv` 里的解释器，我验证过**它带 tkinter**，能正常弹出窗口。（如果你选了微软商店那个 3.13.14 也许行，但 `.venv` 的 3.14.7 是我专门验过的。）

### ants
```powershell
cd Project\ants
```
`ants.py` 里有个 `make_ants()` 函数**默认被注释掉了**，要把它取消注释才能看到蚂蚁跑。经典作业（ants battle）。

### scheme（SICP 解释器）
这个最特殊：
- 主要写 `.scm` 文件（Scheme 代码），不是 `.py`。
- 仓库自带官方编辑器：`Project\scheme\editor\` —— 用浏览器打开里面的 index.html 就能写 Scheme。
- `.py` 那部分是解释器本身（`scheme.py` + `scheme_*.py` 一堆模块）。
- 测试：`python ok --local`
- **强烈建议**：把 `Project\scheme` 也加进解释器搜索路径（我已经加了）。

---

## 一句话速查表（打印贴显示器上）

```
切解释器    : Ctrl+Shift+P → "interpreter" → 选带 .venv 的那条
开终端      : Ctrl + `
跑测试      : Ctrl+Shift+B → ok: test current file
手动测试    : cd HW\hw01  然后  python ok --local
测单题      : python ok -q 函数名 --local
看有哪些题  : python ok --tests
调试        : 行号左边点红点 → F5
保存        : Ctrl + S
万能搜索    : Ctrl+Shift+P
跳文件      : Ctrl + P
```

---

## 最后确认：现在就开始

1. 打开 VSCode → 打开文件夹 `C:\Users\86199\CS61A-Assignments`
2. 底部确认 Python 是 `.venv` 那条
3. 左边点 `HW` → `hw01` → `hw01.py`
4. 把第一个 `_____` 换成 `add` 或 `sub`（题目要求：b<0 时用 sub）
5. `Ctrl+S` → `Ctrl+Shift+B` → 选 `ok: test current file`

第 4 步提示：`a_plus_abs_b(a, b)` 要求 b 为负时用 `sub`、否则用 `add`，文件顶部已经 `from operator import add, sub` 导入好了，所以填 `f = sub` / `f = add` 就行。

> 我实测过这个答案：填好后跑 `python ok -q a_plus_abs_b --local`，输出是 **"1 test cases passed! No cases failed."** ✅
> （注意 `if b < 0:` 那一支要用 `sub`——因为 b 是负数，减去它等于加上它的绝对值。填反了会得到 `expected 5 but got -1`。）

**做完这一步你就完全入门了。** 剩下的 9 份作业、12 个 lab、4 个项目，都是同一套流程。
