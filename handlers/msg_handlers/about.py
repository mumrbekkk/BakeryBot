from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.constants import constants_uz
from utils.keyboards import reply_kb
from states.keyboard_states import ReplyKeyboardState

router = Router()


@router.message(ReplyKeyboardState.home_state, F.text == constants_uz.ABOUT_MSG_HANDLER_TXT)
async def msg_about(message: Message, state: FSMContext):
    await state.set_state(ReplyKeyboardState.about_state)

    await message.reply(
        text=constants_uz.ABOUT_MSG_TXT,
        reply_markup=await reply_kb.about_kb()
    )


@router.message(ReplyKeyboardState.about_state, F.text == constants_uz.INSTAGRAM_MSG_HANDLER_TXT)
async def msg_instagram(message: Message):
    await message.answer_photo(photo=constants_uz.INSTAGRAM_IMG_LINK)
    await message.reply(text="👇🏻Bizni instagram sahifamizda kuzatib boring 😊")
    await message.answer(text=constants_uz.INSTAGRAM_LINK)


@router.message(ReplyKeyboardState.about_state, F.text == constants_uz.TELEGRAM_MSG_HANDLER_TXT)
async def msg_instagram(message: Message):
    await message.answer_photo(photo=constants_uz.TELEGRAM_IMG_LINK)
    await message.reply("👇🏻Bizni telegram sahifamizda kuzatib boring 😊")
    await message.answer(constants_uz.TELEGRAM_LINK)


@router.message(ReplyKeyboardState.about_state, F.text == constants_uz.BACKUP_CONTACTS_MSG_HANDLER_TXT)
async def msg_instagram(message: Message):
    await message.answer("☎️ 90-090-01-64")
    await message.answer("📍Adres: Shovot lelinizm 49 IDUM yoni, Zargar ko'chasi 46-uy")





