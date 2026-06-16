from fastapi import FastAPI

from app.core.config import get_settings


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="A step-by-step AI knowledge assistant project.",
    version=settings.app_version,
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": settings.service_name,
        "environment": settings.app_env,
    }
