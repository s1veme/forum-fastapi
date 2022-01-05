from typing import List

from fastapi import APIRouter, Depends

from models.user import User, UserCreate, UserRead
from repositories.users import UserRepository
from .depends import get_user_repository

router = APIRouter()


@router.get('/', response_model=List[UserRead])
async def read_users(users: UserRepository = Depends(get_user_repository), limit: int = 100, skip: int = 0):
    return await users.get_all(limit=limit, skip=skip)


@router.post('/create', response_model=UserRead)
async def create_user(user: UserCreate, users: UserRepository = Depends(get_user_repository)):
    return await users.create(user)


@router.patch('/update', response_model=UserRead)
async def update_user(id: int, user: UserCreate, users: UserRepository = Depends(get_user_repository)):
    return await users.update(id, user)
