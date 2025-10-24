import psycopg2
import os

from dotenv import load_dotenv
from sqlalchemy import URL, Engine, create_engine
from functools import cached_property

load_dotenv()

PG_USER = os.getenv('PG_USER')
PG_PASS = os.getenv('PG_PASS')
PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_PORT')
PG_DB = os.getenv('PG_DB')

class Postgres:
    def __init__(self, user: str = PG_USER, password: str = PG_PASS, host: str = PG_HOST, port: int | str = PG_PORT, db: str = PG_DB):
        self._pg_url = URL.create(
            "postgresql+psycopg2",
            username=user,
            password=password,
            host=host,
            database=db,
            port=port
        )
        
    @cached_property
    def engine(self) -> Engine:
        return create_engine(self._pg_url)
    

if __name__ == '__main__':
    pg = Postgres()
    print(pg._pg_url.render_as_string())