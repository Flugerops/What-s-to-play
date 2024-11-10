from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker


class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class AsyncDB:
    ENGINE = create_async_engine("sqlite+aiosqlite:///users.db")
    SESSION = async_sessionmaker(bind=ENGINE, expire_on_commit=False)

    @classmethod
    async def up(cls):
        async with cls.ENGINE.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @classmethod
    async def down(cls):
        async with cls.ENGINE.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    @classmethod
    async def migrate(cls):
        await cls.down()
        await cls.up()

    @classmethod
    async def get_session(cls):
        async with cls.SESSION.begin() as session:
            yield session

    @classmethod
    async def create_mock(cls):
        async with cls.SESSION.begin() as session:
            user = User(username="test", email="gfsd", hashed_password="5432534253")
            session.add(user)


from .models import User
