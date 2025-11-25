from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CreateUserRequest:
    first_name: str
    last_name: str
    phone: str
    code: str


@dataclass(frozen=True)
class CreateUserResponse:
    id: UUID
    first_name: str
    last_name: str
    phone: str
    code: str


@dataclass(frozen=True)
class GetUserByPhoneRequest:
    phone: str


@dataclass(frozen=True)
class GetUserByPhoneResponse:
    id: UUID
    first_name: str
    last_name: str
    phone: str
    code: str

