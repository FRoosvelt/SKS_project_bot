from aiogram.dispatcher.filters.state import StatesGroup, State


class Application(StatesGroup):
    type = State()
    text = State()