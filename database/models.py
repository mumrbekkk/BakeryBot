from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite3")
async_session = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(200))

    sweet_items = relationship("SweetItem", back_populates="item_category")


class SweetItem(Base):
    __tablename__ = "sweet_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(200))
    image_url: Mapped[str] = mapped_column(String(200))
    price: Mapped[str] = mapped_column()
    category: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    item_category = relationship("Category", back_populates="sweet_items")


async def async_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


