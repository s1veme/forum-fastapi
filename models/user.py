import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    username: str
    status: str = None
    avatar: str = None
    _hashed_password: str
    _is_staff: bool = False
    _is_active: bool = True
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        underscore_attrs_are_private = True


class UserIn(BaseModel):
    email: str
    username: str
    password: constr(min_length=8)
    status: str = None
    avatar: str = None
