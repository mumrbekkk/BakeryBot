from aiogram.fsm.state import StatesGroup, State


class ReplyKeyboardState(StatesGroup):
    home_state = State()
    menu_state = State()
    big_cakes_state = State()
    small_cakes_state = State()
    desserts_state = State()

