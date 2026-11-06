import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sessions import StringSession

from handlers import callback, commands

# Загружаем переменные из .env до их чтения
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
SESSION_STRING = os.getenv('SESSION_STRING')


async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    # Запускаем Telethon один раз
    telethon_client = TelegramClient(
        StringSession(SESSION_STRING),
        API_ID,
        API_HASH,
        connection_retries=10,
        retry_delay=5,
        timeout=30,
    )
    await telethon_client.connect()
    print("Telethon подключён!")

    try:
        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        # Очищаем папку downloads при старте
        for f in os.listdir("downloads"):
            try:
                os.remove(os.path.join("downloads", f))
            except OSError:
                pass
        print("Папка downloads очищена")

        dp.include_router(commands.router)
        dp.include_router(callback.router)

        # Передаём telethon_client в handlers через bot
        bot.telethon = telethon_client

        print('Bot Start')
        # Снимаем webhook, иначе polling не работает (TelegramConflictError)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as ex:
        print(f"There is an Exception: {ex}")
    finally:
        await bot.session.close()
        await telethon_client.disconnect()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')