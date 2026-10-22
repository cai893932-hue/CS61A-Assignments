// CS61A 测试按钮扩展
// 在 VS Code 底部状态栏放一个「🧪 测试」按钮 + 一个「单题」按钮。
// 纯鼠标点击，不需要任何快捷键。

const vscode = require("vscode");
const path = require("path");
const fs = require("fs");
const { execFile } = require("child_process");

/** 找到某个文件所在作业目录里的 ok 可执行文件 */
function findOkFor(filePath) {
  let dir = path.dirname(filePath);
  while (dir && dir !== path.dirname(dir)) {
    const okPath = path.join(dir, "ok");
    if (fs.existsSync(okPath)) return { dir, okPath };
    dir = path.dirname(dir);
  }
  return null;
}

/** 找到仓库根（含 .vscode 的那一层） */
function findWorkspaceRoot() {
  const folders = vscode.workspace.workspaceFolders;
  if (!folders || folders.length === 0) return null;
  return folders[0].uri.fsPath;
}

/** 找到可用的 python 解释器 */
function getPython() {
  const root = findWorkspaceRoot();
  if (root) {
    const venv = path.join(root, ".venv", "Scripts", "python.exe");
    if (fs.existsSync(venv)) return venv;
  }
  return "python";
}

function runInTerminal(name, cwd, cmd, args) {
  const terminal = vscode.window.createTerminal({ name, cwd });
  terminal.show(true);
  terminal.sendText(`${cmd} ${args.join(" ")}`);
  return terminal;
}

/** 跑测试，输出到「测试结果」输出通道，同时在终端里也能看到 */
async function runTest(target, extraArgs) {
  if (!target) {
    vscode.window.showWarningMessage(
      "CS61A: 没找到 ok 测试文件。确认你打开的是 HW/Lab/Project 里的 .py 文件。"
    );
    return;
  }

  const root = findWorkspaceRoot();
  const py = getPython();
  const args = [target.okPath, ...extraArgs, "--local"];

  // 在专用终端里跑，方便看完整输出
  const terminal = vscode.window.createTerminal({
    name: "CS61A 测试",
    cwd: target.dir,
  });
  terminal.show(true);

  const quoted = args
    .map((a) => (a.includes(" ") ? `"${a}"` : a))
    .join(" ");
  terminal.sendText(`"${py}" ${quoted}`);

  // 同时写一份到输出面板
  const out = vscode.window.createOutputChannel("CS61A 测试");
  out.show(true);
  out.appendLine(`$ ${py} ${quoted}`);
  out.appendLine(`  (工作目录: ${target.dir})`);

  execFile(
    py,
    args,
    { cwd: target.dir, timeout: 300000 },
    (error, stdout, stderr) => {
      out.appendLine("");
      out.appendLine(stdout || "");
      if (stderr) out.appendLine(stderr);
      if (error) {
        out.appendLine(`[退出码 ${error.code ?? "?"}]`);
      }
    }
  );
}

function activate(context) {
  const testBtn = vscode.window.createStatusBarItem(
    vscode.StatusBarAlignment.Right,
    100
  );
  testBtn.text = "$(beaker) 测试";
  testBtn.tooltip = "点击运行当前作业的 ok 测试（快捷键已被占用时的替代方案）";
  testBtn.command = "cs61a.testHere";
  testBtn.show();

  const qBtn = vscode.window.createStatusBarItem(
    vscode.StatusBarAlignment.Right,
    99
  );
  qBtn.text = "$(question) 单题";
  qBtn.tooltip = "点击后输入函数名，只跑那一题";
  qBtn.command = "cs61a.testOne";
  qBtn.show();

  context.subscriptions.push(testBtn, qBtn);

  context.subscriptions.push(
    vscode.commands.registerCommand("cs61a.testHere", async () => {
      const editor = vscode.window.activeTextEditor;
      const target = editor
        ? findOkFor(editor.document.fileName)
        : findOkFor(path.join(findWorkspaceRoot() || "", "x.py"));
      await runTest(target, []);
    })
  );

  context.subscriptions.push(
    vscode.commands.registerCommand("cs61a.testOne", async () => {
      const editor = vscode.window.activeTextEditor;
      const target = editor
        ? findOkFor(editor.document.fileName)
        : findOkFor(path.join(findWorkspaceRoot() || "", "x.py"));
      if (!target) {
        vscode.window.showWarningMessage("CS61A: 没找到 ok 测试文件。");
        return;
      }
      const q = await vscode.window.showInputBox({
        title: "只跑哪一题？",
        prompt: "输入函数名，例如 hailstone",
        placeHolder: "hailstone",
      });
      if (!q) return;
      await runTest(target, ["-q", q]);
    })
  );

  // 右键菜单：文件上直接测
  context.subscriptions.push(
    vscode.commands.registerCommand("cs61a.testFile", async (uri) => {
      const p = uri && uri.fsPath ? uri.fsPath : "";
      const target = p ? findOkFor(p) : null;
      await runTest(target, []);
    })
  );
}

function deactivate() {}

module.exports = { activate, deactivate };
