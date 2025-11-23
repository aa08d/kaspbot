from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class UserCreateRequest:
    first_name: str
    last_name: str
    phone: str
    code: str


@dataclass(frozen=True)
class UserCreateResponse:
    id: UUID
    first_name: str
    last_name: str
    phone: str
    code: str
