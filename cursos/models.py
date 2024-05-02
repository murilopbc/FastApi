from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int] = None
    name: str
    classes: int
    hours: int
    instructor: str
    