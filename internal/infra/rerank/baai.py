from sentence_transformers import CrossEncoder
from internal.domain.document import Document

class RerankBAAI:
    def __init__(self, model: CrossEncoder):
        self.model = model

    def rerank(self, query: str, documents: list) -> list[Document]:

        pairs = [(query, doc) for doc in documents]

        scores = self.model.predict(pairs)

        ranked = sorted (
            zip(documents, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        result = []
        for doc, score in ranked:
            print(f"{score:.4f} | {doc}")
            document = Document(document=doc, score=round(score, 4))
            result.append(document)

        return result