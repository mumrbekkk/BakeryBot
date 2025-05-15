from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.keyboard_states import ReplyKeyboardState
from utils.keyboards.reply_kb import item_admin_kb


async def msg_item__(message: Message, state: FSMContext):
    await message.answer("Mahsulot Bo'limi", reply_markup=item_admin_kb)

    await state.set_state(ReplyKeyboardState.item_state)

