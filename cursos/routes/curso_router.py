from fastapi import APIRouter
from time import sleep
from typing import Any
from fastapi import Depends, HTTPException, Header, Response, status, Query
from models import Curso

router = APIRouter()


cursos = {
    1: {
        "name": "Python",
        "classes": 20,
        "hours": 80,
        "instructor": "Cleber"
    },

    2: {
        "name": "Java",
        "classes": 15,
        "hours": 60,
        "instructor": "Leonardo"
    }
}


# GET METHOD (General)


@router.get('/cursos')
async def get_cursos():
    return cursos


# GET METHOD (Specifically)


@router.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Course not found')
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid value type')
    

# POST METHOD (Create)
    
    
@router.post('/cursos', status_code=status.HTTP_201_CREATED)
async def create_curso(curso: Curso):
    if curso.id not in cursos:
        next_id = len(cursos) + 1
        cursos[next_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Already exists a course with the ID {curso.id}")


# PUT METHOD (Update all the information about course)
    

@router.put('/cursos/{curso_id}')
async def update_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
            cursos[curso_id] = curso
            curso.id = curso_id
            del curso.id
            return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    

# DELETE METHOD
    

@router.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code = status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")


# INJECAO DE DEPENDENCIAS

def fake_db():
    try:
        print("Abrindo a conexão com banco de dados")
        sleep(1)
    except:
        pass
    finally:
        print("Fechando conexão com banco de dados")
        sleep(1)

async def get_cursos(db: Any = Depends(fake_db)):
    return db
    