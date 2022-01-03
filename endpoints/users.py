from typing import List

from fastapi import APIRouter, Depends

from models.user import User, UserIn
from repositories.users import UserRepository
from .depends import get_user_repository

router = APIRouter()


@router.get('/', response_model=List[User])
async def read_users(users: UserRepository = Depends(get_user_repository), limit: int = 100, skip: int = 0):
    return await users.get_all(limit=limit, skip=skip)


@router.post('/create', response_model=User)
async def create_user(user: UserIn, users: UserRepository = Depends(get_user_repository)):
    return await users.create(user)


@router.patch('/update', response_model=User)
async def update_user(id: int, user: UserIn, users: UserRepository = Depends(get_user_repository)):
    return await users.update(id, user)