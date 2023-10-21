from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

engine = create_async_engine(
    'sqlite+aiosqlite:///base.db',
    future=True
)


async def create_base():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def get_session():
    try:
        async with sessionmaker(bind=engine, class_=AsyncSession)() as session:
            yield session
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
