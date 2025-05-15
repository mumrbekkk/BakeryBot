from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from utils.constants import constants_uz
from states.comment_states import CommentState
from utils.keyboards import inline_kb
from helpers.methods import send_data_to_admin
from states.keyboard_states import ReplyKeyboardState
from handlers.handler_utils.command_bodies.cmd_start_util import cmd_start_callback__

router = Router()


@router.message(ReplyKeyboardState.home_state, F.text == constants_uz.COMMENT_QUESTION_MSG_HANDLER_TXT)
async def msg_comment(message: Message, state: FSMContext):
    await state.set_state(CommentState.comment)
    await message.reply(text="Izoh yoki savolingizni yozib qoldiring...",
                        reply_markup=ReplyKeyboardRemove())
    await message.answer(text="Izoh yozish jarayonini bekor qilish👇🏻",
                         reply_markup=await inline_kb.comment_cancellation_kb())


@router.message(CommentState.comment)
async def msg_get_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    await state.set_state(CommentState.confirmation)

    await message.reply(text="Izohingiz to'g'rimi?"
                             "\nIzoh yoki Savolingizni qayta tekshirib tasdiqlang...",
                        reply_markup=await inline_kb.comment_confirmation_kb())


@router.callback_query(CommentState.confirmation, F.data == "Yes")
async def callback_yes(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    data_to_send = (f"Izoh: {data['comment']}"
                    f"\nUsername: @{callback.from_user.username}")

    await send_data_to_admin(bot=callback.bot, data=data_to_send)

    await callback.answer("Tasdiqlandi!")
    await callback.message.edit_text("Izohingiz qabul qilindi, tez orada admin siz bilan bo'glanadi!"
                                     "\nE'tibor va sabringiz uchun raxmat!")
    await state.clear()

    await cmd_start_callback__(callback, state)


@router.callback_query(StateFilter(CommentState.comment, CommentState.confirmation), F.data == "No")
async def callback_no(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Muoffaqiyatli bekor qilindi!")
    await callback.message.edit_text("Izoh qoldirish jarayoni muoffaqiyatli bekor qilindi!"
                                     "\nE'tibor va sabringiz uchun raxmat!")
    await state.clear()
    await cmd_start_callback__(callback, state)

