# 第07课：API 路由拆分

## 这一课要解决什么

第04课里，我们把 `/health` 直接写在了：

```text
app/main.py
```

这在项目刚开始时没问题。

但如果以后继续往里面加接口，比如：

```text
/documents/upload
/questions/ask
/evaluations/run
/models/list
```

`main.py` 很快就会变成一个大杂烩。

第07课要做的事很简单：

```text
把健康检查接口从 main.py 拆到 app/api/health.py。
```

接口地址不变，还是：

```text
GET /health
```

只是代码摆放位置更清楚了。

## `main.py` 应该负责什么

大白话：`main.py` 是总开关，不应该什么活都自己干。

它适合负责：

```text
创建 FastAPI 应用
读取基础配置
注册路由
以后注册中间件
以后注册启动和关闭事件
```

它不适合塞满所有接口函数。

如果 `main.py` 里同时写上传、检索、问答、评测、用户管理，后面你会很难找东西。

所以我们让它更像一家店的总经理：

```text
不亲自做每一道菜，但知道每个窗口在哪里。
```

## `app/api/health.py` 是什么

这一课新增了：

```text
app/api/health.py
```

它专门放健康检查接口。

以后你看到这个文件名，就能立刻知道：

```text
这里管 /health。
```

这比把所有接口都堆在 `main.py` 里清楚得多。

## `APIRouter` 是什么

`APIRouter` 可以理解成一个“小路由本”。

以前我们直接在 `app` 上挂接口：

```python
@app.get("/health")
```

现在改成在 `router` 上挂接口：

```python
router = APIRouter(tags=["system"])

@router.get("/health")
def health_check():
    ...
```

大白话：

```text
先把 /health 记在 health.py 这个小本子上。
```

然后在 `main.py` 里写：

```python
app.include_router(health_router)
```

意思是：

```text
把 health.py 这个小本子登记到 FastAPI 总应用里。
```

## 拆分前后有什么变化

拆分前：

```text
main.py
  创建 app
  写 /health 接口
```

拆分后：

```text
main.py
  创建 app
  注册 health_router

api/health.py
  写 /health 接口
```

对用户来说，没有变化。

用户访问的仍然是：

```text
http://127.0.0.1:8000/health
```

返回的仍然是：

```json
{
  "status": "ok",
  "service": "ai-knowledge-assistant",
  "environment": "development"
}
```

对开发者来说，变化很大。

因为以后加新接口时，我们可以继续拆：

```text
app/api/documents.py   文档上传、文档列表
app/api/questions.py   提问、答案生成
app/api/evaluations.py 评测接口
```

每个文件管一类事。

## 为什么测试不用大改

测试文件仍然请求：

```text
GET /health
```

因为接口地址和返回内容没有变。

这说明一个很重要的工程原则：

```text
内部代码结构可以调整，但对外行为尽量保持稳定。
```

如果用户访问方式没变，测试也不需要跟着乱改。

## 今天新增了什么

```text
app/api/__init__.py
app/api/health.py
docs/第07课-API路由拆分.md
```

并修改了：

```text
app/main.py
README.md
```

## 今天的验收标准

完成之后，你应该能做到：

1. 知道 `main.py` 是应用总入口，不适合堆所有接口。
2. 知道 `app/api/health.py` 专门管理健康检查接口。
3. 知道 `APIRouter` 是一个可以被注册到 FastAPI 应用的小路由本。
4. 知道 `app.include_router(...)` 是把小路由本接进总应用。
5. 知道重构后的接口地址和返回结果应该保持不变。

