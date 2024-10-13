import os

from pydantic import BaseModel


class DatabaseConfig(BaseModel):
    MONGO_URL: str = os.getenv("DATABASE_MONGO_URL")
    MONGO_MIN_POOL_SIZE: int = int(os.getenv("DATABASE_POSTGRES_MIN_POOL_SIZE", 10))
    MONGO_MAX_POOL_SIZE: int = int(os.getenv("DATABASE_POSTGRES_MAX_POOL_SIZE", 100))
    MONGO_TIMEOUT: int = int(os.getenv("DATABASE_MONGO_TIMEOUT", 20000))
