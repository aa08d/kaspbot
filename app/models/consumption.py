from uuid import UUID
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class ConsumptionCreateRequest:
    telegram_id: int
    readings: int | float
    photo_url: str



@dataclass(frozen=True)
class ConsumptionCreateResponse:
    id: UUID
    readings: int | float
    photo_url: str
    date: date
    user_id: UUID
