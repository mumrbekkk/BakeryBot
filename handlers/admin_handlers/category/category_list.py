from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from states.keyboard_states import ReplyKeyboardState
from states.inline_kb_states import InlineKeyboardState
from utils.constants import constants_uz
from utils.keyboards import inline_kb
from handlers.handler_utils.message_bodies.msg_category_util import msg_category__


router = Router()


@router.message(ReplyKeyboardState.category_state, F.text == constants_uz.ALL_CATEGORIES_TXT)
async def msg_category_list(message: Message, state: FSMContext):
    await message.answer(text=constants_uz.ALL_CATEGORIES_TXT, reply_markup=await inline_kb.category_list_kb())

    await state.set_state(InlineKeyboardState.category_list_state)


@router.callback_query(InlineKeyboardState.category_list_state, F.data == "back_to_category")
async def callback_back_to_category(callback: CallbackQuery, state: FSMContext):
    await msg_category__(state, callback=callback)




