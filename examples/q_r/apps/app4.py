from fastapi import APIRouter
from fastapi import Form

app4 = APIRouter()

@app4.post("/regin")
async def data(username: str = Form(), password: str = Form()):
    print(f"username: {username}, password: {password}")
    return {
        "username": username
    }