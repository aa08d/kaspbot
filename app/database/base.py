from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine, async_sessionmaker

from app.config_loader import load_config

from .config import DBConfig


db_config = load_config(DBConfig, "database")


class Base(DeclarativeBase):
    pass


def create_engine() -> AsyncEngine:
    engine = create_async_engine(url=db_config.full_url)
    return engine


def create_session() -> AsyncSession:
    session = async_sessionmaker(
        bind=create_engine(),
        autoflush=False,
        expire_on_commit=False,
    )
    return session
