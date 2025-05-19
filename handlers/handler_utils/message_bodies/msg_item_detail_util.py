from aiogram.types import Message

from database.all_requests import get_item_by_name
from helpers.methods import price_to_string


async def msg_item_detail__(message: Message):
    item_name = message.text
    item = await get_item_by_name(item_name)
    price = await price_to_string(item.price)

    await message.answer(
        text=f"<b>{item.name.capitalize()}</b>\n\n"
             f"{item.description}\n"
             f"💵 Narxi: {price} so'm\n\n"
             f"{item.image_url}",
        parse_mode="HTML"
    )