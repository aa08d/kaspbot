from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from sqlalchemy.ext.asyncio import AsyncSession

from app.telegram.states import RegistrationState
from app.models import CreateTelegramRequest
from app.database.crud import create_telegram_account
from app.telegram.keyboards import menu_keyboard



router = Router()


@router.message(F.contact, StateFilter(RegistrationState.ON))
async def contact_message(message: Message, session: AsyncSession, state: FSMContext) -> None:
    user = await create_telegram_account(
        session,
        CreateTelegramRequest(telegram_id=message.from_user.id, phone=message.contact.phone_number)
    )

    if user is None:
        await message.answer("Вы не являетесь нашим клиентом.")
        return

    await message.answer("Вы успешно авторизовались!", reply_markup=ReplyKeyboardRemove())
    await message.answer("Выберите действие", reply_markup=menu_keyboard)
    await state.clear()
