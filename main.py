from fastapi import FastAPI
from pydantic import BaseModel
from src.routes import tags, notes

app = FastAPI()

app.include_router(tags.router, prefix='/api')
app.include_router(notes.router, prefix='/api')

@app.get('/')
def read_root():
    return {"message": "Hello FastAPI"}














# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float = None

# @app.post("/items")
# async def create_item(item: Item):
#     return item

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id" : item_id}


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id" : item_id, "item" : item}


# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):
#     return {"item_id" : item_id}

