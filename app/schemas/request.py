from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    query: str = Field(..., example="Who won IPL 2025?")

class QueryResponse(BaseModel):
    response: str