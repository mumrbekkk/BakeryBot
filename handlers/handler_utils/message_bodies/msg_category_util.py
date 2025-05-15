from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from utils.keyboards import reply_kb
from states.keyboard_states import ReplyKeyboardState


async def msg_category__(state: FSMContext, message: Message = None, callback: CallbackQuery = None):
    if message:
        await message.answer(text="Kategoriya bo'limi!", reply_markup=await reply_kb.category_admin_kb())
    else:
        await callback.message.edit_text(text="Kategoriya bo'limi!")

    await state.set_state(ReplyKeyboardState.category_state)

