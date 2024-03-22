# from fastapi import FastAPI

# from typing import Optional
# from pydantic import BaseModel, Field, EmailStr, HttpUrl

# app = FastAPI()


# @app.get("/api/healthchecker")
# def root():
#     return {"message": "Welcome to FastAPI!"}

# @app.get("/api/main")
# def root1():
#     return {"message": "Welcome to MAIN!"}

# @app.get("/notes/{note_id}")
# async def read_note(note_id: int):
#     return {"note": note_id}


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items")
async def create_item(item: Item):
    return item

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id" : item_id}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id" : item_id, "item" : item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"item_id" : item_id}

