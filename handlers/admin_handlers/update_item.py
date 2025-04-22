from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from database.requests import get_item_by_id
from utils.keyboards import inline_kb
from states.update_item_states import UpdateItemState
from states.inline_kb_states import InlineKeyboardState
from helpers.validators import validate_updating_field
from database.requests import update_item_field


router = Router()


@router.callback_query(StateFilter(InlineKeyboardState.item_details_state, UpdateItemState.update_field_state))
async def update_item_callback(callback: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    data = await state.get_data()

    if current_state == InlineKeyboardState.item_details_state.state:
        item_id = int(callback.data.split("_")[1])
        await state.update_data(item_id=item_id)
        item = await get_item_by_id(item_id)
    else:
        item = await get_item_by_id(data['item_id'])

    await callback.message.edit_text(text=f"<<{item.name}>> mahsuloti ma'lumotlarini o'zgartirish ",
                                     reply_markup=await inline_kb.update_item_kb(item))
    await state.set_state(UpdateItemState.update_state)


@router.callback_query(StateFilter(UpdateItemState.update_state, UpdateItemState.update_confirm_state),
                       F.data.startswith("sweetitem_"))
async def update_field_callback(callback: CallbackQuery, state: FSMContext):
    await state.set_state(UpdateItemState.update_field_state)
    data = await state.get_data()
    item_id = data['item_id']
    field_name = callback.data.split("_")[1]
    field_to_update: str
    if field_name == "nomi":
        field_to_update = "name"
    elif field_name == "tavsifi":
        field_to_update = "description"
    elif field_name == "rasmi":
        field_to_update = "image_url"
    elif field_name == "narxi":
        field_to_update = "price"
    elif field_name == "kategoriyasi":
        field_to_update = "category"
    else:
        await callback.message.answer(text="Something went wrong...")
        return

    await state.update_data(field_to_update_uz=field_name, field_to_update=field_to_update)

    await callback.message.edit_text(
        text=f"Mahsulot tafsilotini ({field_name}) yanggi qiymatini kiriting",
        reply_markup=await inline_kb.update_item_field_kb(item_id)
    )


@router.message(UpdateItemState.update_field_state)
async def confirm_update_item_field(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(new_value=message.text, callback_=f"sweetitem_{data['field_to_update_uz']}")
    data = await state.get_data()

    field_to_update = data['field_to_update']
    new_value = data['new_value']

    if not await validate_updating_field(field_to_update, new_value, message):
        return

    await message.answer(text=f"Mahsulot yanggi {data['field_to_update_uz']}: {data['new_value']}. Tasdiqlaysizmi?",
                         reply_markup=await inline_kb.update_item_field_confirmation_kb(data['callback_']))

    await state.set_state(UpdateItemState.update_confirm_state)


@router.callback_query(UpdateItemState.update_confirm_state, F.data == "update_confirm")
async def yes_(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    item_id = data['item_id']
    field_to_update = data['field_to_update']
    new_value = data['new_value']

    success = await update_item_field(item_id, field_to_update, new_value)

    if success:
        await callback.answer(text="✅ Muoffaqiyatli o'zgartildi!", show_alert=True)
        await callback.message.edit_text(
            text="✅ Tahrirlash jarayoni muoffaqiyatli yakunlandi!",
            reply_markup=await inline_kb.update_item_field_kb(item_id)
        )
    else:
        await callback.answer(text="❌ Hatolik yuz berdi!", show_alert=True)
        await callback.message.edit_text(
            text="❌ Tahrirlash jarayonida hatolik yuz berdi!",
            reply_markup=await inline_kb.update_item_field_kb(item_id)
        )

    await state.set_state(UpdateItemState.update_field_state)



















