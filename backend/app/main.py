from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="PolicyPilot AI",
    description="Enterprise RAG assistant with KVKK-aware guardrails",
    version="0.1.0",
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "app": "PolicyPilot AI",
        "status": "running"
    }