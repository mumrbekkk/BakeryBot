from . import Router, F

from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from database.requests import get_item_by_id, delete_item_by_id
from utils.keyboards import inline_kb
from states.inline_kb_states import InlineKeyboardState
from states.delete_item_states import DeleteItemState
from handlers.handler_utils.message_bodies.msg_all_items_util import all_items__

router = Router()


@router.callback_query(StateFilter(InlineKeyboardState.item_details_state),
                       F.data.startswith("delete_"))
async def delete_confirmation(callback: CallbackQuery, state: FSMContext):
    item_id = int(callback.data.split("_")[1])
    item = await get_item_by_id(item_id)

    await callback.answer("Siz mahsulotni o'chirmoqchisiz!", show_alert=True)
    await callback.message.edit_text(text=f"'{item.name}' mahsulotini o'chirmoqchimisiz?",
                                     reply_markup=await inline_kb.delete_confirmation_kb(item_id))

    await state.set_state(DeleteItemState.confirm_deletion_state)


@router.callback_query(DeleteItemState.confirm_deletion_state, F.data.startswith("confirm_delete_"))
async def delete_item(callback: CallbackQuery, state: FSMContext):
    item_id = int(callback.data.split("_")[2])
    item = await get_item_by_id(item_id)
    # TODO Add exception handling
    await delete_item_by_id(item_id)
    await callback.answer("✅ Masulot o'chirildi")
    await callback.message.edit_text(text=f"'{item.name}' o'chirildi ✅", reply_markup=await inline_kb.back_to_list_kb())


@router.callback_query(DeleteItemState.confirm_deletion_state, F.data == "back_to_list")
async def back_to_list(callback: CallbackQuery, state: FSMContext):
    await all_items__(callback, state)


