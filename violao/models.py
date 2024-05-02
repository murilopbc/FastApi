from typing import Optional
from pydantic import BaseModel

class Violao(BaseModel):
    id: Optional[int] = None
    nome: str
    marca: str
    preco: float
    modelo: str

    