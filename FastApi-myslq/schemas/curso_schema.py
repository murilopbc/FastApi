from typing import Optional
from sqlalchemy import BaseModel as SchemaBaseModel

# Validação dos dados

class CursoSchema(SchemaBaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    instrutor: str

    class Config:
        orm_mode = True
        from_atributes = True