from fastapi import APIRouter
from fastapi.responses import FileResponse, JSONResponse

router = APIRouter(prefix="")


@router.get("/")
async def get_static_html() -> FileResponse:
    return FileResponse(path="app/static/html/page_0.html")


@router.get("/hello")
async def get_hello() -> dict | list:
    return {"message": "Hello World"}


@router.get("/calculate")
async def get_calculate(a: int, b: int) -> JSONResponse:
    return JSONResponse({"result": a + b})
