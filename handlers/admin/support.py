from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery, Message, ContentTypes

from data.config import ADMIN_ID, bot
from keyboards.support import support_keyboard


async def send_to_support(call: CallbackQuery, state: FSMContext):
    await call.answer()
    split = call.data.split()
    user_id = int(split[1])

    await call.message.answer("⬇️Пришлите ваше сообщение, которым вы хотите поделиться")
    await state.set_state("wait_for_support_message")
    await state.update_data(second_id=user_id)

async def get_support_message(message: Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get("second_id")

    await bot.send_message(second_id,
                           f"Вам письмо! Вы можете ответить нажав на кнопку ниже")
    keyboard = await support_keyboard(messages="one", user_id=message.from_user.id)
    await message.send_copy(second_id, reply_markup=keyboard)

    await message.answer("Вы отправили это сообщение!")
    await state.reset_state()

def register_support_admin(dp: Dispatcher):
    dp.register_callback_query_handler(
        send_to_support,
        Text(startswith="support"),
        user_id=ADMIN_ID
    )
    dp.register_message_handler(
        get_support_message,
        content_types=ContentTypes.ANY,
        state="wait_for_support_message",
        user_id=ADMIN_ID
    )