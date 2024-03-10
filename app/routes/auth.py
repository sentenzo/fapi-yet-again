from fastapi import APIRouter, Cookie, HTTPException, Response
from fastapi.responses import JSONResponse

from app.models.auth import Auth

router = APIRouter(prefix="")


def validate_session_token(session_token: str) -> bool:
    return "correct_token" in session_token  # dummy


def check_password(username: str, password: str) -> bool:
    return True  # dummy


def generate_session_token(username: str, password: str) -> str:
    return f"{username}_correct_token_{username}"


@router.post("/login")
async def login(auth: Auth, response: Response) -> dict:
    if check_password(**auth.model_dump()):
        response.set_cookie(
            key="session_token",
            value=generate_session_token(**auth.model_dump()),
            secure=True,
        )
        return {"response": "ok"}
    raise HTTPException(status_code=403)


@router.get("/logout")
async def logout(response: Response) -> dict:
    response.delete_cookie("session_token")
    return {"response": "ok"}


@router.get("/am_i_authorized")
async def am_i_authorized(
    session_token: str | None = Cookie(None),
) -> JSONResponse:
    # print(request.cookies)
    if session_token and validate_session_token(session_token):
        return JSONResponse({"response": "yes"})
    return JSONResponse({"response": "no"})
