import re

from pydantic import BaseModel, Field, field_validator


class BaseUser(BaseModel):
    phone_number: str = Field(pattern=r"^(\+98|0)?9\d{9}$")
    first_name: str | None = Field(default=None, max_length=127)
    last_name: str | None = Field(default=None, max_length=127)


class UserCreate(BaseUser):
    password: str = Field(min_length=8)


class UserLogin(BaseModel):
    phone_number: str
    password: str

    @field_validator('phone_number')
    @classmethod
    def phone_number_validator(cls, value):
        iran_phone_number_regex = r"^(\+98|0)?9\d{9}$"
        if re.fullmatch(iran_phone_number_regex, value):
            return value
        raise ValueError("Invalid phone number")


class User(BaseUser):
    id: int

    class Config:
        from_attribute = True
