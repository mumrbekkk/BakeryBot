from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from states import keyboard_states
from helpers.methods import is_admin_or_not
from utils.constants import constants_uz
from utils.keyboards import reply_kb


async def cmd_start_message__(message: Message, state: FSMContext):
    await state.set_state(keyboard_states.ReplyKeyboardState.home_state)
    is_admin = await is_admin_or_not(message.from_user.username)

    await message.answer(
        text=constants_uz.START_MSG_REPLY_TXT,
        reply_markup=await reply_kb.start_kb(is_admin=is_admin)
    )


async def cmd_start_callback__(callback: CallbackQuery, state: FSMContext):
    await state.set_state(keyboard_states.ReplyKeyboardState.home_state)
    is_admin = await is_admin_or_not(callback.from_user.username)

    await callback.message.answer(
        text=constants_uz.START_MSG_REPLY_TXT,
        reply_markup=await reply_kb.start_kb(is_admin=is_admin)
    )


