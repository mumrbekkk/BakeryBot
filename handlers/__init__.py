from .cmd_handlers import start_router, add_router
from .msg_handlers import menu_router, big_cakes_router, small_cakes_router, desserts_router, orqaga_router

routers = [
    orqaga_router,
    start_router,
    menu_router,
    big_cakes_router,
    small_cakes_router,
    desserts_router,
    add_router,
]

