from fastapi import APIRouter
from fastapi import Request

app6 = APIRouter()

@app6.post("/items")
async def items(request: Request):
    print("URL:", request.url)
    print("IP:", request.client.host)
    print("Host", request.headers.get("user-agent"))
    return {
        "URL": request.url
    }