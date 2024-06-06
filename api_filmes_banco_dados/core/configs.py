from pydantic.v1 import BaseSettings

from sqlalchemy.orm import declarative_base

# Configurações iniciais

class Settings(BaseSettings):

    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+asyncmy://root:admin123@127.0.0.1:3306/tmdfilmes'
    DBBaseModel = declarative_base()

settings = Settings() 