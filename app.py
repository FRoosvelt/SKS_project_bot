import logging

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor

from data.config import TOKEN, storage
from db_api.database import create_base
from register import register, setup_middlewares


async def on_startup(dp: Dispatcher):
    setup_middlewares(dp)
    register(dp)
    await create_base()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(bot, storage=storage)
    executor.start_polling(dp, on_startup=on_startup)