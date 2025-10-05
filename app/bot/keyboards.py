from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .filters import HomePage, ConsumptionPage, DocumentPage


home_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Показания", callback_data=HomePage(category="consumption").pack()),
            InlineKeyboardButton(text="Счета", callback_data=HomePage(category="document").pack())
        ],
        [
            InlineKeyboardButton(text="Поддержка", url="t.me/GadVpnSupport")
        ],
    ],
)

consumption_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Добавить показания", callback_data=ConsumptionPage(action="add"))
        ],
    ],
)

document_page = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="За последний месяц", callback_data=DocumentPage(action="last")),
        ],
        [
            InlineKeyboardButton(text="За последний месяц", callback_data=DocumentPage(action="date")),
        ],
    ],
)
