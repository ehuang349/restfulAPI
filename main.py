from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


# Data model

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# In-memory database replacement
items_db = []


@app.get("/api/")
def read_root():
    return {"message": "Hello World"}


@app.get("/api/items/", response_model=List[Item])
def read_items():
    return items_db


@app.post("/api/items/", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item


@app.get("/api/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return item


@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items_db.pop(item_id)
    return {"deleted": deleted_item.name}
