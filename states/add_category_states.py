from aiogram.fsm.state import StatesGroup, State


class AddCategoryState(StatesGroup):
    category_name_state = State()
    category_description_state = State()
    add_category_confirm_state = State()



