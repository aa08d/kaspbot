from aiogram.fsm.state import State, StatesGroup


class AddConsumptionState(StatesGroup):
    readings = State()
    photo = State()
