from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from states.keyboard_states import ReplyKeyboardState
from utils.keyboards import reply_kb
from database.requests import get_item_by_name
from helpers.methods import price_to_string


router = Router()


@router.message(ReplyKeyboardState.menu_state)
async def msg_category(message: Message, state: FSMContext):
    category_name = message.text
    await message.answer(text=f"{category_name} kategoriya mahsulotlari",
                         reply_markup=await reply_kb.category_kb(category_name))

    await state.set_state(ReplyKeyboardState.menu_category_state)


@router.message(ReplyKeyboardState.menu_category_state)
async def msg_category_detail(message: Message):
    item_name = message.text
    item = await get_item_by_name(item_name)
    price = await price_to_string(item.price)

    await message.answer(
        text=f"<b>{item.name.capitalize()}</b>\n\n"
             f"{item.description}\n"
             f"💵 Narxi: {price}\n\n"
             f"{item.image_url}",
        parse_mode="HTML"
    )









