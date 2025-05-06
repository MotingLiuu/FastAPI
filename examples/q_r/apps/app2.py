from fastapi import APIRouter
from typing import Optional
app2 = APIRouter()

@app2.get("/jobs")
async def get_jobs(gj: Optional[int] = None):
    print("id:", 1)
    return {
        "user": 12345,
        "gj": 5
        }