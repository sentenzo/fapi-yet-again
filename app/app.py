import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()


@app.get("/", response_class=FileResponse)
async def page0() -> FileResponse:
    return FileResponse(path="app/static/html/page_0.html", status_code=200)


@app.get("/hello")
async def root() -> dict | list:
    return {"message": "Hello World"}


@app.get("/calculate", response_class=JSONResponse)
async def calculate(a: int, b: int) -> JSONResponse:
    return JSONResponse({"result": a + b}, status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
