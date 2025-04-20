from aiogram.fsm.state import StatesGroup, State


class ReplyKeyboardState(StatesGroup):
    home_state = State()
    menu_state = State()
    big_cakes_state = State()
    small_cakes_state = State()
    desserts_state = State()
    about_state = State()
    instagram_state = State()
    telegram_state = State()
    admin_state = State()
