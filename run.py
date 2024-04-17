import asyncio
import logging
from os import getenv
from dotenv import find_dotenv, load_dotenv
from aiogram import Bot, Dispatcher
from app_wending.handlers import router
from app_wending.handlers_1_2 import router_one
from app_wending.handlers_3 import router_two

load_dotenv(find_dotenv())


async def main():
    bot = Bot(token=getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(router_one)
    dp.include_router(router_two)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
