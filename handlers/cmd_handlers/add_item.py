from database import requests
from database.models import SweetItem
from states.add_item_states import AddItemState

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command("produkt_qoshish"))
async def add_item(message: Message, state: FSMContext):
    await message.answer(text=message.from_user.username)
    username = message.from_user.username
    if username != "m_umrbekkk" and username != "NargizaRahmatullayeva":
        return

    await state.set_state(AddItemState.name)
    await message.reply("Product qo'shish uchun quyidagi formani to'ldiring...")
    await message.answer("📝 Mahsulot nomini kiriting:")


@router.message(AddItemState.name)
async def item_name(message: Message, state: FSMContext):
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
    await message.answer("🏷 Kategoriya ID sini kiriting:")


@router.message(AddItemState.category)
async def item_category(message: Message, state: FSMContext):
    await state.update_data(category=message.text)
    data = await state.get_data()

    await requests.add_item(
        SweetItem(
            name=data['name'],
            description=data['description'],
            image_url=data['image_url'],
            price=data['price'],
            category=data['category']
        )
    )
    await message.answer("✅ Mahsulot muvaffaqiyatli qo‘shildi!")
    await message.answer(
        f"""
        📦 Nomi: {data['name']}
        🖊 Tavsifi: {data['description']}
        🖼 Rasm: {data['image_url']}
        💵 Narxi: {data['price']}
        🏷 Kategoriya: {data['category']}
        """)
    await state.clear()





