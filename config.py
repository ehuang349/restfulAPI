from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv


class Settings(BaseSettings):
    environment: str = "dev"
    debug: bool = True

    class Config:
        env_file = ".env"


def load_environment():
    environment = os.getenv("ENVIRONMENT", "dev")
    env_file = "dev.env" if environment == "dev" else "prod.env"
    load_dotenv(env_file)
    setting = Settings()
    return setting


settings = load_environment()
