# 第08课：API 返回模型

## 这一课要解决什么

第07课之后，`/health` 已经被拆到了：

```text
app/api/health.py
```

现在它能正常返回：

```json
{
  "status": "ok",
  "service": "ai-knowledge-assistant",
  "environment": "development"
}
```

但这里还有一个小问题：

```text
返回结构只藏在函数里面，没有被正式声明出来。
```

这节课要做的事就是：

```text
给 /health 的返回结果定义一个模型。
```

## 什么是 API 返回模型

API 返回模型就是接口对外承诺的返回形状。

比如 `/health` 现在承诺返回：

```text
status      字符串
service     字符串
environment 字符串
```

这就像菜单上写清楚：

```text
这道菜里有什么。
```

不是后厨今天心情好就放三个字段，明天忘了就只放两个字段。

接口应该有稳定结构。

## 新增的 `schemas.py`

这一课新增了：

```text
app/api/schemas.py
```

它现在只有一个模型：

```python
class HealthResponse(BaseModel):
    status: str
    service: str
    environment: str
```

大白话：

```text
HealthResponse 规定了 /health 应该返回什么字段。
```

以后我们还会在这里继续放：

```text
DocumentUploadResponse
QuestionRequest
QuestionAnswerResponse
EvaluationResult
```

这些名字现在不用背，先知道 `schemas.py` 是“接口输入输出模型的集中存放处”。

## `BaseModel` 是什么

`BaseModel` 来自 Pydantic。

你可以把它理解成一个“数据表格模板”。

我们写：

```python
class HealthResponse(BaseModel):
    status: str
    service: str
    environment: str
```

意思是：

```text
这个模型需要三个字段，而且三个字段都应该是字符串。
```

这样数据结构就从“随手写的字典”变成了“有名字、有字段、有类型的对象”。

## `response_model` 是什么

在接口上我们写：

```python
@router.get("/health", response_model=HealthResponse)
```

这句话的大白话是：

```text
/health 这个接口的响应应该长得像 HealthResponse。
```

FastAPI 会把这个信息用于自动文档。

以后打开：

```text
http://127.0.0.1:8000/docs
```

你会看到 `/health` 的返回结构不再只是一个模糊的 JSON，而是有明确模型。

## 为什么不继续返回普通字典

普通字典当然能跑。

但它的问题是：

```text
结构靠人记
字段靠人别写错
类型靠人别传错
文档靠人自己解释
```

模型的好处是：

```text
结构写在类里
字段有名字
类型有标注
FastAPI 能自动生成文档
```

项目越往后做，模型越重要。

因为提问接口以后可能返回：

```text
answer          答案
sources         引用来源
confidence      置信度
latency_ms      延迟
token_cost      token 成本
```

如果都靠字典随手写，很快就会乱。

## 旁支小课堂：API 合同

API 合同就是前后端约定好的规则：

```text
你请求什么地址
你传什么参数
我返回什么字段
字段是什么类型
错误时怎么返回
```

真实公司里，前端、后端、测试经常不是同一个人。

如果后端随手改字段名，前端可能直接报错。

所以你要慢慢形成一个意识：

```text
接口不是函数返回值而已，接口是对外承诺。
```

## 今天新增了什么

```text
app/api/schemas.py
docs/第08课-API返回模型.md
```

并修改了：

```text
app/api/health.py
README.md
```

## 今天的验收标准

完成之后，你应该能做到：

1. 知道 API 返回模型是接口返回结构的正式声明。
2. 知道 `HealthResponse` 描述了 `/health` 的返回字段。
3. 知道 `response_model=HealthResponse` 是告诉 FastAPI 这个接口返回什么模型。
4. 知道普通字典能跑，但模型更适合长期维护。
5. 知道 API 合同是前后端之间的稳定约定。

