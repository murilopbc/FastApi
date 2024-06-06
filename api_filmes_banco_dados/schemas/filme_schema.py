from typing import Optional
from pydantic import BaseModel as SchemaBaseModel

# Validação dos dados

class FilmeSchema(SchemaBaseModel):
    id: Optional[int] = None
    titulo: str
    data_lancamento: str
    genero: str
    avaliacao: int
    diretor: str

    class Config:
        from_atributes = True