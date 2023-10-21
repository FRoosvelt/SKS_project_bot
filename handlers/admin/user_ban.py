from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from data.config import ADMIN_ID
from db_api.commands.users import update_user_ban_status, select_user_id
from db_api.tables.users import Users


async def ban_user_command(message: Message):
    args = message.get_args()
    if not args:
        return await message.reply(
            '<b> Отсутствуют аргументы к команде!</b>'
        )

    try:
        user: Users = await select_user_id(args)
        if not user:
            return await message.answer(
                '<b> Такого пользователя не существует!</b>'
            )
        need_ban = message.text.startswith('/ban')
        delete_ban = message.text.startswith('/unban')
        if need_ban and user.is_blocked:
            return await message.reply(
                '<b> Пользователь итак заблокирован!</b>'
            )
        elif delete_ban and not user.is_blocked:
            return await message.reply(
                '<b> Пользователь итак разблокирован!</b>'
            )
        await update_user_ban_status(user.user_id, True if not user.is_blocked else False)
        await message.bot.send_message(
                user.user_id,
                '<b> ❌Ваш аккаунт заблокирован!</b>' if not user.is_blocked
                else '<b> ✅Ваш аккаунт разблокирован!</b>'
            )
        await message.reply(
                f'<b> ❌Пользователь заблокирован!</b>'
                if not user.is_blocked
                else f'<b> ✅Пользователь разблокирован!</b>'
            )
    except ValueError:
        await message.reply(
            '<b> Значение должно быть числом!</b>'
        )


def register_ban_command(dp: Dispatcher):
    dp.register_message_handler(
        ban_user_command,
        Text(startswith=['/ban', '/unban']),
        user_id=ADMIN_ID,
        state='*'
    )