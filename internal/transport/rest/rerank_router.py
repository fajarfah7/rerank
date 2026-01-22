from fastapi import APIRouter
from sentence_transformers import CrossEncoder
from fastapi.responses import JSONResponse
from internal.repository.rerank.base import RerankRepository
from internal.infra.rerank.baai import RerankBAAI
from internal.usecase.rerank import RerankService
from internal.domain.error import ResponseError
from internal.transport.rest.request.rerank import RequestRerank
from dataclasses import dataclass, asdict

def rerank_router(model: CrossEncoder) -> APIRouter:
    rerank_repository = RerankBAAI(model=model)
    handler = RerankRouter(rerank_repository=rerank_repository)

    router = APIRouter()
    router.post("/rerank")(handler.rerank)
    return router

class RerankRouter:
    def __init__(self, rerank_repository: RerankRepository):
        self.usecase = RerankService(rerank_repository=rerank_repository)

    def rerank(self, req: RequestRerank):
        try:
            result = self.usecase.rerank(query=req.query, documents=req.documents)
            return JSONResponse(status_code=200, content=result.model_dump())
        
        except Exception as e:
            err = ResponseError("ERR_HANDLER", str(e))
            return JSONResponse(status_code=500, content=err.asdict())