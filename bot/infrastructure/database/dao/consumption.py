from uuid import UUID
from datetime import date

from sqlalchemy import select, extract
from sqlalchemy.ext.asyncio import AsyncSession

from bot.infrastructure.database.models import Consumption


class ConsumptionDAO:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_consumption_by_id(self, user_id: UUID) -> Consumption | None:
        stmt = select(Consumption).filter(Consumption.user_id == user_id)
        result = await self.session.execute(stmt)
        consumption = result.scalar_one_or_none()
        return consumption

    async def get_users_consumption_by_period(self, user_id: UUID, month: int, year: int) -> Consumption:
        stmt = select(Consumption).filter(
            Consumption.user_id == user_id,
            extract("month", Consumption.date) == month,
            extract("year", Consumption.date) == year,
        )

    async def create(
            self,
            previous: float,
            current: float,
            photo_url: str,
            user_id: UUID,
    ) -> Consumption:
        consumption = Consumption(
            previous=previous,
            current=current,
            photo_url=photo_url,
            user_id=user_id,
            date=date.today(),
        )
        self.session.add(consumption)
        await self.session.commit()
        return consumption
