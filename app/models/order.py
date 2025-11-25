from uuid import UUID
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class CreateOrderRequest:
    code: str


@dataclass(frozen=True)
class CreateOrderResponse:
    id: UUID
    date: date
    user_id: UUID
