from fastapi import APIRouter, HTTPException

from app.models.user import User, UserCommonFields, UserGet

router = APIRouter(prefix="/user")

users_mock_db = {
    1: User(id=1, name="John Doe", age=12),
    2: User(id=2, name="Jane Doe", age=21),
}


@router.get("/{user_id}")
async def get_single_user(user_id: int) -> UserGet:
    if user_id not in users_mock_db:
        raise HTTPException(404)
    user = users_mock_db[user_id]
    return UserGet(**user.model_dump())


@router.post("")
async def new_user(new_user: UserCommonFields) -> User:
    new_user_id = max(users_mock_db) + 1
    new_user = User(**new_user.model_dump(), id=new_user_id)
    users_mock_db[new_user_id] = new_user
    return new_user
