from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter

from states.inline_kb_states import InlineKeyboardState
from utils.constants import constants_uz
from utils.keyboards import inline_kb
from database.all_requests import get_category_by_id


router = Router()


@router.callback_query(
    StateFilter(
        InlineKeyboardState.category_list_state,
        InlineKeyboardState.update_category_state,
        InlineKeyboardState.delete_category_confirmation_state
    ),
    F.data.startswith("category_")
)
async def callback_category_details(callback: CallbackQuery, state: FSMContext):
    category_id = int(callback.data.split("_")[1])
    await state.update_data(category_id=category_id)

    category = await get_category_by_id(category_id)
    await callback.message.edit_text(
        text=f"Kategoriya: <b>{category.name}</b>\n\n"
             f"Tavsifi: {category.description}",
        reply_markup=await inline_kb.category_detail_kb(),
        parse_mode="HTML"
    )

    await state.set_state(InlineKeyboardState.category_detail_state)


@router.callback_query(InlineKeyboardState.category_detail_state, F.data == "back_to_category_list")
async def callback_back_to_category_list(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text=constants_uz.ALL_CATEGORIES_TXT,
        reply_markup=await inline_kb.category_list_kb()
    )

    await state.set_state(InlineKeyboardState.category_list_state)




