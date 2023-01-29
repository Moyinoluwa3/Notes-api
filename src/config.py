from typing import Any

from pydantic import BaseSettings, PostgresDsn, RedisDsn, root_validator



class Settings(BaseSettings):
    database_hostname: str
    database_password: str
    database_name: str
    database_username: str
    


    class Config:
        env_file = ".env"



settings = Settings()

