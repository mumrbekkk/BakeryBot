from database.models import async_session
from database.models import User, Category, SweetItem

from sqlalchemy import select
from sqlalchemy.orm import selectinload


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
        user = await session.scalar(select(User).where(User.user_name == username))

    return user


# --------------------------- CATEGORY MODEL RELATED --------------------------- #
async def get_all_categories():
    async with async_session() as session:
        categories = await session.scalars(select(Category))
    return categories


# --------------------------- ITEM MODEL RELATED --------------------------- #
async def get_all_items():
    async with async_session() as session:
        items = session.scalars(select(SweetItem))
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
            .where(SweetItem.id == item_id)
        )
        result = await session.execute(query)
        item = result.scalars().first()

    return item

