from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states.keyboard_states import ReplyKeyboardState
from states.inline_kb_states import InlineKeyboardState
from utils.constants import constants_uz
from handlers.handler_utils.message_bodies.msg_all_items_util import all_items__
from handlers.handler_utils.message_bodies.msg_item_util import msg_item__


router = Router()


@router.message(ReplyKeyboardState.item_state, F.text == constants_uz.ITEM_LIST_MSG_HANDLER_TXT)
async def msg_all_items(message: Message, state: FSMContext):
    await all_items__(message, state)


@router.callback_query(InlineKeyboardState.all_items_state, F.data == "back_to_item")
async def back_to_admin_panel_callback(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="[O'chirildi]", reply_markup=None)
    await msg_item__(callback.message, state)



