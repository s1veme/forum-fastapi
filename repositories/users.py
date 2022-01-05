import datetime
from typing import List, Optional

from core.security import hash_password
from db.users import users
from models.user import User, UserCreate, UserRead
from .base import BaseRepository


class UserRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[UserRead]:
        query = users.select().limit(limit).offset(skip)

        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[UserRead]:
        query = users.select().where(users.c.id == id)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def create(self, user: UserCreate) -> UserRead:
        new_user = User(
            email=user.email,
            username=user.username,
            hashed_password=hash_password(user.password),
            status=user.status,
            avatar=user.avatar,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**new_user.dict(exclude={'id'})}
        query = users.insert().values(**values)
        new_user.id = await self.database.execute(query)
        return new_user

    async def update(self, id: int, user: UserCreate) -> UserRead:
        u = User(
            id=id,
            email=user.email,
            username=user.username,
            hashed_password=hash_password(user.password),
            status=user.status,
            avatar=user.avatar,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**u.dict(exclude={'id', 'created_at'})}

        query = users.update().where(users.c.id == id).values(**values)
        await self.database.execute(query)
        return u

    async def get_by_email(self, email: str) -> Optional[UserRead]:
        query = users.select().where(users.c.email == email)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def get_by_username(self, username: str) -> Optional[UserRead]:
        query = users.select().where(users.c.username == username)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)
