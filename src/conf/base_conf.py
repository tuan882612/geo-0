from functools import lru_cache

from pydantic_settings import BaseSettings

from src.conf.db_conf import DatabaseConfig
from src.conf.server_conf import ServerConfig


class BaseConfig(BaseSettings):
    SERVER: ServerConfig = ServerConfig()
    DATABASE: DatabaseConfig = DatabaseConfig()


@lru_cache()
def get_base_config() -> BaseConfig:
    return BaseConfig()
