from pydantic import BaseModel, computed_field


class UserSystemFields(BaseModel):
    id: int


class UserCommonFields(BaseModel):
    name: str
    age: int


class User(UserSystemFields, UserCommonFields):
    pass


class UserGet(UserCommonFields):
    @computed_field  # type: ignore
    @property
    def is_adult(self) -> bool:
        return self.age >= 18
