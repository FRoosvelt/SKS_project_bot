from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, \
    KeyboardButton, Message, ContentType

from data.config import bot, ADMIN_ID
from db_api.commands.users import select_all_users
from states.rasylka import Rasylka

async def rasylka(message: Message):
    back_markups = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [
                                               KeyboardButton('❌Отменить рассылку')
                                           ]
                                       ]
                                       )
    await Rasylka.text.set()
    await message.answer('Напишите текст рассылки', reply_markup=back_markups)


async def app_text_rassylka(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    text_rasylka_markups = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('📤Рассылать', callback_data='text_rasylka'),
                InlineKeyboardButton('🌄Добавить фото', callback_data='photo_rasylka')
            ],
            [
                InlineKeyboardButton('❌Отменить рассылку', callback_data='back_rasylka')
            ]
        ]
    )
    await message.answer('Выберите что делать дальше', reply_markup=text_rasylka_markups)
    await Rasylka.state.set()


async def back_rasylka(message: Message, state: FSMContext):
    await state.finish()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="📤Рассылка")
            ]
        ]
    )
    await message.answer('❌Отменено', reply_markup=keyboard)


async def back_rasylka_call(call: CallbackQuery, state: FSMContext):
    await state.finish()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="📤Рассылка")
            ]
        ]
    )
    await call.message.answer('❌Отменено', reply_markup=keyboard)


async def mailing_text(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    users = await select_all_users()
    await state.finish()
    try:
        for user in users:
            await bot.send_message(chat_id=user, text=text)
    except Exception:
        pass
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="📤Рассылка")
            ]
        ]
    )
    await call.message.answer('✅Рассылка выполнена', reply_markup=keyboard)


async def photo(call: CallbackQuery):
    await Rasylka.photo.set()
    back_markups = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [
                                               KeyboardButton('❌Отменить рассылку')
                                           ]
                                       ]
                                       )
    await call.message.answer('Пришлите фото', reply_markup=back_markups)


async def app_photo(message: Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    await state.update_data(photo=photo_file_id)
    photo_markup = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton('📤Рассылать', callback_data='photo'),
                                                InlineKeyboardButton('❌Отменить', callback_data='back_rasylka')
                                            ]
                                        ]
                                        )
    await message.answer('Выберите что делать дальше', reply_markup=photo_markup)


async def rasylka_photo(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    users = await select_all_users()
    try:
        for user in users:
            await bot.send_photo(chat_id=user, photo=photo, caption=text)
    except Exception:
        pass
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="📤Рассылка")
            ]
        ]
    )
    await call.message.answer('✅Рассылка выполнена', reply_markup=keyboard)

async def back(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="📤Рассылка")
            ]
        ]
    )
    await message.answer('✅Сделано',reply_markup=keyboard)

def register_rasylka(dp: Dispatcher):
    dp.register_message_handler(
        rasylka,
        Text('📤Рассылка'),
        user_id=ADMIN_ID
    )
    dp.register_message_handler(
        back_rasylka,
        Text('❌Отменить рассылку'),
        state='*',
        user_id=ADMIN_ID
    )
    dp.register_message_handler(
        app_text_rassylka,
        state=Rasylka.text,
        user_id=ADMIN_ID
    )
    dp.register_callback_query_handler(
        mailing_text,
        state=Rasylka.state,
        text='text_rasylka',
        user_id=ADMIN_ID
    )
    dp.register_callback_query_handler(
        photo,
        state=Rasylka.state,
        text='photo_rasylka',
        user_id=ADMIN_ID
    )
    dp.register_message_handler(
        app_photo,
        state=Rasylka.photo,
        user_id=ADMIN_ID,
        content_types=ContentType.PHOTO
    )
    dp.register_callback_query_handler(
        back_rasylka_call,
        text='back_rasylka',
        user_id=ADMIN_ID,
        state="*"
    )
    dp.register_callback_query_handler(
        rasylka_photo,
        text='photo',
        state=Rasylka.photo,
        user_id=ADMIN_ID
    )
    dp.register_message_handler(
        back,
        Text('⬅️Назад'),
        user_id=ADMIN_ID,
    )