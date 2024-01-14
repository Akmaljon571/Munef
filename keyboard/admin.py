from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from database.connect import get_all
from var.index import *


def admin_start_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [KeyboardButton(fillial_qoshish), KeyboardButton(fillial_ochirish),
               KeyboardButton(vacancy_qoshish), KeyboardButton(vacancy_ochirish)]

    keyboard.add(*buttons)
    return keyboard


def workshop_keyboard():
    all_data = get_all()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    for a in all_data:
        buttons.append(KeyboardButton(a['title']))

    keyboard.add(*buttons)
    return keyboard


def vacancy_keyboard(obj):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    for a in obj['vacancy']:
        buttons.append(KeyboardButton(a))

    keyboard.add(*buttons)
    return keyboard
