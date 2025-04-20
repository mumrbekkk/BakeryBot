from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.keyboard_states import ReplyKeyboardState
from utils.keyboards import reply_kb
from utils.constants import constants_uz


async def msg_menu__(message: Message, state: FSMContext):
    await state.set_state(ReplyKeyboardState.menu_state)
    await message.answer(
        text=constants_uz.MENU_MSG_REPLY_TXT,
        reply_markup=await reply_kb.categories_kb()
    )