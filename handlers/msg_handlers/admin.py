from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.keyboard_states import ReplyKeyboardState
from utils.constants import constants_uz
from handlers.handler_utils.message_bodies.msg_admin_util import msg_admin__

router = Router()


@router.message(ReplyKeyboardState.home_state, F.text == constants_uz.ADMIN_MSG_HANDLER_TXT)
async def msg_admin(message: Message, state: FSMContext):
    await msg_admin__(message, state)
