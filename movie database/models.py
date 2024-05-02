from typing import Optional
from pydantic import BaseModel

class Filme(BaseModel):
    id: Optional[int] = None
    title: str
    released: str
    overview: str
    director: str
    vote_average: int
    genre: str

