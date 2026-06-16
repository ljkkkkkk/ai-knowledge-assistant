from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "ai-knowledge-assistant",
        "environment": "development",
    }


def test_app_metadata_comes_from_settings() -> None:
    assert app.title == "AI Knowledge Assistant"
    assert app.version == "0.1.0"
