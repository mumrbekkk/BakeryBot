from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.keyboard_states import ReplyKeyboardState
from states.add_category_states import AddCategoryState
from utils.constants import constants_uz
from handlers.handler_utils.command_bodies.cmd_start_util import cmd_start_message__
from handlers.handler_utils.message_bodies.msg_menu_util import msg_menu__
from handlers.handler_utils.message_bodies.msg_admin_util import msg_admin__
from handlers.handler_utils.message_bodies.msg_category_util import msg_category__
from handlers.handler_utils.message_bodies.msg_price_filter_util import msg_price_filter__


router = Router()


@router.message(F.text == constants_uz.BACK_MSG_HANDLER_TXT)
async def msg_back(message: Message, state: FSMContext):
    current_state = await state.get_state()
    # MENU CONDITION
    if current_state == ReplyKeyboardState.menu_state.state:
        await cmd_start_message__(message, state)

    elif current_state == ReplyKeyboardState.menu_category_state.state:
        await msg_menu__(message, state)

    elif current_state == ReplyKeyboardState.price_filter_state:
        await msg_menu__(message, state)

    elif current_state == ReplyKeyboardState.price_filter_item_state:
        await msg_price_filter__(message, state)

    # ABOUT CONDITION
    elif current_state == ReplyKeyboardState.about_state.state:
        await cmd_start_message__(message, state)

    # ADMIN CONDITION
    elif current_state == ReplyKeyboardState.admin_state.state:
        await cmd_start_message__(message, state)

    # ITEM CONDITION
    elif current_state == ReplyKeyboardState.item_state.state:
        await msg_admin__(message, state)

    # CATEGORY CONDITION
    elif current_state == ReplyKeyboardState.category_state.state:
        await msg_admin__(message, state)

    elif current_state == AddCategoryState.category_name_state.state:
        await msg_category__(state, message=message)



