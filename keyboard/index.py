from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from database.connect import get_all


def student_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [KeyboardButton('Ha 👨‍🎓'), KeyboardButton("Yo'q 👨‍💼"), KeyboardButton("Ortga qaytish 🔙")]
    keyboard.add(*buttons)
    return keyboard


def time_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [KeyboardButton('1 smen 🌇'), KeyboardButton("2 smen 🌃"), KeyboardButton("Ortga qaytish 🔙")]
    keyboard.add(*buttons)
    return keyboard


def back_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton("Ortga qaytish 🔙")]
    keyboard.add(*buttons)
    return keyboard


def workshop_keyboard():
    all_data = get_all()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    for a in all_data:
        buttons.append(KeyboardButton(a['title']))

    buttons.append(KeyboardButton("Ortga qaytish 🔙"))
    keyboard.add(*buttons)
    return keyboard


def vacancy_keyboard(obj):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    for a in obj['vacancy']:
        buttons.append(KeyboardButton(a))

    buttons.append(KeyboardButton("Ortga qaytish 🔙"))
    keyboard.add(*buttons)
    return keyboard

