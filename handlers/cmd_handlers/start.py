from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.constants import constants_uz
from handlers.handler_utils.command_bodies.cmd_start_util import cmd_start_message__

from database import all_requests

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await all_requests.set_user(tg_id=message.from_user.id, username=message.from_user.username)

    await message.answer(text=constants_uz.WELCOME_MESSAGE)
    await cmd_start_message__(message, state)

