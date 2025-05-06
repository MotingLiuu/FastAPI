from fastapi import APIRouter

app1 = APIRouter()

@app1.get("/user/{id}")
def get_user(id: int):
    print("id:", id, type(id))
    return {"user": id}
