import uvicorn
from fastapi import FastAPI

from app.routes.dummy import router as dummy_router
from app.routes.user import router as user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(dummy_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
