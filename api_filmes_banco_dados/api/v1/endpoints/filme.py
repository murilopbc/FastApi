import sys
default_path = "C:\\Users\\ct67ca\\Desktop\\FastApi\\api_filmes_banco_dados"
sys.path.append(default_path)

from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.filme_model import FilmeModel
from schemas.filme_schema import FilmeSchema
from core.deps import get_session


router = APIRouter()


# POST FILME

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=FilmeSchema)
async def post_filme(filme: FilmeSchema, db: AsyncSession = Depends(get_session)):
    novo_filme = FilmeModel(titulo= filme.titulo, data_lancamento = filme.data_lancamento, genero = filme.genero, avaliacao = filme.avaliacao, diretor = filme.diretor)

    db.add(novo_filme)
    await db.commit()
    return novo_filme

# GET FILME

@router.get('/', response_model = List[FilmeSchema])
async def get_filmes(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FilmeModel)
        result = await session.execute(query)
        filmes: List[FilmeModel] = result.scalars().all()
        return filmes

# GET FILME BY ID
    
@router.get('/{filme_id}', response_model=FilmeSchema, status_code=status.HTTP_200_OK)
async def get_filme(filme_id: int, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FilmeModel).filter(FilmeModel.id == filme_id)
        result = await session.execute(query)
        filme = result.scalar_one_or_none()
        
        if filme:
            return filme
        else:
            raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado..."))
        
# UPDATE FILME
        
@router.put('/{filme_id}', response_model=FilmeSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_filme(filme_id: int, filme: FilmeSchema, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FilmeModel).filter(FilmeModel.id == filme_id)
        result = await session.execute(query)
        filme_up = result.scalar_one_or_none()
        
        if filme_up:
            filme_up.titulo = filme.titulo
            filme_up.data_lancamento = filme.data_lancamento
            filme_up.genero = filme.genero
            filme_up.avaliacao = filme.avaliacao
            filme_up.diretor = filme.diretor
            await session.commit()
            return filme_up
        else:
            raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado..."))


# DELETE FILME
        

@router.delete('/{filme_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_filme(filme_id:int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FilmeModel).filter(FilmeModel.id == filme_id)
        result = await session.execute(query)
        filme_del = result.scalar_one_or_none()
        if filme_del:
            await session.delete(filme_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado..."))


