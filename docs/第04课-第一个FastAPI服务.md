# 第04课：第一个 FastAPI 服务

## 这一课要解决什么

前面三课，我们做的是项目地基：

```text
仓库有了
目录清楚了
运行环境准备好了
```

但到目前为止，这个项目还不会真正回应外界。

第04课要让它完成第一次“开口说话”：

```text
访问 /health
返回 {"status": "ok"}
```

这就是后端服务最小的生命体征。

## 什么是后端服务

大白话：后端服务就是一个在电脑上运行的程序，它一直等着别人来问问题。

别人可以是：

```text
浏览器
前端页面
手机 App
另一个后端程序
测试脚本
```

它们通过 HTTP 请求来和后端说话。

比如：

```text
GET /health
```

这句话像是在问：

```text
你还活着吗？
```

如果服务正常，就回答：

```json
{
  "status": "ok",
  "service": "ai-knowledge-assistant"
}
```

## `app/main.py` 是什么

这一课新增了：

```text
app/main.py
```

它是后端应用的入口文件。

你可以把它理解成餐馆开门时挂出的第一块营业牌：

```text
本店已开门，菜单在这里，点菜窗口在这里。
```

里面最重要的是这一句：

```python
app = FastAPI(...)
```

这行代码创建了一个 FastAPI 应用。

大白话：

```text
从这一刻开始，我们有了一个能接收 HTTP 请求的后端程序。
```

## `/health` 是什么

`/health` 是健康检查接口。

健康检查接口一般不做复杂业务。

它只负责回答：

```text
服务有没有正常启动？
最基本的请求能不能进来？
程序能不能正常返回 JSON？
```

我们写的是：

```python
@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "ai-knowledge-assistant",
    }
```

这里有两个新概念。

### `@app.get("/health")`

这一行叫装饰器。

先不用害怕这个词。

你可以把它理解成给函数挂了一个门牌：

```text
有人用 GET 方法访问 /health 时，就来找下面这个函数。
```

### `health_check`

这是普通 Python 函数。

它返回一个字典：

```python
{
    "status": "ok",
    "service": "ai-knowledge-assistant",
}
```

FastAPI 会自动把这个 Python 字典变成 JSON。

也就是说，你写的是 Python：

```python
dict
```

用户收到的是接口响应：

```json
{
  "status": "ok",
  "service": "ai-knowledge-assistant"
}
```

## 怎么启动服务

在项目根目录执行：

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

这条命令看起来长，我们拆开看：

```text
.\.venv\Scripts\python.exe
```

意思是：

```text
用当前项目虚拟环境里的 Python。
```

```text
-m uvicorn
```

意思是：

```text
用 Python 启动 uvicorn 这个服务器工具。
```

```text
app.main:app
```

意思是：

```text
去 app/main.py 里找到名叫 app 的 FastAPI 应用。
```

```text
--reload
```

意思是：

```text
开发模式下，代码改了自动重启服务。
```

启动后你通常会看到：

```text
Uvicorn running on http://127.0.0.1:8000
```

这表示服务已经在本机 8000 端口等请求了。

## 怎么访问接口

浏览器打开：

```text
http://127.0.0.1:8000/health
```

应该能看到：

```json
{
  "status": "ok",
  "service": "ai-knowledge-assistant"
}
```

这就是我们的后端第一次成功回应外界。

## 今天的实际验证结果

我们做了两种验证。

第一种是测试验证：

```text
1 passed
```

这说明 `tests/test_health.py` 能确认 `/health` 返回正确结果。

第二种是真实 HTTP 验证：

```text
200
{'status': 'ok', 'service': 'ai-knowledge-assistant'}
```

这说明服务真的能通过 HTTP 回应请求。

中间尝试用 PowerShell 的 `Start-Process` 启动后台服务时，遇到了一个环境变量大小写冲突：

```text
Key in dictionary: 'PATH'  Key being added: 'Path'
```

这不是 FastAPI 代码坏了，而是当前 PowerShell 运行环境里同时出现了 `PATH` 和 `Path` 两个键。

所以我们换成了 Python 内部启动 Uvicorn、发请求、再自动关闭的方式完成验证。

工程里要慢慢习惯这个判断：

```text
启动方式报错，不一定等于业务代码报错。
```

## 为什么要写测试

这一课还新增了：

```text
tests/test_health.py
```

测试文件的作用不是装样子。

它像一个小质检员，每次都帮你问一遍：

```text
/health 还能不能返回 200？
返回内容是不是我们期待的？
```

运行测试：

```powershell
.\.venv\Scripts\python.exe -m pytest
```

如果看到类似：

```text
1 passed
```

说明最小接口是好的。

## 为什么新增 `pytest.ini`

这台机器运行测试时，Pytest 默认想在项目根目录创建缓存：

```text
.pytest_cache/
```

缓存只是为了让 Pytest 下次运行更快一点，不影响接口本身。

但当前环境对临时缓存目录权限比较敏感，所以第一次测试虽然通过了，却出现了缓存 warning。

它还留下过类似这样的临时目录：

```text
pytest-cache-files-xxxx/
```

这些也只是测试缓存残留，不是项目代码。

为了让新手阶段的输出更干净，我们新增了：

```text
pytest.ini
```

里面写：

```ini
[pytest]
addopts = -p no:cacheprovider
```

大白话：

```text
Pytest，这个项目先别创建缓存，认真跑测试就行。
```

这样以后看到测试输出，就更容易聚焦在真正重要的结果：

```text
passed 或 failed
```

## 今天新增了什么

```text
app/main.py
tests/test_health.py
docs/第04课-第一个FastAPI服务.md
pytest.ini
```

还在 `requirements.txt` 里新增了：

```text
httpx
```

因为 FastAPI 的测试客户端需要它来模拟请求。

## 今天的验收标准

完成之后，你应该能做到：

1. 知道 `app/main.py` 是后端入口。
2. 知道 `/health` 是健康检查接口。
3. 知道 `@app.get("/health")` 是给函数挂接口门牌。
4. 知道 `uvicorn app.main:app --reload` 是启动服务。
5. 知道测试不是形式主义，而是帮你确认接口没有坏。
