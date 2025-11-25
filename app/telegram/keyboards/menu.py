from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.telegram.filters.callback_data import MenuCallbackData


menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Показания",
                callback_data=MenuCallbackData(category="consumption").pack()
            )
        ],
        [InlineKeyboardButton(text="Поддержка", url="https://t.me/clipposter")],
    ]
)
