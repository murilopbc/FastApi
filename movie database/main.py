from fastapi import FastAPI, HTTPException, Path, Response, status
from models import Filme
import requests
from datetime import date

app = FastAPI()

filmes = {
    1: {
        "title": "Godzilla e Kong: O Novo Império",
        "released": "28/03/2024",
        "overview":"O poderoso Kong e o temível Godzilla se unem contra uma colossal ameaça mortal escondida no mundo dos humanos, que ameaça a existência de sua espécie e da nossa. Mergulhando profundamente nos mistérios da Ilha da Caveira e nas origens da Terra Oca, o filme irá explorar a antiga batalha de Titãs que ajudou a forjar esses seres extraordinários e os ligou à humanidade para sempre.",
        "director": "Adam Wingard",
        "vote_average": "67",
        "genre": "Action"

    },
    2: {
        "title": "Kung Fu Panda 4",
        "released": "21/03/2024",
        "overview":"Po está prestes a se tornar o novo líder espiritual do Vale da Paz, mas antes que possa fazer isso, ele deve encontrar um sucessor para se tornar o novo Dragão Guerreiro. Ele parece encontrar uma em Zhen, uma raposa com muitas habilidades promissoras, mas que não gosta muito da ideia de Po treiná-la.",
        "director": "Mike Mitchell",
        "vote_average": "67",
        "genre": "Animation"
    }
   
}

# MY API

@app.get('/filmes')
async def get_filmes():
    return filmes


@app.get('/filmes/{filme_id}')
async def get_filme(filme_id: int = Path(title='ID do Filme', description='Deve estar entre 1 e 2', gt=0, lt=3)):
    try:
        filme = filmes[filme_id]
        return filme
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid value type")
    
    
@app.post('/filmes', status_code=status.HTTP_201_CREATED)
async def create_filme(filme: Filme):
    if filme.id not in filmes:
        next_id = len(filmes) + 1
        filmes[next_id] = filme
        del filme.id
        return filme
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Already exists a movie with the ID {filme.id}")
    

@app.put('/filmes/{filme_id}')
async def update_filme(filme_id: int, filme: Filme):
    if filme_id in filmes:
        filmes[filme_id] = filme
        filme.id = filme_id
        del filme.id
        return filme
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    
    
@app.patch('/filmes/{filme_id}')
async def partial_update_filme(filme_id: int, filme_data: dict):
    if filme_id in filmes:
        filme = filmes[filme_id]
        for key, value in filme_data.items():
            setattr(filme, key, value)
        return filme
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    
@app.delete('/filmes/{filme_id}')
async def delete_filme(filme_id: int):
    if filme_id in filmes:
        del filmes[filme_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")


# CONSUMING ONLINE API WITH REQUESTS LIBRARY

@app.get('/movies')
async def get_api_tmdb():
    url = "https://api.themoviedb.org/3/movie/6/recommendations?api_key=07e9b188ce58e608d62827e85ec07ed5"
    response = requests.get(url)
    data = response.json()
    return data

# JOHN BEARD API
    
@app.get('/times/{time_id}')
async def get_time(time_id):

    time_id = int(time_id)
    url = (f"http://10.234.94.137:8000/times/{time_id}")
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        print("Não Encontrado!")


@app.get('/player/{player_name}')
async def get_player(player_name):

    player_name = str(player_name)
    url = (f"http://10.234.94.137:8000/jogador/{player_name}")
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        print("Não Encontrado!")


# JOHN NO BEARD API

@app.get('/times')
async def get_times():
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



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)