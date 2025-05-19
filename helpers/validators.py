from aiogram.types import Message, CallbackQuery

from database.all_requests import get_category_by_id, get_category_by_name
from utils.constants import constants
from database import all_requests as requests


async def is_admin_or_not(username) -> bool:
    if username == constants.ADMIN_1_USERNAME:
        return True
    elif username == constants.ADMIN_2_USERNAME:
        return True
    return False


# ADD FORM VALIDATORS
async def validate_name(name: str, message: Message = None, callback: CallbackQuery = None) -> bool:
    item = await requests.get_item_by_name(name)
    if item:
        if callback:
            await callback.message.reply("Bu mahsulot mavjud! Boshqa ism kiriting!")
            return False

        await message.reply("Bu mahsulot mavjud! Boshqa ism kiriting!")
        return False

    return True


async def validate_url(url: str, message: Message = None, callback: CallbackQuery = None) -> bool:
    if not (url.startswith("http://") or url.startswith("https://")):
        if callback:
            await callback.message.reply(text="Noto'g'ri URL manzil kiritdingiz!")
            return False
        await message.reply(text="Noto'g'ri URL manzil kiritdingiz!")
        return False

    return True


async def validate_price(price: str, message: Message = None, callback: CallbackQuery = None) -> bool:
    try:
        int(price)
    except ValueError:
        if callback:
            await callback.message.reply("❌ Iltimos, faqat raqam kiriting.")
            return False

        await message.reply("❌ Iltimos, faqat raqam kiriting.")
        return False

    return True


async def validate_category(category_id: str, message: Message = None, callback: CallbackQuery = None) -> bool:
    try:
        category_id_int = int(category_id)
    except ValueError:
        if callback:
            await callback.message.reply("Kategoriya IDsini raqam bo'lishi kerak")
            return False
        await message.reply("Kategoriya IDsini raqam bo'lishi kerak")
        return False

    category = await get_category_by_id(category_id_int)
    if not category:
        if callback:
            await callback.message.reply(f"{category_id} - ID ostidagi kategoriya topilmadi")
            return False
        await message.reply(f"{category_id} - ID ostidagi kategoriya topilmadi")
        return False

    return True


async def validate_updating_field(field_to_update: str, value: str, message: Message) -> bool:
    if field_to_update == "name":
        return await validate_name(value, message=message)
    elif field_to_update == "image_url":
        return await validate_url(value, message=message)
    elif field_to_update == "price":
        return await validate_price(value, message=message)
    elif field_to_update == "category":
        return await validate_category(value, message=message)

    return True


async def validate_category_name(category_name: str, message: Message = None) -> bool:
    category_exists = await get_category_by_name(category_name)
    if category_exists:
        await message.answer(text="Bu kategoriya mavjud!")
        return False

    return True









