from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import (
    CreateUserRequest,
    CreateUserResponse,
    GetUserByPhoneRequest,
    GetUserByPhoneResponse,
    CreateTelegramRequest,
    CreateTelegramResponse,
    GetTelegramRequest,
    GetTelegramResponse,
    CreateOrderRequest,
    CreateOrderResponse,
    CreateConsumptionRequest,
    CreateConsumptionResponse,
)
from app.database.models import User, TelegramAccount, Order, Consumption


async def create_user(
    session: AsyncSession,
    request: CreateUserRequest,
) -> CreateUserResponse | None:
    user = User(
        first_name=request.first_name,
        last_name=request.last_name,
        phone=request.phone,
        code=request.code,
    )
    session.add(user)
    await session.commit()

    return CreateUserResponse(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        code=user.code,
    )

async def get_user_by_phone(
    session: AsyncSession,
    request: GetUserByPhoneRequest,
) -> GetUserByPhoneResponse | None:
    stmt = select(User).where(User.phone == request.phone)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        return None

    return GetUserByPhoneResponse(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        code=user.code,
    )


async def create_telegram_account(
    session: AsyncSession,
    request: CreateTelegramRequest,
) -> CreateTelegramResponse | None:
    stmt = select(User).where(User.phone == request.phone)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        return None

    telegram = TelegramAccount(telegram_id=request.telegram_id, user_id=user.id)
    session.add(telegram)
    await session.commit()

    return CreateTelegramResponse(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        code=user.code,
    )

async def get_telegram_account(
    session: AsyncSession,
    request: GetTelegramRequest,
) -> GetTelegramResponse | None:
    stmt = select(TelegramAccount).where(TelegramAccount.telegram_id == request.telegram_id)
    result = await session.execute(stmt)
    telegram = result.scalar_one_or_none()

    if telegram is None:
        return None

    return GetTelegramResponse(
        telegram_id=telegram.telegram_id,
        user_id=telegram.user_id,
    )

async def create_order(
    session: AsyncSession,
    request: CreateOrderRequest,
) -> CreateOrderResponse | None:
    stmt = select(User).where(User.code == request.code)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        return None

    order = Order(user_id=user.id)
    session.add(order)
    await session.commit()

    return CreateOrderResponse(
        id=order.id,
        date=order.date,
        user_id=user.id,
    )


async def create_consumption(
    session: AsyncSession,
    request: CreateConsumptionRequest,
) -> CreateConsumptionResponse | None:
    stmt = select(TelegramAccount).where(TelegramAccount.telegram_id == request.telegram_id)
    result = await session.execute(stmt)
    telegram = result.scalar_one_or_none()

    if telegram is None:
        return None

    consumption = Consumption(
        id=request.id,
        readings=request.readings,
        photo_url=request.photo_url,
        user_id=telegram.user_id,
    )
    session.add(consumption)
    await session.commit()

    return CreateConsumptionResponse(
        id=consumption.id,
        readings=consumption.readings,
        photo_url=consumption.photo_url,
        date=consumption.date,
        user_id=consumption.user_id,
    )
