from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    age: int
    edv: int

class UpdateItem(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    edv: Optional[int] = None