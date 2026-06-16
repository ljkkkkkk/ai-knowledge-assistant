# Lesson 03: Python 虚拟环境和依赖管理

## 这一课要解决什么

前两课我们做了两件事：

```text
Lesson 01: 项目有了 GitHub 仓库
Lesson 02: 项目有了清楚的房间布局
```

现在问题来了：

```text
这个项目以后要靠哪些 Python 包运行？
这些包应该装在哪里？
真实密码应该放在哪里？
```

Lesson 03 要解决的就是“运行环境”问题。

你可以把它理解成：

```text
项目不只是几份代码文件，它还需要自己的工具箱和配置柜。
```

## 为什么不能把包乱装在电脑大环境里

假设你电脑里有两个项目。

第一个项目需要：

```text
fastapi 0.95
```

第二个项目需要：

```text
fastapi 0.115
```

如果所有包都装在电脑的全局 Python 里，就像全宿舍共用一个牙刷杯：

```text
刚开始省事，时间久了必乱。
```

你今天升级一个包，可能明天另一个项目就跑不起来。

所以每个项目最好有自己的虚拟环境：

```text
.venv/
```

大白话：虚拟环境就是这个项目自己的“小厨房”。

这个项目需要的锅、铲子、调料，都放在自己的小厨房里，不去污染别的项目。

## `.venv` 是什么

`.venv` 是 Python 虚拟环境文件夹。

如果你执行：

```powershell
python -m venv .venv
```

项目里会多出一个目录：

```text
.venv/
```

这个目录里会有一份专门给当前项目用的 Python 和包管理工具。

注意：`.venv` 很大，而且每个人电脑都能自己生成，所以它不应该上传 GitHub。

这就是为什么 `.gitignore` 里有：

```text
.venv/
```

这行的意思是：

```text
Git，别管虚拟环境文件夹。
```

## 激活虚拟环境是什么意思

创建 `.venv` 只是把小厨房建好了。

激活虚拟环境，才是告诉终端：

```text
接下来做饭，用这个项目自己的厨房。
```

Windows PowerShell 里通常是：

```powershell
.\.venv\Scripts\Activate.ps1
```

激活后，你可能会看到命令行前面多一个：

```text
(.venv)
```

这就像终端戴了一个小牌子提醒你：

```text
你现在正在这个项目的虚拟环境里。
```

## `requirements.txt` 是什么

`requirements.txt` 是依赖清单。

它告诉别人：

```text
这个项目需要安装哪些 Python 包，版本是多少。
```

我们现在先写入这些包：

```text
fastapi
uvicorn
pydantic-settings
python-dotenv
pytest
```

它们分别负责什么？

### `fastapi`

FastAPI 是后端 Web 框架。

后面我们要写接口，比如：

```text
GET /health
POST /documents/upload
POST /questions/ask
```

这些接口就靠 FastAPI 搭起来。

### `uvicorn`

Uvicorn 是服务器。

FastAPI 更像“餐馆的菜单和后厨规则”，Uvicorn 像真正把门打开接客的服务员。

以后你会看到类似命令：

```powershell
uvicorn app.main:app --reload
```

这句话的大白话是：

```text
启动 app/main.py 里的 FastAPI 应用，并且代码改了就自动重载。
```

### `pydantic-settings`

它用来管理配置。

比如：

```text
项目名字
运行环境
数据库地址
模型名称
```

这些配置不应该散落在代码各处，后面我们会统一放进 `app/core/`。

### `python-dotenv`

它负责读取 `.env` 文件。

`.env` 是本地配置文件，里面可以放真实密钥和密码。

比如：

```text
DATABASE_URL=mysql+pymysql://root:真实密码@localhost:3306/ai_knowledge_assistant
OPENAI_API_KEY=真实 API Key
```

但 `.env` 绝对不能上传 GitHub。

原因很简单：

```text
GitHub 是公开门面，.env 是你家的钥匙串。
```

门面可以给别人看，钥匙串不能挂门口。

### `pytest`

Pytest 是测试工具。

以后我们写完一个函数，不只靠肉眼看，还要写测试确认它真的工作。

测试不是为了折磨自己，而是为了让你敢改代码。

## `.env.example` 是什么

`.env.example` 是环境变量模板。

它可以上传 GitHub，因为里面不放真实密码，只放占位符。

它的作用是告诉别人：

```text
如果你要运行这个项目，需要准备这些配置。
```

比如我们现在放了：

```text
DATABASE_URL=mysql+pymysql://USERNAME:PASSWORD@localhost:3306/ai_knowledge_assistant
OPENAI_API_KEY=your_api_key_here
```

看到这里要注意：

```text
真实账号密码只写在 .env
模板占位符写在 .env.example
```

`.gitignore` 里已经有：

```text
.env
.env.*
```

这表示 Git 默认不会把真实 `.env` 存进仓库。

## 关于数据库，我们先不急着连

你提到本地 MySQL 可能有账号密码。

这个信息后面会有用，但现在先不急着连数据库。

原因是：

```text
我们还没有 API，也还没有文档数据，过早接数据库只会增加干扰。
```

后面真正接数据库时，我们会按这个顺序来：

```text
先写一个最小 FastAPI 服务
再写配置读取
再决定数据库
最后才把数据库连接接进项目
```

这样你不会陷入“数据库、框架、模型、接口全搅在一起”的混乱状态。

## 今天新增了什么

这一课新增了：

```text
requirements.txt
.env.example
docs/lesson-03-python-env-and-dependencies.md
```

它们分别像：

```text
requirements.txt = 采购清单
.env.example     = 配置表模板
Lesson 03        = 使用说明和学习笔记
```

## 今天实际遇到的坑

这次我们真的创建了虚拟环境和安装依赖，中间遇到了两个很典型的问题。

### 坑 1：`python -m venv .venv` 创建到一半失败

错误发生在：

```text
ensurepip
```

大白话：虚拟环境本体建好了，但里面的 `pip` 没装好。

`pip` 是 Python 的包安装器。没有它，就不能在虚拟环境里安装 FastAPI。

这就像厨房已经装修好了，但采购工具还没放进去。

我们最后的处理方式是：

```text
先确认 .venv 里的 Python 能运行
再单独给 .venv 补装 pip
```

### 坑 2：pip 临时目录权限问题

安装依赖时，pip 需要下载包、解压包、临时存放文件。

它默认想把临时文件放到系统临时目录里，但当前环境权限不稳定，所以我们给它指定了项目内部的临时目录：

```text
.tmp/
```

`.tmp/` 只是本地临时垃圾桶，不应该上传 GitHub。

所以 `.gitignore` 里加了：

```text
.tmp/
```

这行的意思是：

```text
Git，别管这些临时安装文件。
```

### 坑 3：`.env.example` 差点被忽略

一开始 `.gitignore` 里有：

```text
.env
.env.*
```

这能保护真实密钥，但也会误伤 `.env.example`。

因为 `.env.example` 也符合 `.env.*`。

所以我们加了一行：

```text
!.env.example
```

这个感叹号的意思是：

```text
前面虽然忽略了 .env.*，但 .env.example 这个模板文件要保留下来。
```

这就是 `.gitignore` 里常见的“先排除，再放行”。

## 今天的验收标准

完成之后，你应该能做到：

1. 知道 `.venv` 是项目自己的 Python 小厨房。
2. 知道 `requirements.txt` 是依赖清单。
3. 知道 `.env` 不能上传 GitHub。
4. 知道 `.env.example` 可以上传，因为它只放模板。
5. 知道数据库密码后面要放进 `.env`，而不是写进代码或 README。
6. 知道环境报错不等于你学不会，很多时候只是临时目录、权限、网络这些工程问题。
