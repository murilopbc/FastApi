from pydantic import BaseModel, validator
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserCreate(BaseModel):
    name: str
    sobrenome: str
    idade: int

    @validator('idade')
    def validarIdade(cls, value):
        if value < 0:
            raise ValueError('Idade deve ser maior que 0')
        return value
    
class UserRead(BaseModel):
    id: int
    name: str
    sobrenome: str
    idade: int


class UserUpdate(BaseModel):
    name: str
    sobrenome: str
    idade: int

    @validator('idade')
    def validarIdade(cls, value):
        if value < 0:
            raise ValueError('Idade deve ser maior que 0')
        return value


class UserDB(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index=True)
    name = Column(String, index=True)
    sobrenome = Column(String, index=True)
    idade = Column(Integer, index=True)


