from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.keyboard_states import ReplyKeyboardState
from utils.constants import constants_uz
from database.requests import get_all_items
from utils.keyboards import inline_kb
from handlers.handler_utils.message_bodies.msg_all_items_util import all_items__

router = Router()


@router.message(ReplyKeyboardState.admin_state, F.text == constants_uz.ADMIN_ITEM_LIST_MSG_HANDLER_TXT)
async def msg_all_items(message: Message, state: FSMContext):
    await all_items__(message)

