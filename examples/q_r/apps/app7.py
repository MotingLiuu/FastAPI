from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

app7 = APIRouter()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app7.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app7.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]