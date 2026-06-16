# 第01课：从 GitHub 仓库开始

## 这一课要解决什么

你之前觉得“学了忘、忘了学”，核心原因通常不是记性差，而是知识没有挂到一个长期项目上。

从今天开始，我们不再把学习拆成零散知识点，而是把所有知识都塞进同一个项目里：

```text
AI 知识库助手
```

以后你学的每个东西，都要回答一个问题：

```text
它能让这个项目多一个什么能力？
```

## Git 是什么

大白话：Git 就是项目的“存档系统”。

你每完成一个小功能，就可以存一次档。以后代码坏了，可以回头看之前哪一步是好的。

## GitHub 是什么

大白话：GitHub 就是把你的 Git 存档放到网上。

它有三个作用：

1. 防止本地电脑出问题导致项目丢失。
2. 让别人能看到你的项目。
3. 让实习面试官看到你不是只会说，而是真的做过。

## 仓库是什么

仓库就是一个项目的家。

比如这个项目的仓库可以叫：

```text
ai-knowledge-assistant
```

里面会放代码、文档、实验记录、项目说明。

## 今天你需要记住的 3 个命令

```powershell
git init
git status
git add .
git commit -m "init project"
```

它们的大白话解释：

- `git init`：告诉 Git，这个文件夹以后要被你管理。
- `git status`：看看哪些文件还没有存档。
- `git add .`：把当前所有变化放进本次存档篮子里。
- `git commit -m "init project"`：正式存档，并写一句说明。

## 敲下命令之后，发生了什么

### `git init`

你敲下：

```powershell
git init
```

表面上好像什么都没发生，但项目文件夹里会多出一个隐藏目录：

```text
.git/
```

这个 `.git` 就像项目的“地下档案室”。你平时写代码是在地面上活动，Git 会在这个档案室里记录：

- 哪些文件出现过
- 哪些文件改过
- 每一次存档长什么样
- 当前项目停在哪个分支

如果没有 `.git`，这个文件夹只是普通文件夹。

有了 `.git`，它才变成一个 Git 仓库。

### `git status`

你敲下：

```powershell
git status
```

这一步不会修改任何文件，它只是让 Git 给你报个平安：

```text
现在有哪些文件是新的？
哪些文件改过？
哪些文件已经准备存档？
```

你可以把它理解成玩游戏前看一眼背包：

```text
我现在手上有什么东西？
哪些东西还没放进仓库？
```

所以以后你不知道项目处于什么状态时，先敲 `git status`。它是最不容易犯错、也最适合新手的命令。

### `git add .`

你敲下：

```powershell
git add .
```

这里的点 `.` 表示“当前文件夹里的所有变化”。

这一步不是正式存档，而是把文件放进“待存档区”。

可以想象成你要寄快递：

```text
写代码          = 东西散在桌上
git add .       = 把东西装进箱子
git commit      = 封箱并贴上快递单
```

执行完 `git add .` 后，再看 `git status`，你会发现文件从“未跟踪”变成“准备提交”。

这说明 Git 已经知道：这些文件准备进入下一次存档。

### `git commit -m "init project"`

你敲下：

```powershell
git commit -m "init project"
```

这一刻，Git 才真的创建了一个存档点。

`"init project"` 是这次存档的说明。以后你回头看历史记录时，会看到类似：

```text
5aa54f2 init project
```

前面的 `5aa54f2` 是这次存档的编号，后面的 `init project` 是你给它写的备注。

这就像游戏存档列表：

```text
存档 1：init project
存档 2：add file upload API
存档 3：add document parser
```

以后项目写坏了，不是“完了全乱了”，而是可以回头看：

```text
是哪一次提交之后坏掉的？
坏之前的代码长什么样？
```

这就是 Git 对工程师最真实的价值：它不是为了背命令，而是为了让你敢改代码。

## 本地仓库和 GitHub 仓库的区别

现在这个项目已经在你电脑上有存档了，但 GitHub 网页还不知道这些文件。

本地 Git 仓库像你电脑里的单机存档。

GitHub 仓库像云端存档。

要把本地存档发到 GitHub，需要后面两个动作：

```powershell
git remote add origin https://github.com/ljkkkkkk/ai-knowledge-assistant.git
git push -u origin main
```

大白话解释：

- `git remote add origin ...`：告诉本地项目，云端仓库地址在哪里。
- `git push -u origin main`：把本地 `main` 分支的存档上传到 GitHub。

上传成功后，你刷新 GitHub 页面，就能看到 `README.md`、`docs/`、`app/` 这些文件。

这时候项目才真正从“我电脑上有”变成“网上也能看到”。

## 今天的验收标准

完成之后，你应该能做到：

1. 本地有一个项目文件夹。
2. 项目里有 `README.md`。
3. 项目已经被 Git 管理。
4. 你知道 Git 和 GitHub 的区别。
5. 你知道下一步是把本地项目推到 GitHub。
