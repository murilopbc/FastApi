from pydantic.v1 import BaseSettings

from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):

    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'myslq+asyncmy://root@127.0.0.1:3306/etscursos'
    DBBaseModel = declarative_base()

settings = Settings() 