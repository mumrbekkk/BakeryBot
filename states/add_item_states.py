from aiogram.fsm.state import StatesGroup, State


class AddItemState(StatesGroup):
    name = State()
    description = State()
    image_url = State()
    price = State()
    category = State()
    confirm = State()

