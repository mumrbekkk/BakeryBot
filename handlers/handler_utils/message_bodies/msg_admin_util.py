from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states.keyboard_states import ReplyKeyboardState
from utils.constants import constants_uz
from utils.keyboards import reply_kb
from helpers.validators import is_admin_or_not


async def msg_admin__(msg, state: FSMContext):
    if CallbackQuery == type(msg):
        if not await is_admin_or_not(msg.from_user.username):
            return

        await msg.message.answer(
            text=constants_uz.ADMIN_WELCOME_MSG,
            reply_markup=await reply_kb.admin_kb()
        )
    elif Message == type(msg):
        if not await is_admin_or_not(msg.from_user.username):
            return
        await msg.answer(
            text=constants_uz.ADMIN_WELCOME_MSG,
            reply_markup=await reply_kb.admin_kb()
        )

    await state.set_state(ReplyKeyboardState.admin_state)

