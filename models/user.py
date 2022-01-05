import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, constr


class BaseUser(BaseModel):
    email: EmailStr
    username: str
    status: str = None
    avatar: str = None


class UserCreate(BaseUser):
    password: constr(min_length=8)


class UserRead(BaseUser):
    id: int
    is_active: bool = True
    created_at: datetime.datetime
    updated_at: datetime.datetime


class User(BaseUser):
    id: Optional[str] = None
    hashed_password: str
    is_staff: bool = False
    is_active: bool = True
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True
