from aiopg.sa import engine as aiopg_engine

__all__ = (
    'Client',
)


class Client:
    def __init__(self, **config):
        self._engine = None
        self._config = config

    async def connect(self):
        self._engine = await aiopg_engine.create_engine(**self._config)
        return self

    async def close(self, *args, **kwargs):
        self._engine.close()
        await self._engine.wait_closed()

    def acquire(self):
        return self._engine.acquire()

    async def execute(self, query):
        async with self.acquire() as conn:
            await conn.execute(query)

    async def fetchone(self, query):
        async with self.acquire() as conn:
            result = await conn.execute(query)
            obj = await result.fetchone()

        return obj

    async def fetchall(self, query):
        async with self.acquire() as conn:
            result = await conn.execute(query)
            objs = await result.fetchall()

        return objs
