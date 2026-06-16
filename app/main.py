from fastapi import FastAPI


app = FastAPI(
    title="AI Knowledge Assistant",
    description="A step-by-step AI knowledge assistant project.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "ai-knowledge-assistant",
    }

