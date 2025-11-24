from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncEngine

from .config import DBConfig


class Base(DeclarativeBase):
    pass


async def build_engine(config: DBConfig) -> AsyncEngine:
    engine = create_async_engine(config.full_url, echo=config.echo)
    return engine


def build_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    session_factory = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    return session_factory
