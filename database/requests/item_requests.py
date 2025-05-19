from database.models import SweetItem, async_session

from sqlalchemy import select


async def get_items_by_price_range(min_price: int, max_price: int):
    async with async_session() as session:
        query = select(SweetItem).where(SweetItem.price.between(min_price, max_price))
        result = await session.execute(query)
        items = result.scalars().all()

        return items
