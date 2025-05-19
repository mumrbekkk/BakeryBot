from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from database.all_requests import get_all_items
from utils.keyboards import inline_kb
from states.inline_kb_states import InlineKeyboardState


async def all_items__(msg, state: FSMContext):
    await state.set_state(InlineKeyboardState.all_items_state)
    all_items = await get_all_items()
    items_list_kb = await inline_kb.items_list_kb(all_items)

    if type(msg) is Message:
        await msg.answer(text="🧾 Mahsulotlar Ro'yhati", reply_markup=ReplyKeyboardRemove())
        await msg.answer(text="🧾 Ro'yhat 🧾", reply_markup=items_list_kb)
    elif type(msg) is CallbackQuery:
        await msg.message.edit_text(text="🧾 Ro'yhat 🧾", reply_markup=items_list_kb)

