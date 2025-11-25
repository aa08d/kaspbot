from uuid import UUID
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class CreateConsumptionRequest:
    id: UUID
    telegram_id: int
    readings: int | float
    photo_url: str



@dataclass(frozen=True)
class CreateConsumptionResponse:
    id: UUID
    readings: int | float
    photo_url: str
    date: date
    user_id: UUID
