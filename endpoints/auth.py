from fastapi import APIRouter, Depends, HTTPException, status

from core.security import verify_password, create_access_token
from endpoints.depends import get_user_repository
from repositories.users import UserRepository
from models.token import Token, Login

router = APIRouter()


@router.post('/', response_model=Token)
async def login(login: Login, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(login.email)
    print(user)
    if user is None or not verify_password(login.password, user.get_hashed_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect email or password')

    return Token(
        access_token=create_access_token({'sub': user.email}),
        token_type='Bearer'
    )