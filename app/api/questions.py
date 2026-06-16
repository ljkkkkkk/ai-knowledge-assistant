from fastapi import APIRouter

from app.api.schemas import QuestionAnswerResponse, QuestionRequest


router = APIRouter(prefix="/questions", tags=["questions"])


@router.post("/ask", response_model=QuestionAnswerResponse)
def ask_question(request: QuestionRequest) -> QuestionAnswerResponse:
    return QuestionAnswerResponse(
        question=request.question,
        answer="This is a placeholder answer. Later, it will come from retrieved documents and an LLM.",
        sources=[],
    )
