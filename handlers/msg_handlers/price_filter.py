from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from utils.constants.constants_uz import *
from states.keyboard_states import ReplyKeyboardState
from utils.keyboards import reply_kb
from database.requests.item_requests import get_items_by_price_range
from helpers.methods import string_price_to_int
from handlers.handler_utils.message_bodies.msg_price_filter_util import msg_price_filter__
from handlers.handler_utils.message_bodies.msg_item_detail_util import msg_item_detail__


router = Router()


@router.message(ReplyKeyboardState.menu_state, F.text == MSG_FILTER_PRICE_TXT)
async def msg_price_filter(message: Message, state: FSMContext):
    await msg_price_filter__(message, state)


@router.message(ReplyKeyboardState.price_filter_state)
async def msg_items_by_price(message: Message, state: FSMContext):
    price_range = message.text.split(" - ")
    min_price = await string_price_to_int(price_range[0])
    max_price = await string_price_to_int(price_range[1])

    items = await get_items_by_price_range(min_price, max_price)

    if items:
        item_names = ", ".join(item.name for item in items)

        await message.reply(
            text=f"Barcha mahsulotlar nomi\n\n"
                 f"{item_names}",
            reply_markup=await reply_kb.category_kb(item_list=items)
        )
    else:
        await message.answer(text="Kiritilgan narxlarda mahsulot mavjud emas")

    await state.set_state(ReplyKeyboardState.price_filter_item_state)


@router.message(ReplyKeyboardState.price_filter_item_state)
async def msg_price_filter_item_detail(message: Message):
    await msg_item_detail__(message)



