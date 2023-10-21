from aiogram import Dispatcher

from handlers.admin.keyboard import register_keyboard_admin
from handlers.admin.rasylka import register_rasylka
from handlers.admin.support import register_support_admin
from handlers.admin.user_ban import register_ban_command
from handlers.users.application import register_application
from handlers.users.keyboard import register_keyboard_user
from handlers.users.support import register_support_user
from middlewares.user_ban_middleware import setup_ban_middleware

def register(dp: Dispatcher):
    register_keyboard_admin(dp)
    register_keyboard_user(dp)
    register_application(dp)
    register_support_admin(dp)
    register_support_user(dp)
    register_ban_command(dp)
    register_rasylka(dp)

def setup_middlewares(dp: Dispatcher):
    setup_ban_middleware(dp)