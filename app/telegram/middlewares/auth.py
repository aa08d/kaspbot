from typing import Callable, Awaitable, Dict, Any
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from aiogram.fsm.context import FSMContext

from app.models import GetTelegramRequest
from app.database.crud import get_telegram_account
from app.telegram.keyboards import share_phone_keyboard
from app.telegram.states import RegistrationState



class AuthMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user_id = event.from_user.id
        session = data.get("session")
        state: FSMContext = data.get("state")

        telegram_account = await get_telegram_account(session, GetTelegramRequest(user_id))

        if telegram_account is None:
            await event.answer(
                "Пожалуйста, отправьте своей номер телефона",
                reply_markup=share_phone_keyboard,
            )
            await state.set_state(RegistrationState.ON)

        data["telegram_account"] = telegram_account
        return await handler(event, data)
