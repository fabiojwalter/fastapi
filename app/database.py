# database.py
import asyncpg


class Database:
    def __init__(self, host: str, port: str, database: str, user: str, password: str):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            user=self.user,
            password=self.password,
            database=self.database,
            host=self.host,
            port=self.port,
        )

    async def disconnect(self):
        if self.pool is not None:
            await self.pool.close()

    async def execute_query(self, query: str, *args):
        if self.pool is None:
            await self.connect()
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def execute(self, query: str, *args):
        if self.pool is None:
            await self.connect()
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)

    async def transaction(self):
        if self.pool is None:
            await self.connect()
        async with self.pool.acquire() as connection:
            return connection.transaction()
