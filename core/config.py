from pydantic import BaseSettings


class Settings(BaseSettings):
    """ project configuration """

    DATABASE_URL: str
    ACCESS_TOKEN_EXPIRE_DAYS: int
    ALGORITHM: str
    SECRET_KEY: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
