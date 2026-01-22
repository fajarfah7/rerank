from fastapi import FastAPI
from sentence_transformers import CrossEncoder
from dotenv import load_dotenv
from internal.domain.document import Document
from internal.config.rerank_model import new_rerank_model_baai
from internal.transport.rest.rerank_router import rerank_router
import os

load_dotenv()
model = new_rerank_model_baai()
app = FastAPI(title="Rerank Service")

@app.get("/healthz")
def healthz() -> str:
    return os.getenv("APP_NAME")

app.include_router(rerank_router(model=model))