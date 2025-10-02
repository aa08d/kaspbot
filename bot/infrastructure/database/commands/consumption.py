from uuid import UUID
from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession

from bot.infrastructure.database.models import Consumption
from bot.infrastructure.database.dao import ConsumptionDAO


@dataclass(frozen=True)
class CreateConsumptionCommand:
    previous: float
    current: float
    photo_url: str
    user_id: UUID


async def create_consumption(
    command: CreateConsumptionCommand,
    session: AsyncSession,
) -> Consumption:
    dao = ConsumptionDAO(session)
    consumption = await dao.create(
        previous=command.previous,
        current=command.current,
        photo_url=command.photo_url,
        user_id=command.user_id,
    )
    return consumption
