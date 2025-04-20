from database import requests
from database.models import SweetItem
from states.add_item_states import AddItemState
from handlers.handler_utils.command_bodies.cmd_start_util import cmd_start_callback__
from utils.keyboards import inline_kb
from helpers.methods import validate_url

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

router = Router()


@router.message(Command("mahsulot_qoshish"))
async def add_item(message: Message, state: FSMContext):
    username = message.from_user.username
    if username != "m_umrbekkk" and username != "NargizaRahmatullayeva":
        return

    await state.set_state(AddItemState.name)
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


@router.message(AddItemState.name)
async def item_name(message: Message, state: FSMContext):
    existing_item = await requests.get_item_by_name(message.text)
    if existing_item:
        await message.answer("Bu mahsulot mavjud! Boshqa ism kiriting!")
        return

    await state.update_data(name=message.text)
    await state.set_state(AddItemState.description)
    await message.answer("🖊 Mahsulot tavsifini kiriting:")


@router.message(AddItemState.description)
async def item_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(AddItemState.image_url)
    await message.answer("🖼 Rasm URL manzilini yuboring:")


@router.message(AddItemState.image_url)
async def item_image_url(message: Message, state: FSMContext):
    correct_url = await validate_url(message.text)
    if not correct_url:
        await message.reply(text="Noto'g'ri URL manzil kiritdingiz!")
        return

    await state.update_data(image_url=message.text)
    await state.set_state(AddItemState.price)
    await message.answer("💵 Narxini kiriting (raqam ko'rinishida):")


@router.message(AddItemState.price)
async def item_price(message: Message, state: FSMContext):
    try:
        price = float(message.text)
    except ValueError:
        await message.answer("❌ Iltimos, to'g'ri narx kiriting (faqat raqam).")
        return

    await state.update_data(price=price)
    await state.set_state(AddItemState.category)
    categories = await requests.get_all_categories()
    categories_txt = ""
    for category in categories:
        categories_txt += f"{category.id} - {category.name}\n"

    reply_categories = await message.answer(text=categories_txt)
    await message.answer(text="🏷 Kategoriya ID sini kiriting:", reply_to_message_id=reply_categories.message_id)


@router.message(AddItemState.category)
async def item_category(message: Message, state: FSMContext):
    await state.update_data(category=message.text)
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
    await state.clear()
    await cmd_start_callback__(callback, state)


@router.callback_query(AddItemState.confirm, F.data == "No")
async def item_confirm_no(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        text="Qo'shish jarayoni bekor qilindi!"
    )
    await callback.answer(
        text="Qo'shish jarayoni bekor qilindi!"
    )
    await cmd_start_callback__(callback, state)

