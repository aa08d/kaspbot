from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class TelegramCreateRequest:
    telegram_id: int
    phone: str


@dataclass(frozen=True)
class TelegramCreateResponse:
    id: UUID
    first_name: str
    last_name: str
    phone: str
    code: str
