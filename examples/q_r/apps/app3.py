from fastapi import APIRouter
from pydantic import BaseModel, Field, validator
from datetime import date
from typing import *

app3 = APIRouter()

class User(BaseModel):
    name: str
    age: int = Field(default=0, gt=0, lt=100)
    birth: Union[date, None] = None
    frinds: List[int] = []
    descroption: Union[str, None] = None  
    
    @validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), "name must be alphas"
        return value
          
@app3.post("/data")
async def data(user: User):
    print(user, type(user))
    print(user.name, user.birth)
    print(user.dict())
    return user