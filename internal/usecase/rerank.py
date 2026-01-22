from internal.repository.rerank.base import RerankRepository
from internal.domain.document import Document
from internal.response.rerank import RerankedItem, RerankResponse

class RerankService:
    def __init__(self, rerank_repository: RerankRepository):
        self.rerank_repository = rerank_repository

    def rerank(self, query: str, documents: list) -> RerankResponse:
        result = self.rerank_repository.rerank(query=query, documents=documents)
        response = RerankResponse(
            data=[
                RerankedItem(
                    document=doc.document,
                    score=doc.score
                )
                for doc in result
            ]
        )

        return response

