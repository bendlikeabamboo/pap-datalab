import os
from dotenv import load_dotenv
from clickhouse_connect import get_client
from clickhouse_connect.driver.client import Client
from typing import Tuple

from sqlalchemy import create_engine, Engine


class PapDatalab:

    def __init__(self, environment: str, environment_path: str | None = None):
        if environment_path:
            load_dotenv(dotenv_path=f"{environment_path}")
        else:
            load_dotenv(dotenv_path=f"{environment}.env")

    def _db_from_env(
        self,
        username: str | None = None,
        password: str | None = None,
        host: str | None = None,
        port: int | None = None,
    ) -> Tuple[str, str, str, int]:
        client_password: str = password or os.environ["clickhouse_password"]
        client_username: str = username or os.environ["clickhouse_username"]
        client_host: str = host or os.environ["clickhouse_host"]
        client_port: int = port or int(os.environ["clickhouse_port"])

        return (client_host, client_username, client_password, client_port)

    def get_client(
        self,
        database: str,
        username: str | None = None,
        password: str | None = None,
        host: str | None = None,
        port: int | None = None,
    ) -> Client:
        client_host, client_username, client_password, client_port = self._db_from_env(
            username=username, password=password, host=host, port=port
        )
        client = get_client(
            host=client_host,
            port=client_port,
            username=client_username,
            password=client_password,
            database=database,
            compression=True,
        )
        return client

    def get_engine(
        self,
        database: str,
        username: str | None = None,
        password: str | None = None,
        host: str | None = None,
        port: int | None = None,
    ) -> Engine:

        client_host, client_username, client_password, client_port = self._db_from_env(
            username=username, password=password, host=host, port=port
        )
        uri = (
            "clickhouse+http://"
            f"{client_username}:{client_password}"
            f"@{client_host}"
            f":{client_port}"
            f"/{database}"
            "?protocol=https"
        )
        engine = create_engine(uri, connect_args={"timezone": "Asia/Manila"})
        return engine
