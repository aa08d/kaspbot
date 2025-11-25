from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.telegram.filters.callback_data import ConsumptionCallbackData


consumption_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Добавить показания",
                callback_data=ConsumptionCallbackData(action="add").pack(),
            )
        ]
    ]
)
