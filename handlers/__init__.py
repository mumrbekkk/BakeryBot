from .admin_handlers import add_router, stop_adding_router, all_items_router, item_details_router
from .cmd_handlers import start_router
from .msg_handlers import (menu_router, big_cakes_router, small_cakes_router, desserts_router,
                           orqaga_router, comment_router, about_router, admin_router)

routers = [
    orqaga_router,
    start_router,
    menu_router,
    big_cakes_router,
    small_cakes_router,
    desserts_router,
    comment_router,
    about_router,
    admin_router,
    stop_adding_router,
    add_router,
    all_items_router,
    item_details_router,
]

