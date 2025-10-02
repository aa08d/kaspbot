from uuid import UUID
from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession

from bot.infrastructure.database.models import Consumption
from bot.infrastructure.database.dao import ConsumptionDAO


@dataclass(frozen=True)
class GetConsumptionByIDQuery:
    user_id: UUID

async def get_consumption_by_id(
    command: GetConsumptionByIDQuery,
    session: AsyncSession,
) -> Consumption:
    dao = ConsumptionDAO(session)
    consumption = await dao.get_consumption_by_id(command.user_id)
    return consumption


@dataclass(frozen=True)
class GetConsumptionByPeriodQuery:
    user_id: UUID
    month: int
    year: int

async def get_consumption_by_period(
    command: GetConsumptionByPeriodQuery,
    session: AsyncSession,
) -> Consumption:
    dao = ConsumptionDAO(session)
    consumption = await dao.get_users_consumption_by_period(
        user_id=command.user_id,
        month=command.month,
        year=command.year,
    )
    return consumption
