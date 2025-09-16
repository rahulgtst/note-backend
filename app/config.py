from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"   # tell Pydantic to read .env

settings = Settings()
