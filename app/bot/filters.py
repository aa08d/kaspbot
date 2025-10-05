from typing import Literal

from aiogram.filters.callback_data import CallbackData


class HomePage(CallbackData, prefix="home"):
    category: Literal["consumption", "document", "support"]


class ConsumptionPage(CallbackData, prefix="consumption"):
    action: Literal["add"]


class DocumentPage(CallbackData, prefix="document"):
    action: Literal["last", "date"]
