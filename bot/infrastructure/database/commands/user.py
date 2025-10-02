from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession

from bot.infrastructure.database.models import User
from bot.infrastructure.database.dao import UserDAO


@dataclass(frozen=True)
class CreateUserCommand:
    first_name: str
    last_name: str
    phone: str



async def create_user(session: AsyncSession, command: CreateUserCommand) -> User:
    dao = UserDAO(session)
    user = await dao.add_user(
        first_name=command.first_name,
        last_name=command.last_name,
        phone=command.phone,
    )
    return user
