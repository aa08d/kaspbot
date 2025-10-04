from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User, Consumption, Document, TelegramAccount


@dataclass(frozen=True)
class CreateUserCommand:
    first_name: str
    last_name: str | None
    phone: str


async def create_user(command: CreateUserCommand, session: AsyncSession) -> User:
    user = User(
        first_name=command.first_name,
        last_name=command.last_name,
        phone=command.last_name,
    )
    session.add(user)
    await session.commit()
    return user


@dataclass(frozen=True)
class CreateConsumptionCommand:
    readings: float
    photo_url: str
    user_id: UUID


async def create_consumption(command: CreateConsumptionCommand, session: AsyncSession) -> Consumption:
    consumption = Consumption(
        readings=command.readings,
        photo_url=command.photo_url,
        user=command.user_id,
    )
    session.add(consumption)
    await session.commit()
    return consumption


@dataclass(frozen=True)
class CreateDocumentCommand:
    user_id: UUID


async def create_document(command: CreateDocumentCommand, session: AsyncSession) -> Document:
    document = Document(user=command.user_id)
    session.add(document)
    await session.commit()
    return document


@dataclass(frozen=True)
class CreateTelegramAccountCommand:
    telegram_id: int
    phone: str


async def create_telegram_account(
    command: CreateTelegramAccountCommand,
    session: AsyncSession,
) -> TelegramAccount:
    stmt = select(User).filter(User.phone == command.phone)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        raise ValueError(f"User with {command.phone} not exists")

    telegram = TelegramAccount(telegram_id=command.telegram_id, user=user.id)
    session.add(telegram)
    await session.commit()
    return telegram
