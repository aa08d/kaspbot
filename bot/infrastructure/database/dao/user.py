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