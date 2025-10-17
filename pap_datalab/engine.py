import os
from dotenv import load_dotenv
from clickhouse_connect import get_client

from sqlalchemy import create_engine, MetaData


load_dotenv()

client_password: str = os.getenv("clickhouse_password") or ""
client_username: str = os.getenv("clickhouse_username") or ""
client_host: str = os.getenv("clickhouse_host") or ""


uri = (
    "clickhouse+http://"
    f"{client_username}:{client_password}"
    f"@{client_host}"
    ":443"
    "/depdev"
    "?protocol=https"
)


# Connect to ClickHouse
client = get_client(
    host="clickhouse-dev.hawitsu.xyz",
    port=443,
    username=client_username,
    password=client_password,
    database="depdev",
    compression=True,
)

engine = create_engine(uri, connect_args={"timezone": "Asia/Manila"})
metadata = MetaData()
