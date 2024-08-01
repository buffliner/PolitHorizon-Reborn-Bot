import asyncio
import logging

from aiogram import Bot, Dispatcher

import config
from handlers import router

async def main():
    bot = Bot(token=config.botToken)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())