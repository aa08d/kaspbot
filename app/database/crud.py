from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import (
    UserCreateRequest,
    UserCreateResponse,
    TelegramCreateResponse,
    TelegramCreateRequest,
    OrderCreateRequest,
    OrderCreateResponse,
    ConsumptionCreateRequest,
    ConsumptionCreateResponse,
)
from app.database.models import User, TelegramAccount, Order, Consumption


async def create_user(
    session: AsyncSession,
    request: UserCreateRequest
) -> UserCreateResponse:
    user = User(
        first_name=request.first_name,
        last_name=request.last_name,
        phone=request.phone,
        code=request.code,
    )
    session.add(user)
    await session.commit()

    return UserCreateResponse(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        code=user.code,
    )


async def create_telegram_account(
    session: AsyncSession,
    request: TelegramCreateRequest,
) -> TelegramCreateResponse | None:
    stmt = select(User).where(User.phone == request.phone)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        return None

    telegram = TelegramAccount(telegram_id=request.telegram_id, user_id=user.id)
    session.add(telegram)
    await session.commit()

    return TelegramCreateResponse(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        code=user.code,
    )


async def create_order(
    session: AsyncSession,
    request: OrderCreateRequest,
) -> OrderCreateResponse | None:
    stmt = select(User).where(User.code == request.code)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        return None

    order = Order(user_id=user.id)
    session.add(order)
    await session.commit()

    return OrderCreateResponse(
        id=order.id,
        date=order.date,
        user_id=user.id,
    )


async def create_consumption(
    session: AsyncSession,
    request: ConsumptionCreateRequest,
) -> ConsumptionCreateResponse | None:
    stmt = select(TelegramAccount).where(TelegramAccount.telegram_id == request.telegram_id)
    result = await session.execute(stmt)
    telegram = result.scalar_one_or_none()

    if telegram is None:
        return None

    consumption = Consumption(
        readings=request.readings,
        photo_url=request.photo_url,
        user_id=telegram.user_id,
    )
    session.add(consumption)
    await session.commit()

    return ConsumptionCreateResponse(
        id=consumption.id,
        readings=consumption.readings,
        photo_url=consumption.photo_url,
        date=consumption.date,
        user_id=consumption.user_id,
    )
