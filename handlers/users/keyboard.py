from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from db_api.commands.users import select_user_id, add_user


async def start(message: Message):
    if not await select_user_id(message.from_user.id):
        await add_user(message.from_user.id)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("SKS")
                                       ],
                                       [
                                           KeyboardButton("Что это?")
                                       ]
                                   ]
                                   )
    return await message.answer("Ну ничего себе, что же ты здесь забыл?", reply_markup=keyboard)


async def what_this(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("Назад")
                                       ]
                                   ]
                                   )
    return await message.answer("жизнь это типа как колодец... там ведро чето... и вода... \n"
                                "SKS Info (https://t.me/+7ZeeST2yEuo4ZTJi)", reply_markup=keyboard)


async def back_1(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("SKS")
                                       ],
                                       [
                                           KeyboardButton("Что это?")
                                       ]
                                   ]
                                   )
    return await  message.answer("Ну ничего себе, что же ты здесь забыл?", reply_markup=keyboard)


async def sks(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("Да 😎"),
                                           KeyboardButton("Нет... 🤔")
                                       ]
                                   ]
                                   )
    return await message.answer("Слушай, а ты тоже бездельник?", reply_markup=keyboard)


async def no(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("Нaзад")
                                       ]
                                   ]
                                   )
    return await message.answer("Тогда что ты здесь делаешь?", reply_markup=keyboard)


async def back_2(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("Да 😎"),
                                           KeyboardButton("Нет... 🤔")
                                       ]
                                   ]
                                   )
    return await message.answer("Слушай, а ты тоже бездельник?", reply_markup=keyboard)


async def yes(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("Всегда мечтал об этом 🤓")
                                       ],
                                       [
                                           KeyboardButton("Я передумал... 🤔")
                                       ]
                                   ]
                                   )
    return await message.answer("Ты правда хочешь подать заявку и работать с лодырями? Слушай, а оно тебе надо? Мы так-то тут нищие сидим...", reply_markup=keyboard)


async def user_think(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("Ок")
                                       ]
                                   ]
                                   )
    return await message.answer("Вот это по-нашему", reply_markup=keyboard)


async def ok(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("SKS")
                                       ],
                                       [
                                           KeyboardButton("Что это?")
                                       ]
                                   ]
                                   )
    return await message.answer("Ну ничего себе, что же ты здесь забыл?", reply_markup=keyboard)


async def dreamed(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("Подать заявку 🍉")
                                       ],
                                       [
                                           KeyboardButton("Всё-таки я не хочу 😎")
                                       ]
                                   ]
                                   )
    return await message.answer("Ладно, давай попробуем подать заявку, вдруг что и получится...", reply_markup=keyboard)


async def i_do_not_want(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("Или давай по новой 🤔")
                                       ],
                                       [
                                           KeyboardButton("В начало")
                                       ]
                                   ]
                                   )
    return await message.answer("Вот и славно, не трать на нас своё время", reply_markup=keyboard)


async def begin(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("SKS")
                                       ],
                                       [
                                           KeyboardButton("Что это?")
                                       ]
                                   ]
                                   )
    return await message.answer("Ну ничего себе, что же ты здесь забыл?", reply_markup=keyboard)


async def or_begin(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("Всегда мечтал об этом 🤓")
                                       ],
                                       [
                                           KeyboardButton("Я передумал... 🤔")
                                       ]
                                   ]
                                   )
    return await message.answer("Ты правда хочешь подать заявку и работать с лодырями? Слушай, а оно тебе надо? Мы так-то тут нищие сидим...", reply_markup=keyboard)


async def application(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("Привлечь инвестиции 🍎")
                                       ],
                                       [
                                           KeyboardButton("Предложить идею 🍏")
                                       ],
                                       [
                                           KeyboardButton("Попасть в команду 🌐")
                                       ],
                                       [
                                           KeyboardButton("Я снова передумал...")
                                       ]
                                   ]
                                   )
    return await message.answer("Стоямба, а куда заявку-то подавать будем?", reply_markup=keyboard)


def register_keyboard_user(dp: Dispatcher):
    dp.register_message_handler(
        start,
        CommandStart()
    )
    dp.register_message_handler(
        what_this,
        Text("Что это?")
    )
    dp.register_message_handler(
        back_1,
        Text("Назад")
    )
    dp.register_message_handler(
        sks,
        Text("SKS")
    )
    dp.register_message_handler(
        no,
        Text("Нет... 🤔")
    )
    dp.register_message_handler(
        back_2,
        Text("Нaзад")
    )
    dp.register_message_handler(
        yes,
        Text("Да 😎")
    )
    dp.register_message_handler(
        user_think,
        Text("Я передумал... 🤔")
    )
    dp.register_message_handler(
        ok,
        Text("Ок")
    )
    dp.register_message_handler(
        dreamed,
        Text("Всегда мечтал об этом 🤓")
    )
    dp.register_message_handler(
        i_do_not_want,
        Text("Всё-таки я не хочу 😎")
    )
    dp.register_message_handler(
        begin,
        Text("В начало")
    )
    dp.register_message_handler(
        or_begin,
        Text("Или давай по новой 🤔")
    )
    dp.register_message_handler(
        application,
        Text("Подать заявку 🍉")
    )
