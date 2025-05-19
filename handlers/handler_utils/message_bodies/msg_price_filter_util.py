
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from states.keyboard_states import ReplyKeyboardState
from utils.keyboards import reply_kb


async def msg_price_filter__(message: Message, state: FSMContext):
    await message.answer("Narxga qarab tanlov", reply_markup=await reply_kb.price_filter_kb())

    await state.set_state(ReplyKeyboardState.price_filter_state)

