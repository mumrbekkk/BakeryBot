from aiogram.types import Message, CallbackQuery

from database.requests import get_all_items
from utils.keyboards import inline_kb


async def all_items__(msg):
    all_items = await get_all_items()
    items_list_kb = await inline_kb.items_list_kb(all_items)

    if type(msg) is Message:
        await msg.answer(text="Mahsulotlar", reply_markup=items_list_kb)
    elif type(msg) is CallbackQuery:
        await msg.message.edit_text(text="Mahsulotlar", reply_markup=items_list_kb)

