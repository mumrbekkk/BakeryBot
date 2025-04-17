from database.models import async_session
from database.models import User, Category, SweetItem

from sqlalchemy import select
from sqlalchemy.orm import selectinload


# --------------------------- USER MODEL RELATED --------------------------- #
async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


# --------------------------- CATEGORY MODEL RELATED --------------------------- #
async def get_all_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))


# --------------------------- ITEM MODEL RELATED --------------------------- #
async def add_item(new_item: SweetItem):
    async with async_session() as session:
        session.add(new_item)
        await session.commit()

async def get_items_by_category_id(category_id: int):
    async with async_session() as session:
        return await session.scalars(
            select(SweetItem)
            .where(SweetItem.category == category_id)
        )


async def get_item_by_name(name: str):
    async with async_session() as session:
        try:
            return await session.scalar(
                select(SweetItem)
                .options(selectinload(SweetItem.item_category))
                .where(SweetItem.name == name)
            )
        except Exception as e:
            return f"Something went wrong --> {e}"



