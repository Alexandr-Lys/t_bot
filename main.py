import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

dp = Dispatcher()


@dp.message()
async def cmd_start(message: Message):
    await message.answer('Привет')


async def main():
    token = os.getenv("TOKEN")
    if not token:
        raise ValueError("Токен не найден. Убедитесь, что переменная окружения TOKEN установлена.")
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
