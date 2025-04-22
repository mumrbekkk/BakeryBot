from aiogram.fsm.state import StatesGroup, State


class UpdateItemState(StatesGroup):
    update_state = State()
    update_field_state = State()
    update_confirm_state = State()




