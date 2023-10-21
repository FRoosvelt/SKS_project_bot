from aiogram.dispatcher.filters.state import StatesGroup, State


class Rasylka(StatesGroup):
    photo = State()
    text = State()
    state = State()
