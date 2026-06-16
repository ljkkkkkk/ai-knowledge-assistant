from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    service: str
    environment: str


class QuestionRequest(BaseModel):
    question: str


class QuestionAnswerResponse(BaseModel):
    question: str
    answer: str
    sources: list[str]
