from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup

from utils.constants import constants_uz
from database.all_requests import get_all_categories, get_items_by_category_name
from helpers.methods import price_filter_pairs, price_to_string


async def start_kb(is_admin: bool):
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text=constants_uz.MENU_MSG_HANDLER_TXT))
    keyboard.add(KeyboardButton(text=constants_uz.COMMENT_QUESTION_MSG_HANDLER_TXT))
    keyboard.add(KeyboardButton(text=constants_uz.ABOUT_MSG_HANDLER_TXT))

    if is_admin:
        keyboard.add(KeyboardButton(text=constants_uz.ADMIN_MSG_HANDLER_TXT))

    return keyboard.adjust(1).as_markup(resize_keyboard=True, input_field_placeholder=constants_uz.START_KB_CAPTION)


async def menu_kb():
    keyboard = ReplyKeyboardBuilder()
    categories = await get_all_categories()
    if categories:
        for category in categories:
            keyboard.add(KeyboardButton(text=category.name))

    keyboard.add(KeyboardButton(text=constants_uz.MSG_FILTER_PRICE_TXT))
    keyboard.add(KeyboardButton(text=constants_uz.BACK_MSG_HANDLER_TXT))
    return keyboard.adjust(2).as_markup(resize_keyboard=True)


async def category_kb(item_list=None, category_name: str = None):
    keyboard = ReplyKeyboardBuilder()

    if category_name:
        items = await get_items_by_category_name(category_name)
    else:
        items = item_list

    if items:
        for item in items:
            keyboard.add(KeyboardButton(text=item.name))

    keyboard.add(KeyboardButton(text=constants_uz.BACK_MSG_HANDLER_TXT))
    return keyboard.adjust(2).as_markup(resize_keyboard=True)


async def price_filter_kb():
    keyboard = ReplyKeyboardBuilder()
    price_list = await price_filter_pairs(25000, 500001, 25000)

    for price_range in price_list:
        start = await price_to_string(price_range[0])
        end = await price_to_string(price_range[1])
        keyboard.add(KeyboardButton(text=f"{start} - {end}"))

    keyboard.add(KeyboardButton(text=constants_uz.BACK_MSG_HANDLER_TXT))
    return keyboard.adjust(2).as_markup()


async def about_kb():
    keyboard = ReplyKeyboardBuilder()

    keyboard.add(KeyboardButton(text=constants_uz.INSTAGRAM_MSG_HANDLER_TXT))
    keyboard.add(KeyboardButton(text=constants_uz.TELEGRAM_MSG_HANDLER_TXT))
    keyboard.add(KeyboardButton(text=constants_uz.BACKUP_CONTACTS_MSG_HANDLER_TXT))
    keyboard.add(KeyboardButton(text=constants_uz.BACK_MSG_HANDLER_TXT))

    return keyboard.adjust(1).as_markup(resize_keyboard=True)


# ADMIN KEYBOARD
async def admin_kb():
    keyboard = ReplyKeyboardBuilder()

    keyboard.add(KeyboardButton(text=constants_uz.ADMIN_ITEM_MSG_HANDLER_TXT))
    keyboard.add(KeyboardButton(text=constants_uz.ADMIN_CATEGORY_MSG_HANDLER_TXT))
    keyboard.add(KeyboardButton(text=constants_uz.BACK_MSG_HANDLER_TXT))

    return keyboard.adjust(1).as_markup(resize_keyboard=True)


item_admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=constants_uz.ITEM_LIST_MSG_HANDLER_TXT)],
        [KeyboardButton(text=constants_uz.ADD_ITEM_CMD_HANDLER_TXT)],
        [KeyboardButton(text=constants_uz.BACK_MSG_HANDLER_TXT)],
    ],
    resize_keyboard=True
)


async def category_admin_kb():
    keyboard = ReplyKeyboardBuilder()

    keyboard.add(KeyboardButton(text=constants_uz.ALL_CATEGORIES_TXT))
    keyboard.add(KeyboardButton(text=constants_uz.ADD_CATEGORY_TXT))
    keyboard.add(KeyboardButton(text=constants_uz.BACK_MSG_HANDLER_TXT))

    return keyboard.adjust(1).as_markup(resize_keyboard=True)
