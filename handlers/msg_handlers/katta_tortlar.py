from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.keyboard_states import ReplyKeyboardState
from utils.keyboards import reply_kb
from utils.constants import constants_uz
from database.requests import get_item_by_name

router = Router()


@router.message(ReplyKeyboardState.menu_state, F.text == constants_uz.BIG_CAKES_MSG_HANDLER_TXT)
async def msg_big_cakes(message: Message, state: FSMContext):
    await state.set_state(ReplyKeyboardState.big_cakes_state)

    await message.reply(
        text=constants_uz.BIG_CAKES_REPLY_TXT,
        reply_markup=await reply_kb.item_by_category_kb(1)
    )


@router.message(ReplyKeyboardState.big_cakes_state)
async def msg_big_cake_details(message: Message):
    user_message = message.text
    item = await get_item_by_name(user_message)

    if item:
        await message.answer_photo(photo=item.image_url)
        await message.reply(text=f"\n------------------------------------------"
                                 f"\nNarxi: {int(item.price) or 0} so'm"
                                 f"\nKategoriya: {item.item_category.name}"
                                 f"\n------------------------------------------"
                                 f"\n{item.description}")






