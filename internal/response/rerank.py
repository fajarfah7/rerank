from pydantic import BaseModel

class RerankedItem(BaseModel):
    document: str
    score: float

class RerankResponse(BaseModel):
    data: list[RerankedItem]