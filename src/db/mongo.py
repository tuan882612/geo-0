import logging
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient

from src.conf.base_conf import BaseConfig


class MongoClient:
    _client: Optional[AsyncIOMotorClient] = None

    def __new__(cls):
        raise NotImplementedError("This class is not meant to be instantiated")

    @classmethod
    async def connect(cls, cfg: BaseConfig):
        try:
            if not cls._client:
                logging.debug(f"Connecting to MongoDB with URL: {cfg.DATABASE.MONGO_URL}")
                cls._client = AsyncIOMotorClient(
                    cfg.DATABASE.MONGO_URL,
                    maxPoolSize=cfg.DATABASE.MONGO_MAX_POOL_SIZE,
                    minPoolSize=cfg.DATABASE.MONGO_MIN_POOL_SIZE,
                    serverSelectionTimeoutMS=cfg.DATABASE.MONGO_TIMEOUT,
                )
                db_name = "geo-0"
                db = cls._client.get_database(db_name)
                await db.command("ping")
                logging.info("Connected to MongoDB")
        except Exception as e:
            logging.error(f"Could not connect to MongoDB: {e}")
            raise e

    @classmethod
    def close(cls):
        if cls._client:
            cls._client.close()
            cls._client = None
            logging.info("Closed connection to MongoDB")

    @classmethod
    def get_database(cls, db_name: str):
        if not cls._client:
            raise Exception("MongoClient is not connected")
        return cls._client[db_name]


async def get_database():
    return MongoClient.get_database("geo-0")
