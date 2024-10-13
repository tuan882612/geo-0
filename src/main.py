import logging

from fastapi import FastAPI
from pydantic import ValidationError

from src.conf.base_conf import get_base_config
from src.server.http_server import HttpServer

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def entry() -> FastAPI:
    try:
        config = get_base_config()
        logging.info("Configuration loaded.")
    except ValidationError as e:
        logging.critical(f"Invalid configuration: {e}", exc_info=True)
        exit(1)

    server = HttpServer(config)
    return server.get_app()
