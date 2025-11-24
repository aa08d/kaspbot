from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CreateTelegramRequest:
    telegram_id: int
    phone: str


@dataclass(frozen=True)
class CreateTelegramResponse:
    id: UUID
    first_name: str
    last_name: str
    phone: str
    code: str


@dataclass(frozen=True)
class GetTelegramRequest:
    telegram_id: int


@dataclass(frozen=True)
class GetTelegramResponse:
    telegram_id: int
    user_id: UUID
