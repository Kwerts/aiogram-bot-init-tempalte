import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import router


load_dotenv()


async def main():
    bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    print('The bot started working.')
    await dispatcher.start_polling(bot)
    
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('The bot has finished working.')