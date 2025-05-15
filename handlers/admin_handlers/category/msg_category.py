from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.keyboard_states import ReplyKeyboardState
from utils.constants import constants_uz
from handlers.handler_utils.message_bodies.msg_category_util import msg_category__


router = Router()


@router.message(ReplyKeyboardState.admin_state,
                F.text == constants_uz.ADMIN_CATEGORY_MSG_HANDLER_TXT)
async def msg_category(message: Message, state: FSMContext):
    await msg_category__(state, message=message)






