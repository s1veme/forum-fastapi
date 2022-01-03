import datetime
from typing import Optional

from .config import settings

from passlib.context import CryptContext
from jose import jwt

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hash: str) -> bool:
    return pwd_context.verify(password, hash)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({'exp': datetime.datetime.utcnow() + datetime.timedelta(days=settings.ACCESS_TOKEN_EXPIRE_DAYS)})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_access_token(token: str):
    try:
        encoded_jwt = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
    except jwt.JWSError:
        return None
    return encoded_jwt
