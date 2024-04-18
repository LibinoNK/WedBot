from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)

################### Клавиатура для возврата назад переиспользуется
back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='Назад')]])

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Старт квиза', callback_data='quiz'),
     InlineKeyboardButton(text='Результат', callback_data='result')],
    [InlineKeyboardButton(text='О боте', callback_data='about_b'),
     InlineKeyboardButton(text='О нас', callback_data='about')],
])

#################### Выбор сезона свадьбы #########################

seasons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='💐         Весна         💐', callback_data='spring'),
     InlineKeyboardButton(text='💐         Лето          💐', callback_data='summer')],
    [InlineKeyboardButton(text='💐         Осень         💐', callback_data='autumn'),
     InlineKeyboardButton(text='💐         Зима          💐', callback_data='winter')],
    [InlineKeyboardButton(text='Назад', callback_data='Назад')],
])

next_back_season = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='seasons'),
     InlineKeyboardButton(text='Далее', callback_data='onward')]])

""" Выбор количества участников свадьбы """
amount = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Только вдвоем', callback_data='together'),
     InlineKeyboardButton(text='Только близкие', callback_data='folks')],
    [InlineKeyboardButton(text='До 100', callback_data='upto100'),
     InlineKeyboardButton(text='Более 100', callback_data='more100')],
    [InlineKeyboardButton(text='Назад', callback_data='seasons')],
])

next_back_amount = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='amount'),
     InlineKeyboardButton(text='Далее', callback_data='farther')]])

""" Выбор стиля свадьбы """

style = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Романтическая свадьба', callback_data='romantic'),
     InlineKeyboardButton(text='Винтажная свадьба', callback_data='vintage')],
    [InlineKeyboardButton(text='Эксцентричная свадьба', callback_data='eccentric'),
     InlineKeyboardButton(text='Современная свадьба', callback_data='modern')],
    [InlineKeyboardButton(text='Классическая свадьба', callback_data='classic'),
     InlineKeyboardButton(text='Свадьба в стиле travel', callback_data='travel')],
    [InlineKeyboardButton(text='Назад', callback_data='amount')],
])

next_back_style = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='style'),
     InlineKeyboardButton(text='Далее', callback_data='colors')]])

""" Выбор цветовой палитры """

colors = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Изумрудно-зеленый', callback_data='emerald_green'),
     InlineKeyboardButton(text='Ванильный', callback_data='vanilla_cream')],
    [InlineKeyboardButton(text='Капучино', callback_data='macchiato'),
     InlineKeyboardButton(text='Пыльная роза', callback_data='dusty_rose')],
    [InlineKeyboardButton(text='Винный', callback_data='wine'),
     InlineKeyboardButton(text='Розовый кварц', callback_data='quartz_pink')],
    [InlineKeyboardButton(text='Назад', callback_data='style')],
])

next_back_colors = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='colors'),
     InlineKeyboardButton(text='Далее', callback_data='colors')]])

""" Выбор цветовой палитры """