from fastapi import APIRouter
from fastapi import Form, File, UploadFile
import os

app5 = APIRouter()

@app5.post("/file")
async def get_file(file: bytes = File()):
    print(file, type(file))
    return {
        "file": "file"
    }
    
@app5.post("/uploadFile")
async def get_file(file: UploadFile = File()):
    print("file", file)
    os.makedirs("imgs", exist_ok=True)
    path = os.path.join("imgs", file.filename)
    with open(path, "wb") as f:
        for line in file.file:
            f.write(line)
    return {
        "file": file.filename
    }        