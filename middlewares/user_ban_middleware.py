from aiogram import Dispatcher
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery, InlineQuery

from db_api.commands.users import select_user_id
class UserBannedMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        user = await select_user_id(message.from_user.id)
        if user and user.is_blocked:
            await message.answer(
                '<b> ❌ Ваш аккаунт заблокирован! Обратитесь к @whysanioks </b>'
            )
            raise CancelHandler

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):
        user = await select_user_id(call.from_user.id)
        if user and user.is_blocked:
            await call.answer(
                '<b> ❌ Ваш аккаунт заблокирован! Обратитесь к @whysanioks <b>',
                show_alert=True
            )
            raise CancelHandler

    async def on_process_inline_query(self, query: InlineQuery, data: dict):
        user = await select_user_id(query.from_user.id)
        if user and user.is_blocked:
            raise CancelHandler


def setup_ban_middleware(dp: Dispatcher):
    dp.middleware.setup(UserBannedMiddleware())
