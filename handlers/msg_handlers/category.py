from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from states.keyboard_states import ReplyKeyboardState
from utils.keyboards import reply_kb
from handlers.handler_utils.message_bodies.msg_item_detail_util import msg_item_detail__


router = Router()


@router.message(ReplyKeyboardState.menu_state)
async def msg_category(message: Message, state: FSMContext):
    category_name = message.text
    await message.answer(text=f"{category_name} kategoriya mahsulotlari",
                         reply_markup=await reply_kb.category_kb(category_name=category_name))

    await state.set_state(ReplyKeyboardState.menu_category_state)


@router.message(ReplyKeyboardState.menu_category_state)
async def msg_category_item_detail(message: Message):
    await msg_item_detail__(message)









