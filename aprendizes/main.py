from fastapi import FastAPI, Path
from database import aprendizes
from base_models import Item, UpdateItem


app = FastAPI()

@app.get("/all")
async def root():
    return aprendizes

@app.get("/get-item/{item_id}")
def get_item(
    item_id : int = Path(
        description = 'Fill with id of the item you want to view')):
    
    search = list(filter(lambda x: x["id"] == item_id, aprendizes))

    if search == []:
        return {'Error': 'Item does not exist'}

    return {'Item': search[0]}

    
@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):

    search = list(filter(lambda x: x["id"] == item_id, aprendizes))

    if search != []:
        return {'Error': 'Item exists'}

    item = item.dict()
    item['id'] = item_id

    aprendizes.append(item)
    return item


@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: UpdateItem):

    search = list(filter(lambda x: x["id"] == item_id, aprendizes))

    if search == []:
        return {'Item': 'Does not exist'}

    return search


@app.delete('/delete-item/{item_id}')
def delete_item(item_id: int):
    search = list(filter(lambda x: x["id"] == item_id, aprendizes))

    if search == []:
        return {'Item': 'Does not exist'}

    for i in range(len(aprendizes)):
        if aprendizes[i]['id'] == item_id:
            del aprendizes[i]
            break
    return {'Message': 'Item deleted successfully'}
