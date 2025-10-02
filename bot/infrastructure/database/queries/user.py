from uuid import UUID
from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession

from bot.infrastructure.database.models import User
from bot.infrastructure.database.dao import UserDAO


@dataclass(frozen=True)
class GetUserByID:
    user_id: UUID

async def get_user_by_id(session: AsyncSession, query: GetUserByID) -> User:
    dao = UserDAO(session)
    user = await dao.get_by_id(query.user_id)
    return user


@dataclass(frozen=True)
class GetUserByPhone:
    phone: str

async def get_user_by_phone(session: AsyncSession, query: GetUserByPhone) -> User:
    dao = UserDAO(session)
    user = await dao.get_by_phone(query.phone)
    return user
