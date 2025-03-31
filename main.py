import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from deep_translator import GoogleTranslator  # Импортируем библиотеку для перевода

TOKEN = "7928323039:AAGUrxWCKqI1Hamw-ACl5CLVyBgUdYb7kno"

bot = Bot(token=TOKEN)
dp = Dispatcher()  # Не передаём bot сюда!
@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Привет!\nЯ бот AiikaTranslatorBot !\nОтправь мне любое сообщение, и я тебе обязательно отвечу.\n"
                         "Я так же могу переводить с других языков! \nНапиши текст, и я переведу его на английский.")

@dp.message()
async def echo(message: Message):
    # Перевод текста с использованием deep_translator
    translated = GoogleTranslator(source='auto', target='en').translate(message.text)  # Перевод на английский
    await message.answer(f"Перевод на английский:\n{translated}")  # Выводим переведённый текст

async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # Очищаем старые обновления
    await dp.start_polling(bot)  # Запускаем бота

if __name__ == "__main__":
    asyncio.run(main())  # Запускаем event loop
