from fastapi import FastAPI

from db.base import database
from endpoints import users, auth

app = FastAPI(title='forum')
app.include_router(users.router, prefix='/api/users', tags=['users'])
app.include_router(auth.router, prefix='/api/auth', tags=['auth'])


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()
