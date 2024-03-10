import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/", response_class=FileResponse)
async def page0() -> FileResponse:
    return FileResponse(path="app/html/page_0.html", status_code=200)


@app.get("/hello")
async def root() -> dict | list:
    return {"message": "Hello World"}


@app.get("/calculate")
async def calculate(a: int, b: int) -> dict:
    return {"result": a + b}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
