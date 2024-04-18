from aiogram import F, Router
from aiogram.types import CallbackQuery
import app_wending.keyboards as kb

router_two = Router()


@router_two.callback_query(F.data == 'romantic')
async def style_romantic(callback: CallbackQuery):
    await callback.answer('Для романтической')
    await callback.message.edit_text(
        'Романтическая свадьба', reply_markup=kb.next_back_style)


@router_two.callback_query(F.data == 'vintage')
async def style_vintage(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text(
        'Винтажная свадьба', reply_markup=kb.next_back_style)


@router_two.callback_query(F.data == 'eccentric')
async def style_eccentric(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text(
        'Эксцентричная свадьба', reply_markup=kb.next_back_style)


@router_two.callback_query(F.data == 'modern')
async def style_modern(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text(
        'Современная свадьба', reply_markup=kb.next_back_style)


@router_two.callback_query(F.data == 'classic')
async def style_classic(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Классическая свадьба', reply_markup=kb.next_back_style)


@router_two.callback_query(F.data == 'travel')
async def style_travel(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Свадьба в стиле путешествия', reply_markup=kb.next_back_style)


@router_two.callback_query(F.data == 'style')
async def back_style(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Сделайте свой выбор в пользу стиля свадьбы ниже!', reply_markup=kb.style)


@router_two.callback_query(F.data == 'colors')
async def season_summer(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Выберите в какой цветовой палитре?', reply_markup=kb.colors)
