from database import all_requests as requests
from database.models import SweetItem
from states.add_item_states import AddItemState
from states.keyboard_states import ReplyKeyboardState
from handlers.handler_utils.message_bodies.msg_item_util import msg_item__
from utils.keyboards import inline_kb
from helpers.validators import (is_admin_or_not, validate_name, validate_url, validate_price,
                                validate_category)
from handlers.handler_utils.message_bodies.msg_admin_util import msg_admin__

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

router = Router()


@router.message(ReplyKeyboardState.item_state, Command("mahsulot_qoshish"))
async def add_item(message: Message, state: FSMContext):
    username = message.from_user.username
    if not await is_admin_or_not(username):
        return

    await message.reply(
        text="Product qo'shish uchun quyidagi formani to'ldiring...",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="/stop")]
            ],
            resize_keyboard=True
        )
    )
    await message.answer("📝 Mahsulot nomini kiriting:")

    await state.set_state(AddItemState.name)


@router.message(
    StateFilter(
      AddItemState.name,
      AddItemState.description,
      AddItemState.image_url,
      AddItemState.price,
      AddItemState.category
    ),
    Command("stop")
)
async def stop_adding(message: Message, state: FSMContext):
    await message.reply("Qo'shish jarayoni bekor qilindi!")

    await msg_admin__(message, state)


@router.message(AddItemState.name)
async def item_name(message: Message, state: FSMContext):
    if not await validate_name(message.text, message):
        return

    await state.update_data(name=message.text)
    await message.answer("🖊 Mahsulot tavsifini kiriting:")

    await state.set_state(AddItemState.description)


@router.message(AddItemState.description)
async def item_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("🖼 Rasm URL manzilini yuboring:")

    await state.set_state(AddItemState.image_url)


@router.message(AddItemState.image_url)
async def item_image_url(message: Message, state: FSMContext):
    if not await validate_url(message.text, message):
        return

    await state.update_data(image_url=message.text)
    await message.answer("💵 Narxini kiriting (raqam ko'rinishida):")

    await state.set_state(AddItemState.price)


@router.message(AddItemState.price)
async def item_price(message: Message, state: FSMContext):
    price = message.text
    if not await validate_price(price, message):
        return
    await state.update_data(price=int(price))

    categories = await requests.get_all_categories()
    categories_txt = ""
    for category in categories:
        categories_txt += f"{category.id} - {category.name}\n"

    reply_categories = await message.answer(text=categories_txt)
    await message.answer(text="🏷 Kategoriya ID sini kiriting:", reply_to_message_id=reply_categories.message_id)

    await state.set_state(AddItemState.category)


@router.message(AddItemState.category)
async def item_category(message: Message, state: FSMContext):
    category_id = message.text
    if not await validate_category(category_id, message):
        return

    await state.update_data(category=int(message.text))

    data = await state.get_data()
    msg_item_details = await message.answer(text=
                                            f"""
📦 Nomi: {data['name']}
🖊 Tavsifi: {data['description']}
🖼 Rasm: {data['image_url']}
💵 Narxi: {data['price']}
🏷 Kategoriya: {data['category']}
""",
                                            )
    await message.answer(
        text="Ma'lumotlar to'grimi?⤴️",
        reply_markup=await inline_kb.item_addition_kb(),
        reply_to_message_id=msg_item_details.message_id
    )

    await state.set_state(AddItemState.confirm)


@router.callback_query(AddItemState.confirm, F.data == "Yes")
async def item_confirm_yes(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await requests.add_item(
        new_item=SweetItem(
            name=data['name'],
            description=data['description'],
            image_url=data['image_url'],
            price=data['price'],
            category=data['category']
        )
    )

    await callback.message.edit_text(
        text="✅ Mahsulot muvaffaqiyatli qo‘shildi!"
    )
    await callback.answer("✅ Mahsulot muvaffaqiyatli qo‘shildi!")
    await msg_item__(callback.message, state)


@router.callback_query(AddItemState.confirm, F.data == "No")
async def item_confirm_no(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        text="Qo'shish jarayoni bekor qilindi!"
    )
    await callback.answer(
        text="Qo'shish jarayoni bekor qilindi!"
    )
    await msg_item__(callback.message, state)





