
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
    if username == "m_umrbekkk":
        return True
    elif username == "NargizaRahmatullayeva":
        return True
    else:
        return False

