# AI Knowledge Assistant

一个从 0 开始构建的 AI 知识库助手项目。

目标不是做一个只能演示的玩具，而是逐步做成一个能写进简历、能讲清楚技术细节、能部署和评测的项目。

## 项目最终形态

- 支持上传 PDF / TXT / Markdown 文档
- 自动解析文档并切分成片段
- 使用向量检索找到相关内容
- 调用大模型生成答案
- 回答时给出引用来源
- 提供简单评测：命中率、延迟、失败样例
- 使用 Docker 一键启动

## 当前阶段

第 1 阶段：创建项目、初始化 Git、连接 GitHub。

第 2 阶段：整理项目结构，让仓库看起来像一个可以长期维护的工程。

第 3 阶段：准备 Python 虚拟环境、依赖清单和环境变量模板。

第 4 阶段：创建第一个 FastAPI 服务和健康检查接口。

第 5 阶段：记录虚拟环境启动排错与项目运行方式。

第 6 阶段：引入配置管理，让应用名称、版本和运行环境从配置读取。

第 7 阶段：拆分 API 路由，让 `main.py` 保持简洁。

第 8 阶段：为 API 响应定义模型，让接口返回结构更清楚。

## 学习原则

每次只做一个小闭环：

1. 先知道这一步是为了解决什么问题。
2. 再动手完成一个具体产物。
3. 最后用自己的话复述它。

## 目录结构

```text
ai-knowledge-assistant/
  app/                # 后端主代码
    main.py           # FastAPI 应用入口
    api/              # 接口层：以后放上传、提问、健康检查等 API
      health.py       # 健康检查接口
      schemas.py      # API 请求和响应模型
    core/             # 核心配置：以后放配置项、日志、环境变量读取
      config.py       # 配置读取：从默认值和 .env 中读取项目设置
    services/         # 业务逻辑：以后放文档解析、检索、问答流程
  data/               # 本地数据、测试文档、索引文件
    samples/          # 示例文档
  docs/               # 学习笔记、项目设计、复盘
  scripts/            # 辅助脚本：以后放评测、数据处理、启动检查
  tests/              # 测试代码
  requirements.txt    # Python 依赖清单
  .env.example        # 环境变量模板，不放真实密码
  README.md           # 项目说明，给自己和面试官看的入口
```

## 学习记录

- [第01课：从 GitHub 仓库开始](docs/第01课-从GitHub仓库开始.md)
- [第02课：项目结构和 README](docs/第02课-项目结构和README.md)
- [第03课：Python 虚拟环境和依赖管理](docs/第03课-Python虚拟环境和依赖管理.md)
- [第04课：第一个 FastAPI 服务](docs/第04课-第一个FastAPI服务.md)
- [第05课：虚拟环境启动排错与项目运行](docs/第05课-虚拟环境启动排错与项目运行.md)
- [第06课：配置管理和环境变量](docs/第06课-配置管理和环境变量.md)
- [第07课：API 路由拆分](docs/第07课-API路由拆分.md)
- [第08课：API 返回模型](docs/第08课-API返回模型.md)

## 本地运行

安装依赖：

```powershell
.\scripts\install-deps.ps1
```

启动服务：

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

访问健康检查：

```text
http://127.0.0.1:8000/health
```
