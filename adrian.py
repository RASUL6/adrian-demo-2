import logging
from bs4 import BeautifulSoup
from array import *
import requests
from aiogram import Bot, types, executor, Dispatcher
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as fmt
from aiogram import types
import aiogram.utils.markdown as fmt
bot = Bot(token='5418995392:AAEJ98Pv1FdTYQKrxd7lhax8Zm0vhIPiCy0')
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
url = 'https://ru.investing.com/commodities/brent-oil'
page = requests.get(url)
print(page.status_code)
filteredNews = []
allNews = []
soup = BeautifulSoup(page.text, "html.parser")
print(soup)
allNews = soup.findAll('a', class_='lenta')
for data in allNews:
    if data.find('span', class_='time2 time3') is not None:
        filteredNews.append(data.text)

for data in filteredNews:
    print(data)        

@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    await message.reply("Здравствуйте вас приветсвует поисковой бот,чем могу помочь?")
@dp.message_handler(commands="next")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["цены на нефть WTI", "цены на нефть BRENT"]
    keyboard.add(*buttons)
    await message.answer("помощь", reply_markup=keyboard)
@dp.message_handler(Text(equals="цены на нефть WTI"))
async def with_puree(message: types.Message):
    await message.reply("107.06")
@dp.message_handler(Text(equals="цены на нефть BRENT"))
async def with_puree(message: types.Message):
    await message.reply("109.10")
@dp.message_handler(commands="help")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="BRANT", url="https://ru.investing.com/commodities/brent-oil"),
        types.InlineKeyboardButton(text="Performance", url="https://www.profinance.ru/chart/brent/")
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await message.answer("информация о нефти", reply_markup=keyboard)

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
    

