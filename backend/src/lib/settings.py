from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Task Manager REST API"

    # Auth Values
    JWT_ALGORITHM: str
    JWT_SECRET: str

    # DB Values
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str

    class Config:
        env_file = ".env"