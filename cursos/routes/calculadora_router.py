from fastapi import APIRouter
from typing import Optional
from fastapi import Header, Query

router = APIRouter()

# QUERY PARAMS
    
@router.get("/calculadora")
async def calcular(a: int, b: int, c: int):
    soma = a + b + c
    return {"resultado": soma}

@router.get("/calc")
async def calculate(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), x_test: str = Header(default=None),c: Optional[int] = 0):
    soma = a + b + c
    return {"resultado": soma}