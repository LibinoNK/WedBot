from aiogram.utils.formatting import Bold, as_list, as_marked_section


description_for_info_pages = {
    "main": "Добро пожаловать в свадебный бот!",
    "about_b": "Я помогу Вам придумать свадьбу мечты.",
    "about": as_list(
        as_marked_section(
            Bold("Варианты крутейших разрабов:"),
            "Юрист",
            "Инженер конструктор авиационных двигателей",
            "Просто Саня",
        ),
        sep="\n----------------------\n",
    ).as_html(),
    'season': 'Выберите время года',
    'amount': 'Какое кол-во гостей вы ожидаете?',
    'place': 'Выбор места проведения свадьбы!',
    'style': 'Добро пожаловать в выбор стиля',
    'colors': 'Выберите в какой цветовой палитре?',
    'fashion': 'Выберите силуэт свадебного платья',
    'costume': 'Выберите костюм жениха',
}
