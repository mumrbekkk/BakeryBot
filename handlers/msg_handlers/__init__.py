from .menu import router as menu_router
from .katta_tortlar import router as big_cakes_router
from .kichik_tortlar import router as small_cakes_router
from .desertlar import router as desserts_router
from .orqaga import router as orqaga_router

__all__ = [
    "menu_router",
    "big_cakes_router",
    "small_cakes_router",
    "desserts_router",
    "orqaga_router",
]


