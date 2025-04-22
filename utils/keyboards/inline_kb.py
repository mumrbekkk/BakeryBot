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

    for item in item_list:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text="🔐 Admin panelga qaytish", callback_data="back_to_admin_panel"))

    return keyboard.adjust(1).as_markup()


async def item_detail_kb(item_id: int):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text="✏ Tahrirlash", callback_data=f"update_{item_id}"))
    keyboard.add(InlineKeyboardButton(text="🗑 O'chirish", callback_data=f"delete_{item_id}"))
    keyboard.add(InlineKeyboardButton(text="🔙 Orqaga", callback_data=f"back_to_list"))

    return keyboard.adjust(2).as_markup()


async def delete_confirmation_kb(item_id: int):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text="✅ Ha", callback_data=f"confirm_delete_{item_id}"))
    keyboard.add(InlineKeyboardButton(text="❌ Yo'q", callback_data=f"item_{item_id}"))

    return keyboard.adjust(2).as_markup()


async def back_to_list_kb():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_list"))

    return keyboard.adjust(1).as_markup()


async def update_item_kb(item: SweetItem):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text=f"📦 Nomi: {item.name}", callback_data=f"sweetitem_nomi"))
    keyboard.add(InlineKeyboardButton(text=f"🖊 Tavsifi: {item.description}", callback_data=f"sweetitem_tavsifi"))
    keyboard.add(InlineKeyboardButton(text=f"🖼 Rasm: {item.image_url}", callback_data=f"sweetitem_rasmi"))
    keyboard.add(InlineKeyboardButton(text=f"💵 Narxi: {item.price}", callback_data=f"sweetitem_narxi"))
    keyboard.add(InlineKeyboardButton(text=f"🏷 Kategoriya: {item.category}", callback_data=f"sweetitem_kategoriyasi"))
    keyboard.add(InlineKeyboardButton(text=f"🔙 Orqaga", callback_data=f"item_{item.id}"))

    return keyboard.adjust(1).as_markup()


async def update_item_field_kb(item_id: int):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text=f"🔙 Orqaga", callback_data=f"update_{item_id}"))

    return keyboard.adjust(1).as_markup()


async def update_item_field_confirmation_kb(callback_: str):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text="✅ Ha", callback_data="update_confirm"))
    keyboard.add(InlineKeyboardButton(text="❌ Yo'q", callback_data=callback_))

    return keyboard.adjust(2).as_markup()


