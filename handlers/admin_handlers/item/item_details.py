from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from database.requests import get_item_by_id
from utils.keyboards import inline_kb
from handlers.handler_utils.message_bodies.msg_all_items_util import all_items__
from states.inline_kb_states import InlineKeyboardState
from states.update_item_states import UpdateItemState
from states.delete_item_states import DeleteItemState
from helpers.methods import price_to_string

router = Router()


@router.callback_query(StateFilter(InlineKeyboardState.all_items_state,
                                   UpdateItemState.update_state,
                                   DeleteItemState.confirm_deletion_state),
                       F.data.startswith("item_"))
async def item_details(callback: CallbackQuery, state: FSMContext):
    await state.set_state(InlineKeyboardState.item_details_state)
    item_id = int(callback.data.split("_")[1])
    item = await get_item_by_id(item_id)
    price = await price_to_string(item.price)

    details = f"📦 Nomi: {item.name}\n" \
              f"🖊 Tavsifi: {item.description}\n" \
              f"🖼 Rasm: {item.image_url}\n" \
              f"💵 Narxi: {price} so'm\n" \
              f"🏷 Kategoriya: {item.item_category.name} [id: {item.category}]"
    kb = await inline_kb.item_detail_kb(item_id)

    await callback.answer("Mahsulot Haqida")
    await callback.message.edit_text(text=details, reply_markup=kb)


@router.callback_query(InlineKeyboardState.item_details_state, F.data == "back_to_list")
async def back_to_list(callback: CallbackQuery, state: FSMContext):
    await all_items__(callback, state)




