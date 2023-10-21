from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

TOKEN = "Your bot Token"
ADMIN_ID = "Your telegram id"

storage = MemoryStorage()
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
