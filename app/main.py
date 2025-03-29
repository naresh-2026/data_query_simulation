from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from app.services import process_query, explain_query, validate_query
from app.auth import get_api_key

app = FastAPI(title="Mini Data Query Engine")

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query(request: QueryRequest, api_key: str = Depends(get_api_key)):
    return process_query(request.query)

@app.post("/explain")
def explain(request: QueryRequest, api_key: str = Depends(get_api_key)):
    return explain_query(request.query)

@app.post("/validate")
def validate(request: QueryRequest, api_key: str = Depends(get_api_key)):
    return validate_query(request.query)
