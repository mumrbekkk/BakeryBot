from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery


from states.keyboard_states import ReplyKeyboardState
from states.inline_kb_states import InlineKeyboardState
from utils.keyboards import inline_kb
from database.all_requests import delete_category_by_id


router = Router()


@router.callback_query(InlineKeyboardState.category_detail_state, F.data == "delete_category")
async def callback_delete_category(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    category_id = data["category_id"]
    await callback.message.edit_text(
        text="O'chirishni tasdiqlang",
        reply_markup=await inline_kb.confirmation_kb(back_callback=f"category_{category_id}")
    )

    await state.set_state(InlineKeyboardState.delete_category_confirmation_state)


@router.callback_query(InlineKeyboardState.delete_category_confirmation_state)
async def callback_delete_category_confirmation(callback: CallbackQuery, state: FSMContext):
    query = callback.data
    data = await state.get_data()
    category_id = data["category_id"]

    if query == "confirm":
        status = await delete_category_by_id(category_id)
        await callback.message.edit_text(status)
    # elif query == "cancel_deletion":
    #     await callback.message.edit_text("[Bekor qilindi]")

        await state.set_data({})
        await state.set_state(ReplyKeyboardState.category_state)


