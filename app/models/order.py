from uuid import UUID
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class OrderCreateRequest:
    code: str


@dataclass(frozen=True)
class OrderCreateResponse:
    id: UUID
    date: date
    user_id: UUID
