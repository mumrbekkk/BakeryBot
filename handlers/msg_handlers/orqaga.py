from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.keyboard_states import ReplyKeyboardState
from utils.keyboards import reply_kb
from utils.constants import constants_uz

router = Router()


@router.message(F.text == constants_uz.BACK_MSG_HANDLER_TXT)
async def msg_back(message: Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == ReplyKeyboardState.menu_state.state:
        await state.set_state(ReplyKeyboardState.home_state)
        await message.answer(
            # TODO Continue
            text=constants_uz.START_MSG_REPLY_TXT,
            reply_markup=reply_kb.start_keyboard
        )
    elif current_state == ReplyKeyboardState.big_cakes_state.state:
        await state.set_state(ReplyKeyboardState.menu_state)
        await message.answer(
            text=constants_uz.MENU_MSG_REPLY_TXT,
            reply_markup=await reply_kb.categories_kb()
        )
    elif current_state == ReplyKeyboardState.small_cakes_state.state:
        await state.set_state(ReplyKeyboardState.menu_state)
        await message.answer(
            text=constants_uz.MENU_MSG_REPLY_TXT,
            reply_markup=await reply_kb.categories_kb()
        )
    elif current_state == ReplyKeyboardState.desserts_state.state:
        await state.set_state(ReplyKeyboardState.menu_state)
        await message.answer(
            text=constants_uz.MENU_MSG_REPLY_TXT,
            reply_markup=await reply_kb.categories_kb()
        )
