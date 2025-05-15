from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from database.models import SweetItem, Category
from database.requests import get_all_categories, get_items_by_category_id


async def menu_kb():
    keyboard = InlineKeyboardBuilder()

    categories = await get_all_categories()
    for category in categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))

    keyboard.add(InlineKeyboardButton(text="🔙 Orqaga", callback_data=f"back_to_home"))
    return keyboard.adjust(1).as_markup()


async def category_items_kb(category_id: int):
    keyboard = InlineKeyboardBuilder()
    items = await get_items_by_category_id(category_id)

    for item in items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"))

    keyboard.add(InlineKeyboardButton(text="🔙 Orqaga", callback_data=f"back_to_menu"))
    return keyboard.adjust(1).as_markup()


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
    keyboard.add(InlineKeyboardButton(text="🔙 Mahsulotlar bo'limiga qaytish", callback_data="back_to_item"))

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
    keyboard.add(InlineKeyboardButton(text=f"🏷 Kategoriya: {item.item_category.name} [id: {item.category}]", callback_data=f"sweetitem_kategoriyasi"))
    keyboard.add(InlineKeyboardButton(text=f"🔙 Orqaga", callback_data=f"item_{item.id}"))

    return keyboard.adjust(1).as_markup()


async def update_item_field_kb(item_id: int):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text=f"🔙 Orqaga", callback_data=f"update_{item_id}"))

    return keyboard.adjust(1).as_markup()


async def confirmation_kb(back_callback: str):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text="✅ Ha", callback_data="confirm"))
    keyboard.add(InlineKeyboardButton(text="❌ Yo'q", callback_data=back_callback))

    return keyboard.adjust(2).as_markup()


# <ADMIN> CATEGORY SECTION
async def category_list_kb():
    keyboard = InlineKeyboardBuilder()

    categories = await get_all_categories()
    for category in categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    keyboard.add(InlineKeyboardButton(text=f"🔙 Orqaga", callback_data="back_to_category"))

    return keyboard.adjust(1).as_markup()


async def category_detail_kb():
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text="✏ Tahrirlash", callback_data=f"update_category"))
    keyboard.add(InlineKeyboardButton(text="🗑 O'chirish", callback_data=f"delete_category"))
    keyboard.add(InlineKeyboardButton(text="🔙 Orqaga", callback_data=f"back_to_category_list"))

    return keyboard.adjust(2).as_markup()


async def edit_category_kb(category: Category):
    keyboard = InlineKeyboardBuilder()
    cat_id = category.id

    keyboard.add(InlineKeyboardButton(text=f"Nomi: {category.name}", callback_data="update_category_name"))
    keyboard.add(InlineKeyboardButton(text=f"Tavsifi: {category.description}", callback_data="update_category_description"))
    keyboard.add(InlineKeyboardButton(text=f"🔙 Orqaga", callback_data=f"category_{cat_id}"))

    return keyboard.adjust(1).as_markup()


async def update_category_field_kb(category_id: int):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text=f"🔙 Orqaga", callback_data=f"update_category_{category_id}"))

    return keyboard.adjust(1).as_markup()

