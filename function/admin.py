from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboard.admin import admin_start_keyboard, workshop_keyboard, vacancy_keyboard
from state.index import Admin_f, Admin_v
from database.connect import *


async def admin_start(message: types.Message):
    await message.answer(text="Assalomu Aleykum Admin \nBugun nimalar qilamiz",
                         reply_markup=admin_start_keyboard())


async def f_add_fn(message: types.Message):
    await Admin_f.f_add.set()
    await message.answer('Yengi Fillial Nomini kiriting:')


async def f_add2_fn(message: types.Message, state: FSMContext):
    all_data = get_all()
    new_obj = {
        "id": all_data[-1]['id'] + 1,
        "title": message.text,
        "vacancy": []
    }
    create(new_obj)
    await state.finish()
    await message.answer('Yengi Fillial Qo`shildi', reply_markup=admin_start_keyboard())


async def f_remove_fn(message: types.Message):
    await Admin_f.f_remove.set()
    await message.answer('Qaysi fillial o`chadi ?', reply_markup=workshop_keyboard())


async def f_remove2_fn(message: types.Message, state: FSMContext):
    all_data = get_all()
    one = 0
    await state.finish()
    for a in all_data:
        if a['title'] == message.text:
            one = a['id']
    if one:
        delete(one)
        await message.answer('Fillial o`chirildi', reply_markup=admin_start_keyboard())


async def v_add_fn(message: types.Message):
    await Admin_v.v_get_add.set()
    await message.answer('Filliallardan birini tanlang:', reply_markup=workshop_keyboard())


async def v_add2_fn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['workshop'] = message.text
    await Admin_v.v_add.set()
    await message.answer(text='Qanday Vakansiya:', reply_markup=ReplyKeyboardRemove())


async def v_add3_fn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        one = data.get('workshop')
    all_data = get_all()
    id = 0
    for a in all_data:
        if a['title'] == one:
            id = a['id']
    if id:
        create_vacancy(id, message.text)
        await message.answer('Vakansita qoshildi:', reply_markup=ReplyKeyboardRemove())
    await state.finish()


async def v_remove_fn(message: types.Message):
    await Admin_v.v_get_remove.set()
    await message.answer('Filliallardan birini tanlang:', reply_markup=workshop_keyboard())


async def v_remove2_fn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['workshop'] = message.text
    await Admin_v.v_remove.set()
    all_data = get_all()
    obj = {"vacancy": []}
    for a in all_data:
        if a['title'] == message.text:
            obj = a
    await message.answer(text='Qaysi Vakansiya:', reply_markup=vacancy_keyboard(obj))


async def v_remove3_fn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        one = data.get('workshop')
    all_data = get_all()
    id = 0
    for a in all_data:
        if a['title'] == one:
            id = a['id']
    if id:
        delete_vacancy(id, message.text)
        await message.answer('Vakansita o`chirildi :', reply_markup=ReplyKeyboardRemove())
    await state.finish()
