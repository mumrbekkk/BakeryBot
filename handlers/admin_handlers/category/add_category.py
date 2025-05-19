from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

from states.keyboard_states import ReplyKeyboardState
from states.add_category_states import AddCategoryState
from utils.constants import constants_uz
from utils.keyboards import inline_kb
from handlers.handler_utils.message_bodies.msg_category_util import msg_category__
from database.models import Category
from database.all_requests import add_category
from helpers.validators import validate_category_name


router = Router()


@router.message(ReplyKeyboardState.category_state, F.text == constants_uz.ADD_CATEGORY_TXT)
async def msg_add_category(message: Message, state: FSMContext):
    await message.reply(
        text="Kategoriya nomini kiriting",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=constants_uz.BACK_MSG_HANDLER_TXT)]
            ],
            resize_keyboard=True
        )
    )

    await state.set_state(AddCategoryState.category_name_state)


@router.message(AddCategoryState.category_name_state)
async def category_name(message: Message, state: FSMContext):
    input_name = message.text
    if not await validate_category_name(category_name=input_name, message=message):
        return

    await state.update_data(category_name=input_name)
    await message.answer(text="Kategoriya tavsifini kiriting")

    await state.set_state(AddCategoryState.category_description_state)


@router.message(AddCategoryState.category_description_state)
async def category_description(message: Message, state: FSMContext):
    await state.update_data(category_description=message.text)

    data = await state.get_data()
    await message.answer(text=f"Kategoriya nomi: {data['category_name']}\n"
                              f"Kategoriya tavsifi: {data['category_description']}\n\n"
                              f"Tasdiqlaysizmi?",
                         reply_markup=await inline_kb.confirmation_kb("back_to_category"))

    await state.set_state(AddCategoryState.add_category_confirm_state)


@router.callback_query(AddCategoryState.add_category_confirm_state, F.data == "confirm")
async def callback_confirm_category(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    new_category = Category(name=data['category_name'], description=data['category_description'])

    if new_category:
        success = await add_category(new_category)
        if success:
            await callback.answer(text="Kategoriya muoffaqiyatli qo'shildi ✅")
            await callback.message.edit_text(text="Kategoriya muoffaqiyatli qo'shildi ✅")
            await msg_category__(state=state, message=callback.message)
            return
    await callback.answer(text="Xatolik yuz berdi🚫")


@router.callback_query(AddCategoryState.add_category_confirm_state, F.data == "back_to_category")
async def callback_back_to_category(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Kategoriya qo'shish jarayoni bekor qilindi ✅", reply_markup=None)
    await msg_category__(state, message=callback.message)





