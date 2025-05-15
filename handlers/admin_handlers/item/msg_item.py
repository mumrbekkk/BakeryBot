from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.keyboard_states import ReplyKeyboardState
from utils.constants import constants_uz
from handlers.handler_utils.message_bodies.msg_item_util import msg_item__


router = Router()


@router.message(ReplyKeyboardState.admin_state, F.text == constants_uz.ADMIN_ITEM_MSG_HANDLER_TXT)
async def msg_item(message: Message, state: FSMContext):
    await msg_item__(message, state)






