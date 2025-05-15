from database.models import async_session
from database.models import User, Category, SweetItem

from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import SQLAlchemyError


# --------------------------- USER MODEL RELATED --------------------------- #
async def set_user(tg_id, username):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(
                User(
                    tg_id=tg_id,
                    user_name=username
                )
            )
            await session.commit()


async def get_user_by_username(username: str) -> User:
    async with async_session() as session:
        user = await session.scalar(
            select(User)
            .where(User.user_name == username)
        )
    return user


# --------------------------- CATEGORY MODEL RELATED --------------------------- #
async def get_all_categories():
    async with async_session() as session:
        categories = await session.scalars(select(Category))
    return categories


async def get_category_by_id(category_id: int) -> Category | None:
    async with async_session() as session:
        category = await session.scalar(
            select(Category)
            .where(Category.id == category_id)
        )
    return category


async def get_category_by_name(category_name: str) -> Category:
    async with async_session() as session:
        category = await session.scalar(
            select(Category)
            .options(selectinload(Category.sweet_items))
            .where(Category.name == category_name)
        )
    return category


async def add_category(category: Category) -> bool:
    async with async_session() as session:
        try:
            session.add(category)
            await session.commit()
            return True
        except:
            return False


async def update_category_field(category_id: int, field_to_update: str, new_value: str) -> str:
    async with async_session() as session:
        category = await session.get(Category, category_id)
        if not category:
            return f"Kategoriya topilmadi"
        if hasattr(category, field_to_update):
            setattr(category, field_to_update, new_value)
            await session.commit()
            return "Muoffaqiyatli o'zgartirildi"

        return "Hatolik :("


async def delete_category_by_id(category_id: int) -> str:
    async with async_session() as session:
        category = await session.get(Category, category_id)
        if not category:
            return f"Kategoriya topilmadi"
        try:
            await session.delete(category)
            await session.commit()
            return "Kategoriya muoffaqiyatli o'chirildi"
        except:
            return "O'chirishda hatolik :("


# --------------------------- ITEM MODEL RELATED --------------------------- #
async def get_all_items():
    async with async_session() as session:
        items = await session.scalars(select(SweetItem))
    return items


async def add_item(new_item: SweetItem):
    async with async_session() as session:
        session.add(new_item)
        await session.commit()


async def get_items_by_category_id(category_id: int):
    async with async_session() as session:
        items = await session.scalars(
            select(SweetItem)
            .where(SweetItem.category == category_id)
        )
    return items


async def get_item_by_name(name: str):
    async with async_session() as session:
        item = await session.scalar(
            select(SweetItem)
            .options(selectinload(SweetItem.item_category))
            .where(SweetItem.name == name)
        )

    return item


async def get_item_by_id(item_id: int) -> SweetItem | None:
    async with async_session() as session:
        query = (
            select(SweetItem)
            .options(selectinload(SweetItem.item_category))
            .where(SweetItem.id == item_id)
        )
        result = await session.execute(query)
        item = result.scalars().first()
    return item


async def get_items_by_category_name(category_name: str):
    category = await get_category_by_name(category_name)
    return category.sweet_items


async def update_item_field(item_id: int, field_name: str, new_value: str) -> bool:
    async with async_session() as session:
        item = await session.get(SweetItem, item_id)
        if not item:
            return False
        if hasattr(item, field_name):
            setattr(item, field_name, new_value)
            await session.commit()
            return True
        else:
            return False


async def delete_item_by_id(item_id: int):
    async with async_session() as session:
        item = await session.scalar(
            select(SweetItem).where(SweetItem.id == item_id)
        )
        await session.delete(item)
        await session.commit()








