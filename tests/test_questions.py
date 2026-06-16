from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_ask_question_returns_placeholder_answer() -> None:
    response = client.post(
        "/questions/ask",
        json={"question": "What is RAG?"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "question": "What is RAG?",
        "answer": "This is a placeholder answer. Later, it will come from retrieved documents and an LLM.",
        "sources": [],
    }
