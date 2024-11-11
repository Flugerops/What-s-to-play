import asyncio

from uvicorn import run as run_asgi

from backend import app
from backend.db import AsyncDB


async def main():
    await AsyncDB.migrate()
    await AsyncDB.create_mock()


if __name__ == "__main__":
    asyncio.run(main())
    run_asgi("backend:app", port=8134, reload=True)
