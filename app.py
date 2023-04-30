from fastapi import FastAPI
from pydantic import BaseModel, Field

from db import users, trades

app = FastAPI(
    title="Financial App 💴💷💶",
)


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["user_id"] == user_id:
            return user
    return None


@app.get("/trades")
def get_trades(limit: int = 5, offset: int = 0):
    return trades[offset:][:limit]


@app.patch("/users/{user_id}")
def change_username(user_id: int, new_name: str):
    current_user = list(filter(lambda u: u["user_id"] == user_id, users))[0]
    current_user["username"] = new_name

    return {
        "status": 200,
        "data": current_user,
    }


class Trade(BaseModel):
    id: int
    user_id: int
    created_at: str
    currency: str
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post("/trades")
def add_trades(new_trades: list[Trade]):
    trades.extend(new_trades)
    return {
        "status": 200,
        "data": trades,
    }
