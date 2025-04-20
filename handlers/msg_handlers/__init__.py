from .menu import router as menu_router
from .katta_tortlar import router as big_cakes_router
from .kichik_tortlar import router as small_cakes_router
from .desertlar import router as desserts_router
from .orqaga import router as orqaga_router
from .comment_question import router as comment_router
from .about import router as about_router
from .admin import router as admin_router

__all__ = [
    "menu_router",
    "big_cakes_router",
    "small_cakes_router",
    "desserts_router",
    "orqaga_router",
    "comment_router",
    "about_router",
    "admin_router",
]


