from setting import dp
from function.index import *
from function.admin import *
from var.index import *
from state.index import MainState


@dp.message_handler(commands=['start'], state="*")
async def start(message: types.Message):
    if ADMIN == message.from_user.id:
        await admin_start(message)
    else:
        await start_fn(message)


@dp.message_handler(text=fillial_qoshish)
async def f_add(message: types.Message):
    await f_add_fn(message)


@dp.message_handler(state=Admin_f.f_add)
async def f_add2(message: types.Message, state: FSMContext):
    await f_add2_fn(message, state)


@dp.message_handler(text=fillial_ochirish)
async def f_remove(message: types.Message):
    await f_remove_fn(message)


@dp.message_handler(state=Admin_f.f_remove)
async def f_remove2(message: types.Message, state: FSMContext):
    await f_remove2_fn(message, state)


@dp.message_handler(text=vacancy_qoshish)
async def v_add(message: types.Message):
    await v_add_fn(message)


@dp.message_handler(state=Admin_v.v_get_add)
async def v_add2(message: types.Message, state: FSMContext):
    await v_add2_fn(message, state)


@dp.message_handler(state=Admin_v.v_add)
async def v_add3(message: types.Message, state: FSMContext):
    await v_add3_fn(message, state)


@dp.message_handler(text=vacancy_ochirish)
async def v_remove(message: types.Message):
    await v_remove_fn(message)


@dp.message_handler(state=Admin_v.v_get_remove)
async def v_remove2(message: types.Message, state: FSMContext):
    await v_remove2_fn(message, state)


@dp.message_handler(state=Admin_v.v_remove)
async def v_remove3(message: types.Message, state: FSMContext):
    await v_remove3_fn(message, state)


@dp.message_handler(text="Ortga qaytish 🔙", state="*")
async def back(message: types.Message, state: FSMContext):
    await back_fn(message, state)


@dp.message_handler(state=MainState.username)
async def username(message: types.Message, state: FSMContext):
    await username_fn(message, state)


@dp.message_handler(state=MainState.age)
async def age(message: types.Message, state: FSMContext):
    await age_fn(message, state)


@dp.message_handler(state=MainState.location)
async def location(message: types.Message, state: FSMContext):
    await location_fn(message, state)


@dp.message_handler(state=MainState.phone)
async def phone(message: types.Message, state: FSMContext):
    await phone_fn(message, state)


@dp.message_handler(state=MainState.student)
async def student(message: types.Message, state: FSMContext):
    await student_fn(message, state)


@dp.message_handler(state=MainState.time)
async def time(message: types.Message, state: FSMContext):
    await time_fn(message, state)


@dp.message_handler(state=MainState.workshops)
async def workshops(message: types.Message, state: FSMContext):
    await workshops_fn(message, state)


@dp.message_handler(state=MainState.vacancy)
async def vacancy(message: types.Message, state: FSMContext):
    await vacancy_fn(message, state)


@dp.message_handler(state=MainState.cv)
async def cv(message: types.Message, state: FSMContext):
    await cv_fn(message, state)
