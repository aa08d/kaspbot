from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot.infrastructure.database.models import User


class UserDAO:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, user_id: UUID) -> User | None:
        stmt = select(User).filter(User.id == user_id)
        result = await self.session.execute(stmt)
        user = result.scalars().one_or_none()
        return user

    async def get_by_phone(self, phone: str) -> User | None:
        stmt = select(User).filter(User.phone == phone)
        result = await self.session.execute(stmt)
        user = result.scalars().one_or_none()
        return user

    async def get_by_telegram_id(self, telegram_id: int) -> User | None:
        stmt = select(User).filter(User.telegram_id == telegram_id)
        result = await self.session.execute(stmt)
        user = result.scalars().one_or_none()
        return user

    async def add_user(
        self,
        first_name: str,
        last_name: str,
        phone: str,
        telegram_id: int,
    ) -> None:
        user = User(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            telegram_id=telegram_id,
        )
        self.session.add(user)
        await self.session.commit()
