from database.requests import get_user_by_username
from utils.constants import constants


async def price_to_string(price: int):
    price_list = [i for i in str(price)]
    price_list.reverse()

    price_list_copy = [i for i in str(price)]
    price_list_copy.reverse()

    add_up = 0
    for index, i in enumerate(price_list):
        if index == 0:
            continue
        if index % 3 == 0:
            price_list_copy.insert(index + add_up, ",")
            add_up += 1

    price_list_copy.reverse()
    price_str = "".join(price_list_copy)

    return price_str


async def is_admin_or_not(username) -> bool:
    if username == constants.ADMIN_1_USERNAME:
        return True
    elif username == constants.ADMIN_2_USERNAME:
        return True
    else:
        return False


async def send_data_to_admin(bot, data):
    admin = await get_user_by_username(constants.ADMIN_3_USERNAME) or await get_user_by_username(constants.ADMIN_1_USERNAME)

    if admin:
        await bot.send_message(admin.tg_id, data)


