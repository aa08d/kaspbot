from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from .config import DBConfig


class Base(DeclarativeBase):
    pass


async def get_session(config: DBConfig) -> AsyncSession:
    engine = create_async_engine(url=config.full_url, echo=config.echo)
    session_factory = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)
    return session_factory()
