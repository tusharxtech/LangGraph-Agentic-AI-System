from fastapi import FastAPI
from app.apis.routes import router

app = FastAPI(title="LangGraph Tool Calling Agent")

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}