import random
from fastapi import FastAPI, HTTPException, Response, status
from models import Violao
import requests
from datetime import date

app = FastAPI()

violoes = {
    1: {
        "nome": "Violão Folk GD11",
        "marca": "Takamine",
        "preco": 2700,
        "modelo": "Folk"
    },
    2: {
        "nome": "Violão MR710",
        "marca": "Cort",
        "preco": 3500,
        "modelo": "Jumbo"
    }
}

# MY API

@app.get('/violoes')
async def get_violoes():
    return violoes


@app.get('/violoes/{violao_id}')
async def get_violao(violao_id: int):
    try:    
        violao = violoes[violao_id]
        return violao
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Guitar not found")
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid value type")


@app.post('/violoes', status_code=status.HTTP_201_CREATED)
async def create_violao(violao: Violao):
    if violao.id not in violoes:
        next_id = len(violoes) + 1
        violoes[next_id] = violao
        del violao.id
        return violao
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Already exists a guitar with the ID {violao.id}")
    

@app.put('/violoes/{violao_id}')
async def update_violao(violao_id: int, violao: Violao):
    if violao_id in violoes:
        violoes[violao_id] = violao
        violao.id = violao_id
        del violao.id
        return violao
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Guitar not found")
    

@app.delete('/violoes/{violao_id}')
async def delete_violao(violao_id: int):
    if violao_id in violoes:
        del violoes[violao_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Guitar not found")

# JOHN BEARD API
    
@app.get('/times/{time_id}')
async def get_times(time_id):

    time_id = int(time_id)
    url = (f"http://10.234.94.137:8000/times/{time_id}")
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        print("Não Encontrado!")

# JOHN NO BEARD API

@app.get('/times')
async def get_api_teste():
    url = ("http://10.234.89.51:8000/times")
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        print("Não Encontrado!")
      

# GET NASA(ASTRONOMY PICTURE OF THE DAY) ONLINE API
        
 # API_KEY =  sqGvFYcfX4iGdXUaRffs4Vcm2NC3yEnziiwGEAOg


@app.get('/nasa')
async def get_api_nasa():
    data_atual = date.today()
    url = (f"https://api.nasa.gov/planetary/apod?date={data_atual}&api_key=sqGvFYcfX4iGdXUaRffs4Vcm2NC3yEnziiwGEAOg")
    response = requests.get(url)
    data = response.json()
    return data

@app.get('/nomes')
async def get_api_ibge():
    nomes = ['Murilo', 'João', 'Caio']
    nome = random.choice(nomes)
    url = (f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}")
    response = requests.get(url)
    data = response.json()
    return data


    
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)