from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.keyboard_states import ReplyKeyboardState
from utils.keyboards import reply_kb
from utils.constants import constants
from utils.constants import constants_uz
from handlers.msg_handlers.methods import is_admin_or_not

from database.requests import set_user

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await set_user(message.from_user.id)
    await state.set_state(ReplyKeyboardState.home_state)
    is_admin = await is_admin_or_not(message.from_user.username)

    await message.answer(
        text=constants_uz.WELCOME_MESSAGE,
        reply_markup=await reply_kb.start_kb(is_admin=is_admin)
    )

    # Rasm
    await message.answer_photo(
        photo=constants.START_PHOTO_URL,
        caption=constants_uz.START_PHOTO_CAPTION
    )
