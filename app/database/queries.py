from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User, Consumption, Document, TelegramAccount


@dataclass(frozen=True)
class GetUserByIDQuery:
    user_id: UUID


async def get_user_by_id(query: GetUserByIDQuery, session: AsyncSession) -> User:
    stmt = select(User).filter(User.id == query.user_id)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    return user


@dataclass(frozen=True)
class GetUserIDByTelegramQuery:
    telegram_id: int


async def get_user_by_telegram(
    query: GetUserIDByTelegramQuery,
    session: AsyncSession,
) -> User:
    stmt = select(User).filter(User.telegrams.any(TelegramAccount.telegram_id == query.telegram_id))
    result = await session.execute(stmt)
    user = result.scalars().first()
    return user


@dataclass(frozen=True)
class GetLastUserConsumptionQuery:
    user_id: UUID


async def get_last_user_consumption(
    query: GetLastUserConsumptionQuery,
    session: AsyncSession,
) -> Consumption:
    stmt = select(Consumption).filter(Consumption.user == query.user_id)
    result = await session.execute(stmt)
    consumption = result.scalars().first()
    return consumption


@dataclass(frozen=True)
class GetLastUserDocumentQuery:
    user_id: UUID


async def get_last_user_document(
    query: GetLastUserDocumentQuery,
    session: AsyncSession,
) -> Document:
    stmt = select(Document).filter(Document.user == query.user_id)
    result = await session.execute(stmt)
    document = result.scalars().first()
    return document
