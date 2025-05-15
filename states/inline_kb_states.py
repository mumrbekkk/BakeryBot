from aiogram.fsm.state import StatesGroup, State


class InlineKeyboardState(StatesGroup):
    all_items_state = State()
    item_details_state = State()

    category_list_state = State()
    category_detail_state = State()
    update_category_state = State()
    update_category_field_state = State()
    update_category_field_confirmation_state = State()
    delete_category_confirmation_state = State()


