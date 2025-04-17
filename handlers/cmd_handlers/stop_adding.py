from states.add_item_states import AddItemState

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command("stop"))
async def stop_adding(message: Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == AddItemState.name.state or current_state == AddItemState.description.state or current_state == AddItemState.image_url.state or current_state == AddItemState.price.state or current_state == AddItemState.category.state:
        await state.clear()
    else:
        return

    await message.reply("Qo'shish forma to'ldirish jarayoni bekor qilindi!")

