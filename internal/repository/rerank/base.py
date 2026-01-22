
from typing import Protocol
from internal.domain.document import Document

class RerankRepository(Protocol):
    def rerank(self, query: str, documents: list) -> list[Document]:
        pass

