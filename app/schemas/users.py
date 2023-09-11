from pydantic import BaseModel, Field, EmailStr


class BaseUser(BaseModel):
    username: str
    email: EmailStr | None = Field(default=None)
    first_name: str | None = Field(default=None, max_length=127)
    last_name: str | None = Field(default=None, max_length=127)


class UserInDB(BaseUser):
    password: str = Field(min_length=8)


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True
