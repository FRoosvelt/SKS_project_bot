from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from data.config import ADMIN_ID, bot
from db_api.commands.application import add_application, select_cont_id_application
from states.application import Application

from db_api.tables.application import application_table


async def type_application_invest(message: Message, state: FSMContext):
    type_application = message.text
    application = application_table()
    application.type = type_application
    await state.update_data(application=application)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton("Рассказать ✏️")
            ],
            [
                KeyboardButton("Haзад")
            ]
        ]
    )
    return await message.answer("Ох, ну и эгоист же ты... Что ж, давай рассказывай свой бизнес-план, а мы что-нибудь придумаем",reply_markup=keyboard)

async def i_again_changed(message: Message, state: FSMContext):
    await state.finish()
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
    return await message.answer("Вот и славно, не трать на нас своё время", reply_markup=keyboard)

async def back(message: Message, state: FSMContext):
    await state.finish()
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

async def speak_invest(message: Message):
    await Application.text.set()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton("Haзад")
            ]
        ]
    )
    return await message.answer("Напиши сочинение на тему: «Как я заработал свой первый миллион»\n"
                        "Ладно, шучу\n\n\n"


                        "Заполняй заявку по форме:\n"
                        "1. Направление своей гениальной идеи, в которую ты хочешь привлечь наши средства\n"
                        "2. Опиши своё дело в трёх словах\n"
                        "3. Окупаемость\n"
                        "4. Сколько средств тебе необходимо?", reply_markup=keyboard)

async def text_invest(message: Message, state: FSMContext):
    data = await state.get_data()
    text = message.text
    application: application_table = data.get("application")
    application.text = text
    await state.update_data(application=application)
    await add_application(user_id=message.from_user.id, type=application.type, text=application.text)
    application_id = await select_cont_id_application()
    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Ответить", callback_data=f"support: {message.from_user.id}")
            ]
        ]
    )
    await bot.send_message(chat_id=ADMIN_ID, text=f"#{application_id}\n"
                                                  f"<b>{message.from_user.id}</>\n"
                                                  f"{application.type}\n"
                                                  f"{application.text}\n", reply_markup=inline_keyboard)
    await state.finish()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton("Вернуться в начало")
            ]
        ]
    )
    return await message.answer("Молодец, мы рассмотрим твою заявку в ближайшее время", reply_markup=keyboard)

async def begin_back(message: Message, state: FSMContext):
    await state.finish()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("Да 😎"),
                                           KeyboardButton("Нет... 🤔")
                                       ]
                                   ]
                                   )
    return await message.answer("Слушай, а ты тоже бездельник?", reply_markup=keyboard)

async def type_idea(message: Message, state: FSMContext):
    await Application.text.set()
    type_application = message.text
    application = Application()
    application.type = type_application
    await state.update_data(application=application)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton("Haзад")
            ]
        ]
    )
    return await message.answer("Так, а вот это нам нравится. Ну-ка рассказывай, что ты хочешь предложить?", reply_markup=keyboard)

async def text_idea(message: Message, state: FSMContext):
    data = await state.get_data()
    text = message.text
    application: application_table = data.get("application")
    application.text = text
    await state.update_data(application=application)
    await add_application(user_id=message.from_user.id, type=application.type, text=application.text)
    application_id = await select_cont_id_application()
    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Ответить", callback_data=f"support: {message.from_user.id}")
            ]
        ]
    )
    await bot.send_message(chat_id=ADMIN_ID, text=f"#{application_id}\n"
                                                  f"<b>{message.from_user.id}</>\n"
                                                  f"{application.type}\n"
                                                  f"{application.text}\n", reply_markup=inline_keyboard)
    await state.finish()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton("Вернуться в начало")
            ]
        ]
    )
    return await message.answer("Молодец, мы рассмотрим твою заявку в ближайшее время", reply_markup=keyboard)

async def command(message: Message):
    await Application.type.set()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton("Да 🤓")
            ],
            [
                KeyboardButton("Нет, я занятой человек")
            ]
        ]
    )
    return await message.answer("Губа не дура...\n\n"

                                "Ты точно хочешь попасть к нам в команду и бездельничать вместе с нами?", reply_markup=keyboard)

async def no_people(message: Message, state: FSMContext):
    await state.finish()
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

async def yes_command(message: Message, state: FSMContext):
    type_application = "Попасть в команду 🌐"
    application = application_table()
    application.type = type_application
    await state.update_data(application=application)
    await Application.text.set()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton("Haзад")
            ]
        ]
    )
    return await message.answer("Тогда расскажи о себе:\n"
                                "1. Кто ты? Работаешь, учишься?\n"
                                "2. С кем работал?\n"
                                "3. С чем работал?\n"
                                "4. И вообще, почему именно ты? Вроде таких как ты миллионы... А может я ошибаюсь...", reply_markup=keyboard)

async def command_text(message: Message, state: FSMContext):
    data = await state.get_data()
    text = message.text
    application: application_table = data.get("application")
    application.text = text
    await state.update_data(application=application)
    await add_application(user_id=message.from_user.id, type=application.type, text=application.text)
    application_id = await select_cont_id_application()
    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Ответить", callback_data=f"support: {message.from_user.id}")
            ]
        ]
    )
    await bot.send_message(chat_id=ADMIN_ID, text=f"#{application_id}\n"
                                                  f"<b>{message.from_user.id}</>\n"
                                                  f"{application.type}\n"
                                                  f"{application.text}\n", reply_markup=inline_keyboard)
    await state.finish()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton("Вернуться в начало")
            ]
        ]
    )
    return await message.answer("Молодец, мы рассмотрим твою заявку в ближайшее время", reply_markup=keyboard)

async def back_type(message: Message, state: FSMContext):
    await state.finish()
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


def register_application(dp: Dispatcher):
    dp.register_message_handler(
        back,
        Text("Haзад"),
        state=["*",Application.text, Application.type, None]
    )
    dp.register_message_handler(
        type_application_invest,
        Text("Привлечь инвестиции 🍎")
    )
    dp.register_message_handler(
        speak_invest,
        Text("Рассказать ✏️")
    )
    dp.register_message_handler(
        text_invest,
        state=Application.text
    )
    dp.register_message_handler(
        i_again_changed,
        Text("Я снова передумал...")
    )
    dp.register_message_handler(
        back_type,
        Text("Haзад"),
        state=Application.text
    )
    dp.register_message_handler(
        type_idea,
        Text("Предложить идею 🍏"),
    )
    dp.register_message_handler(
        text_idea,
        state=Application.text
    )
    dp.register_message_handler(
        command,
        Text("Попасть в команду 🌐")
    )
    dp.register_message_handler(
        no_people,
        Text("Нет, я занятой человек"),
        state=Application.type
    )
    dp.register_message_handler(
        yes_command,
        Text("Да 🤓"),
        state=Application.type
    )
    dp.register_message_handler(
        command_text,
        state=Application.text
    )
    dp.register_message_handler(
        begin_back,
        Text("Вернуться в начало")
    )
