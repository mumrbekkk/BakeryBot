from aiogram import Bot, Dispatcher

from core.config import BOT_TOKEN
from handlers import routers
from database.models import async_database

"""--------------------------------------------------------------"""

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

for router in routers:
    dp.include_router(router)


async def main():
    await async_database()
    await dp.start_polling(bot)


































""" Starter code if needed"""


# import asyncio
# import logging
#
# from aiogram import Bot, Dispatcher
# from aiogram.filters import CommandStart
# from aiogram.types import Message
#
# from core.config import TOKEN
#
# """--------------------------------------------------------------"""
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# """--------------------------------------------------------------"""
#
#
# @dp.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer(
#         f"Assalomu alaykum "
#         f"Sweet Housening ofitsial botiga xush kelibsiz!"
#         f"\n(Davomi bor...)"
#     )
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# """--------------------------------------------------------------"""
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     try:
#         print("Starting Bakery Bot...")
#         asyncio.run(main())
#     except:
#         print('Exit')












