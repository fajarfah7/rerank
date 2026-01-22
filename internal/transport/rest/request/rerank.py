from pydantic import BaseModel

class RequestRerank(BaseModel):
    query: str
    documents: list[str]