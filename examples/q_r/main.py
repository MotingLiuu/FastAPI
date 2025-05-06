from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from apps.app1 import app1
from apps.app2 import app2
from apps.app3 import app3
from apps.app4 import app4
from apps.app5 import app5
from apps.app6 import app6
from apps.app7 import app7
app = FastAPI()

app.mount("/static", StaticFiles(directory="statics"))

app.include_router(app1, prefix="/app1", tags=["1 路径参数"])
app.include_router(app2, prefix="/app2", tags=["2 查询参数"])
app.include_router(app3, prefix="/app3", tags=["请求体"])
app.include_router(app4, prefix="/app4", tags=["表单"])
app.include_router(app5, prefix="/app5", tags=["文件上传"])
app.include_router(app6, prefix="/app6", tags=["Request"])
app.include_router(app7, prefix="/app7", tags=["Response Model"])
if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)
    