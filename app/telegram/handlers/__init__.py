from aiogram import Dispatcher

from .start import router as start_router
from .consumption import router as consumption_router



def include_routers(dp: Dispatcher) -> None:
    dp.include_router(start_router)
    dp.include_router(consumption_router)
