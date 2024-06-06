from core.configs import settings
from sqlalchemy import Column, Integer, String

# Criar modelo tabela no banco de dados

class FilmeModel(settings.DBBaseModel):
    __tablename__ = "filmes"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    data_lancamento: str = Column(String(10))
    genero: str = Column(String(15))
    avaliacao: int = Column(Integer)
    diretor: str = Column(String(100))
    