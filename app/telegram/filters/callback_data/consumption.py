from aiogram.filters.callback_data import CallbackData


class ConsumptionCallbackData(CallbackData, prefix="consumption"):
    action: str
