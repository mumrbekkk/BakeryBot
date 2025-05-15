from handlers.admin_handlers import category
from .cmd_handlers import start
from .msg_handlers import (about, admin, category, comment_question, menu, orqaga)

from handlers.admin_handlers.category import (
    msg_category, category_list, category_details,
    edit_category, delete_category, add_category
)
from handlers.admin_handlers.item import (
    msg_item, add_item, item_list, item_details, edit_item, delete_item
)

routers = [
    start.router,
    menu.router,
    orqaga.router,
    category.router,
    comment_question.router,
    about.router,
    admin.router,
]

category_routers = [
    msg_category.router,
    category_list.router,
    category_details.router,
    edit_category.router,
    delete_category.router,
    add_category.router
]


item_routers = [
    msg_item.router,
    add_item.router,
    item_list.router,
    item_details.router,
    edit_item.router,
    delete_item.router
]


routers = routers + category_routers + item_routers



