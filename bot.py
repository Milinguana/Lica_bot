import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Кнопки меню
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("👙 Посмотреть трусики"))
menu.add(KeyboardButton("💌 Сделать заказ"))
menu.add(KeyboardButton("💳 Как оплатить"))
menu.add(KeyboardButton("📦 Условия доставки"))

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        "Привет, я Лиса в кружевах 🦊\n\nВыбери, что тебе интересно:",
        reply_markup=menu
    )

@dp.message_handler(lambda m: m.text == "👙 Посмотреть трусики")
async def catalog_handler(message: types.Message):
    await message.answer("✨ Каталог:\n\n1. Кремовое кружево — 2500₽\n2. Бархат на коже — 2900₽\n\nНапиши, что понравилось 💌")

@dp.message_handler(lambda m: m.text == "💌 Сделать заказ")
async def order_handler(message: types.Message):
    await message.answer("Напиши, что ты хочешь заказать и куда отправить 📦")

@dp.message_handler(lambda m: m.text == "💳 Как оплатить")
async def pay_handler(message: types.Message):
    await message.answer("Оплата: USDT TRC-20\nКошелёк: TVgXXXXXX...\nПосле оплаты — напиши мне и я отправлю твою пару 🧡")

@dp.message_handler(lambda m: m.text == "📦 Условия доставки")
async def delivery_handler(message: types.Message):
    await message.answer("Анонимная упаковка. Отправка по РФ и СНГ. Пиши, обсудим удобный способ.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
