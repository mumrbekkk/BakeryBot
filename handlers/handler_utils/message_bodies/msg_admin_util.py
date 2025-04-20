from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.keyboard_states import ReplyKeyboardState
from utils.constants import constants_uz
from utils.keyboards import reply_kb


async def msg_admin__(message: Message, state: FSMContext):
    await state.set_state(ReplyKeyboardState.admin_state)
    await message.answer(
        text=constants_uz.ADMIN_WELCOME_MSG,
        reply_markup=await reply_kb.admin_kb()
    )

