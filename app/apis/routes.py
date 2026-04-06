from fastapi import APIRouter
from app.graph.workflow import build_graph
from app.schemas.request import QueryRequest, QueryResponse

router = APIRouter()
graph = build_graph()

@router.post("/query",response_model=QueryResponse)
async def query(request:QueryRequest):
    result = graph.invoke({"user_query": request.query})
    return QueryResponse(response= result["answer"])