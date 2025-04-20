from aiogram.fsm.state import StatesGroup, State


class CommentState(StatesGroup):
    comment = State()
    confirmation = State()


