from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.keyboard_states import ReplyKeyboardState
from utils.constants import constants_uz
from utils.keyboards import reply_kb

router = Router()


@router.message(ReplyKeyboardState.home_state, F.text == constants_uz.ADMIN_MSG_HANDLER_TXT)
async def msg_admin(message: Message, state: FSMContext):
    await state.set_state(ReplyKeyboardState.admin_state)
    await message.answer(
        text=constants_uz.ADMIN_WELCOME_MSG,
        reply_markup=await reply_kb.admin_kb()
    )
