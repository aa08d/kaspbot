from uuid6 import uuid7
from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from sqlalchemy.ext.asyncio import AsyncSession

from app.telegram.filters.callback_data import MenuCallbackData, ConsumptionCallbackData
from app.telegram.keyboards import consumption_keyboard
from app.telegram.states import AddConsumptionState
from app.models import CreateConsumptionRequest
from app.database.crud import create_consumption
from app.s3 import S3Service


router = Router()


async def consumption_category_callback(callback: CallbackQuery) -> None:
    await callback.message.answer("Категория показаний", reply_markup=consumption_keyboard)


async def add_consumption_callback(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer("Введите показания")
    await state.set_state(AddConsumptionState.readings)


@router.message(StateFilter(AddConsumptionState.readings))
async def add_readings_callback(message: Message, state: FSMContext) -> None:
    await state.update_data(readings=message.text)
    await message.answer("Отправьте фото счетчика")
    await state.set_state(AddConsumptionState.photo)


@router.message(StateFilter(AddConsumptionState.photo), F.photo)
async def add_photo_callback(
    message: Message,
    bot: Bot,
    state: FSMContext,
    session: AsyncSession,
    s3: S3Service,
) -> None:
    state_data = await state.get_data()
    file_id = message.photo[-1].file_id
    photo = await bot.download_file(file_id)

    filename = uuid7()

    await s3.upload_file(file=photo, file_name=str(filename))

    await create_consumption(
        session=session,
        request=CreateConsumptionRequest(
            id=filename,
            telegram_id=message.from_user.id,
            readings=state_data.get("readings"),
            photo_url=str(filename),
        )
    )
    await state.clear()
    await message.answer("Показания записаны")
