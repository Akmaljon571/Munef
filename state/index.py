from aiogram.dispatcher.filters.state import State, StatesGroup


class MainState(StatesGroup):
    username = State()
    age = State()
    location = State()
    phone = State()
    student = State()
    time = State()
    workshops = State()
    vacancy = State()
    cv = State()


class Admin_f(StatesGroup):
    f_add = State()
    f_remove = State()


class Admin_v(StatesGroup):
    v_get_add = State()
    v_get_remove = State()
    v_add = State()
    v_remove = State()
