from sentence_transformers import CrossEncoder
from internal.domain.document import Document
import os

class RerankBAAI:
    def __init__(self, model: CrossEncoder):
        self.model = model

    def rerank(self, query: str, documents: list) -> list[Document]:
        top_n = int(os.getenv("TOP_N"))
        if top_n <= 0:
            top_n = 3

        pairs = [(query, doc) for doc in documents]

        scores = self.model.predict(pairs)

        ranked = sorted (
            zip(documents, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        top_k = ranked[:top_n]

        result = []
        for doc, score in top_k:
            print(f"{score:.4f} | {doc}")
            document = Document(document=doc, score=round(score, 4))
            result.append(document)

        return result