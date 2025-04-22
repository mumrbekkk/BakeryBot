from aiogram.fsm.state import StatesGroup, State


class InlineKeyboardState(StatesGroup):
    all_items_state = State()
    item_details_state = State()


