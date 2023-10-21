from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, ContentTypes

from data.config import bot, ADMIN_ID
from keyboards.support import support_keyboard, support_callback


async def send_to_support(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()
    user_id = int(callback_data.get("user_id"))

    await call.message.answer("Оформите текст заявки")
    await state.set_state("wait_for_support_message")
    await state.update_data(second_id=user_id)

async def get_support_message(message: Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get("second_id")

    await bot.send_message(second_id,
                           f"<b>{message.from_user.id}</>\n"
                           f"У вас 1 непрочитанное сообщение!")
    keyboard = await support_keyboard(messages="one", user_id=message.from_user.id)
    await message.send_copy(second_id, reply_markup=keyboard)

    await message.answer("Заявка успешно отправлена!")
    await state.reset_state()

async def get_support_admin(message: Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get("second_id")

    await bot.send_message(second_id,
                           f"У вас 1 непрочитанное сообщение!")
    keyboard = await support_keyboard(messages="one", user_id=message.from_user.id)
    await message.send_copy(second_id, reply_markup=keyboard)

    await message.answer("Заявка успешно отправлена!")
    await state.reset_state()

def register_support_user(dp: Dispatcher):
    dp.register_callback_query_handler(
        send_to_support,
        support_callback.filter(messages="one")
    )
    dp.register_message_handler(
        get_support_message,
        state="wait_for_support_message",
        content_types=ContentTypes.ANY
    )
    dp.register_message_handler(
        get_support_message,
        state="wait_for_support_message",
        content_types=ContentTypes.ANY,
        user_id=ADMIN_ID
    )
