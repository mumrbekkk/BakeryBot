from aiogram.fsm.state import StatesGroup, State


class ReplyKeyboardState(StatesGroup):
    home_state = State()

    menu_state = State()
    menu_category_state = State()

    about_state = State()
    instagram_state = State()
    telegram_state = State()
    admin_state = State()
    item_state = State()
    category_state = State()
    category_list_state = State()
    add_category_state = State()

