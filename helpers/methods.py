from database.all_requests import get_user_by_username
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


async def string_price_to_int(price: str) -> int:
    _price = ""
    for i in price:
        if i == ",":
            continue
        else:
            _price += i

    return int(_price)


async def send_data_to_admin(bot, data):
    admin = await get_user_by_username(constants.ADMIN_2_USERNAME)
    admin_staff = await get_user_by_username(constants.ADMIN_1_USERNAME)

    if admin:
        await bot.send_message(admin.tg_id, data)
    elif admin_staff:
        await bot.send_message(admin_staff.tg_id, data)



async def price_filter_pairs(start, end, step):
    range_list = [i for i in range(start, end, step)]
    return_list = []
    for current, next in zip(range_list, range_list[1:]):
        return_list.append([current, next])

    return return_list


