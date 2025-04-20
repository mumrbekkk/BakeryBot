from . import Router, FSMContext, F

from aiogram.types import CallbackQuery

from database.requests import get_item_by_id
from utils.keyboards import inline_kb
from handlers.handler_utils.message_bodies.msg_all_items_util import all_items__

router = Router()


@router.callback_query(F.data.startswith("item_"))
async def item_details(callback: CallbackQuery):
    item_id = int(callback.data.split("_")[1])
    item = await get_item_by_id(item_id)

    details = f"📦 Nomi: {item.name}\n" \
              f"🖊 Tavsifi: {item.description}\n" \
              f"🖼 Rasm: {item.image_url}\n" \
              f"💵 Narxi: {item.price}\n" \
              f"🏷 Kategoriya: {item.category}"
    kb = await inline_kb.item_detail_kb(item_id)

    await callback.answer("Mahsulot Haqida")
    await callback.message.edit_text(text=details, reply_markup=kb)


@router.callback_query(F.data == "back_to_list")
async def back_to_list(callback: CallbackQuery):
    await callback.answer("Mahsulotlar Ro'yhati")
    await all_items__(callback)



