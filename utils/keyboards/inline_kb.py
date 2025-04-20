from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from database.models import SweetItem

async def comment_cancellation_kb():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Bekor qilish", callback_data="No"))

    return keyboard.adjust(1).as_markup()


async def comment_confirmation_kb():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Tasdiqlayman", callback_data="Yes"))
    keyboard.add(InlineKeyboardButton(text="Bekor qilish", callback_data="No"))

    return keyboard.adjust(1).as_markup()


async def item_addition_kb():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Tasdiqlayman", callback_data="Yes"))
    keyboard.add(InlineKeyboardButton(text="Bekor qilish", callback_data="No"))

    return keyboard.adjust(1).as_markup()


async def items_list_kb(item_list):
    keyboard = InlineKeyboardBuilder()

    for item in await item_list:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"))

    return keyboard.adjust(2).as_markup()


async def item_detail_kb(item_id: int):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text="✏ Tahrirlash", callback_data=f"update_{item_id}"))
    keyboard.add(InlineKeyboardButton(text="🗑 O'chirish", callback_data=f"delete_{item_id}"))
    keyboard.add(InlineKeyboardButton(text="🔙 Orqaga", callback_data=f"back_to_list"))

    return keyboard.adjust(2).as_markup()





