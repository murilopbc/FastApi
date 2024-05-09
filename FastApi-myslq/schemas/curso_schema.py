from typing import Optional
from pydantic import BaseModel as SchemaBaseModel

# Validação dos dados

class CursoSchema(SchemaBaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    instrutor: str

    class Config:
        from_atributes = True