from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from database.connect import get_all
from keyboard.index import student_keyboard, time_keyboard, back_keyboard, workshop_keyboard, vacancy_keyboard
from state.index import MainState
from setting import bot, ADMIN


async def start_fn(message: types.Message):
    await MainState.username.set()
    await message.answer(text="""Assalomu Aleykum hayrli kun😊 Xush kelibsiz
Ariza topshirish uchun passportdagi Ism va Familiyangizni kiriting:""", reply_markup=ReplyKeyboardRemove())


async def back_fn(message: types.Message, state: FSMContext):
    prev_state = await state.get_state()

    if prev_state is not None:
        if prev_state == MainState.username.state:
            await message.answer(text="Assalomu Aleykum hayrli kun😊 Xush kelibsiz"
                                      "\nAriza topshirish uchun passportdagi Ism va Familiyangizni kiriting:",
                                 reply_markup=ReplyKeyboardRemove())
        elif prev_state == MainState.age.state:
            await message.answer(text='Passportdagi Ism va Familiyangizni qayta kiriting:', reply_markup=back_keyboard())
        elif prev_state == MainState.location.state:
            await message.answer(text='Yoshingizni kiriting: \n(Misol: 19)', reply_markup=back_keyboard())
        elif prev_state == MainState.phone.state:
            await message.answer(text="Yashash manzilingiz (tuman, ko'cha/kvartal, uy/kvartira):",
                                 reply_markup=back_keyboard())
        elif prev_state == MainState.student.state:
            await message.answer(text="Telefon raqamingizni kiriting: \n(Misol: +998901234567)",
                                 reply_markup=back_keyboard())
        elif prev_state == MainState.time.state:
            await message.answer(text="Talabamisiz:", reply_markup=student_keyboard())
        elif prev_state == MainState.workshops.state:
            await message.answer(text='Qaysi vaqtlar ishlay olasiz:', reply_markup=time_keyboard())
        elif prev_state == MainState.vacancy.state:
            await message.answer(text='Filliallardan birini tanlang:', reply_markup=workshop_keyboard())

    else:
        await message.answer(text="Assalomu Aleykum hayrli kun😊 Xush kelibsiz "
                                  "\n Ariza topshirish uchun passportdagi Ism va Familiyangizni kiriting:""", reply_markup=ReplyKeyboardRemove())
    await MainState.previous()


async def username_fn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await MainState.age.set()
    await message.answer(text='Yoshingizni kiriting: \n(Misol: 19)', reply_markup=back_keyboard())


async def age_fn(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and 10 < int(text) < 60:
        async with state.proxy() as data:
            data['age'] = text
        await MainState.location.set()
        await message.answer(text="Yashash manzilingiz (tuman, ko'cha/kvartal, uy/kvartira):",
                             reply_markup=back_keyboard())
    else:
        await message.answer(text='Yoshingizni kiriting: \n(Misol: 19)', reply_markup=back_keyboard())


async def location_fn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['location'] = message.text
    await MainState.phone.set()
    await message.answer(text="Telefon raqamingizni kiriting: \n(Misol: +998901234567)", reply_markup=back_keyboard())


async def phone_fn(message: types.Message, state: FSMContext):
    text = message.text
    if text.startswith('+998') and len(text) == 13 and text[4:].isdigit():
        async with state.proxy() as data:
            data['phone'] = text
        await MainState.student.set()
        await message.answer(text="Talabamisiz:", reply_markup=student_keyboard())
    else:
        await message.answer(text="Telefon raqamingizni kiriting: \n(Misol: +998901234567)",
                             reply_markup=back_keyboard())


async def student_fn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['student'] = message.text
    await MainState.time.set()
    await message.answer(text='Qaysi vaqtlar ishlay olasiz:', reply_markup=time_keyboard())


async def time_fn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
    await MainState.workshops.set()
    await message.answer(text='Filliallardan birini tanlang:', reply_markup=workshop_keyboard())


async def workshops_fn(message: types.Message, state: FSMContext):
    all_data = get_all()
    one_data = list(filter(lambda x: x['title'] == message.text, all_data))
    if one_data:
        async with state.proxy() as data:
            data['workshops'] = message.text
        await MainState.vacancy.set()

        return await message.answer(text="Yo'nalishni tanlang:", reply_markup=vacancy_keyboard(one_data[0]))
    await message.answer(text='Berilgan filliallardan birini tanlang:', reply_markup=workshop_keyboard())


async def vacancy_fn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['vacancy'] = message.text
    await MainState.cv.set()
    await message.answer(
        text="Avval Ishlagan joyingiz haqida qisqacha yozing yoki ishlamagan boʻlsangiz "
             "“ishlamaganman” tarzida yozing:",
        reply_markup=back_keyboard())


async def cv_fn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        text = f"""
        <b>Yengi Ariza keldi...</b>
        
🇺🇿 <code>Telegram id</code>: <b>{message.from_user.id}</b>,
👨‍💼 <code>Ismi</code>: <b>{data.get('username', 'N/A')}</b>,
🕐 <code>Yosh</code>: <b>{data.get('age', 'N/A')} yosh</b>,
📞 <code>Aloqa</code>: <b>{data.get('phone', 'N/A')}</b>,
📍 <code>Manzil</code>: <b>{data.get('location', 'N/A')}</b>,
👨‍🎓 <code>Talaba</code>: <b>{data.get('student', 'N/A')}</b>,
⏰ <code>Ishlash Vaqti</code>: <b>{data.get('time', 'N/A')}</b>,
🌃 <code>Hudud</code>: <b>{data.get('workshops', 'N/A')}</b>,
🧍 <code>Qaysi Yonalishda</code>: <b>{data.get('vacancy', 'N/A')}</b>,
🔎 <code>Eski Ishxonasi</code>: <b>{message.text}</b>
        """

    await bot.send_message(chat_id=ADMIN, text=text, parse_mode='html')
    await state.finish()
    await message.answer(text="Ma'lumot uchun rahmat! \n"
                              "Tez orada siz bilan +998909514006 nomer orqali bog'lanamiz",
                         reply_markup=ReplyKeyboardRemove())
