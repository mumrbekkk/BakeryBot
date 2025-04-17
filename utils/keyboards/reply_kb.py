from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils.constants import constants_uz
from database.requests import get_items_by_category_id, get_all_categories


async def start_kb(is_admin: bool):
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text=constants_uz.MENU_MSG_HANDLER_TXT))
    keyboard.add(KeyboardButton(text=constants_uz.ABOUT_MSG_HANDLER_TXT))

    if is_admin:
        keyboard.add(KeyboardButton(text="/mahsulot_qoshish"))
        keyboard.add(KeyboardButton(text="/stop"))

    return keyboard.adjust(1).as_markup(resize_keyboard=True, input_field_placeholder=constants_uz.START_KB_CAPTION)


async def categories_kb():
    keyboard = ReplyKeyboardBuilder()
    categories = await get_all_categories()
    for category in categories:
        keyboard.add(KeyboardButton(text=category.name))

    keyboard.add(KeyboardButton(text=constants_uz.BACK_MSG_HANDLER_TXT))
    return keyboard.adjust(2).as_markup(resize_keyboard=True)


async def item_by_category_kb(category_id: int):
    keyboard = ReplyKeyboardBuilder()
    items_by_category = await get_items_by_category_id(category_id)

    for item in items_by_category:
        keyboard.add(KeyboardButton(text=item.name))

    keyboard.add(KeyboardButton(text=constants_uz.BACK_MSG_HANDLER_TXT))
    return keyboard.adjust(2).as_markup(resize_keyboard=True)

