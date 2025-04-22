from aiogram.fsm.state import StatesGroup, State


class DeleteItemState(StatesGroup):
    confirm_deletion_state = State()



