from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Dispatcher

from data.config import ADMIN_ID


async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="📤Рассылка")
            ]
        ]
    )
    return await message.answer("Слушаю, BOS", reply_markup=keyboard)

def register_keyboard_admin(dp: Dispatcher):
    dp.register_message_handler(
        start,
        CommandStart(),
        user_id=ADMIN_ID
    )