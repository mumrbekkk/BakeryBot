from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter

from states.keyboard_states import ReplyKeyboardState
from states.inline_kb_states import InlineKeyboardState
from utils.keyboards import inline_kb
from database.requests import get_category_by_id, update_category_field


router = Router()


@router.callback_query(
    StateFilter(InlineKeyboardState.category_detail_state,
                InlineKeyboardState.update_category_field_state),
    F.data.startswith("update_category")
)
async def callback_edit_category(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    category_id = data["category_id"]
    category = await get_category_by_id(category_id)

    await callback.message.edit_text(
        text="Kategoriyani tahrirlash",
        reply_markup=await inline_kb.edit_category_kb(category)
    )

    await state.set_state(InlineKeyboardState.update_category_state)


@router.callback_query(InlineKeyboardState.update_category_state, F.data.startswith("update_category_"))
async def callback_update_category_field(callback: CallbackQuery, state: FSMContext):
    split = callback.data.split("_")
    field_to_update = split[2]
    await state.update_data(field_to_update=field_to_update)

    field_to_update_uz = "ma'umotini"
    if field_to_update == "name":
        field_to_update_uz = "nomini"
    elif field_to_update == "description":
        field_to_update_uz = "tasnifini"

    data = await state.get_data()
    category_id = data["category_id"]

    await callback.message.edit_text(
        text=f"Kategoriya {field_to_update_uz} yanggi qiymatni kiriting",
        reply_markup=await inline_kb.update_category_field_kb(category_id)
    )

    await state.set_state(InlineKeyboardState.update_category_field_state)


@router.message(InlineKeyboardState.update_category_field_state)
async def update_category_field_confirmation(message: Message, state: FSMContext):
    new_value = message.text
    await state.update_data(new_value=new_value)
    await message.reply(
        text=f"Yanggi qiymat: {new_value}. Tasdiqlaysizmi?",
        reply_markup=await inline_kb.confirmation_kb("cancel")
    )

    await state.set_state(InlineKeyboardState.update_category_field_confirmation_state)


@router.callback_query(InlineKeyboardState.update_category_field_confirmation_state)
async def callback_update_category_field_confirmation(callback: CallbackQuery, state: FSMContext):
    query = callback.data
    data = await state.get_data()
    category_id = data["category_id"]
    field_to_update = data["field_to_update"]
    new_value = data["new_value"]

    if query == "cancel":
        await callback.message.edit_text("[Bekor qilindi]")
    elif query == "confirm":
        message = await update_category_field(category_id, field_to_update, new_value)
        await callback.message.edit_text(message)

    await state.set_data({})
    await state.set_state(ReplyKeyboardState.category_state)




