# Подключение  api телеграм бота
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN_telega = '5854451170:AAEIUVyG2wTkzouXGp5LoKcf8yDNbjPWFDs'
bot = Bot(token=API_TOKEN_telega)
dp = Dispatcher(bot)


# Работа в телеграм боте
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button0 = KeyboardButton('Бот, что ты умеешь?')
btns0 = ReplyKeyboardMarkup(resize_keyboard=True).row(button0)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   user_name = message.from_user.first_name
   await message.reply(f'Халлоу, {user_name}', reply_markup = btns0)


button_1_1 = KeyboardButton('Выбрать валюту')
btns_1 = ReplyKeyboardMarkup(resize_keyboard=True).row(button_1_1)


@dp.message_handler(lambda message: message.text == 'Бот, что ты умеешь?')
async def choose_2(message: types.Message):
   await message.reply('Я 🤖 скажу 📣 тебе актуальную стоимость 💰 криптовалюты', reply_markup = btns_1)

button_1_1 = KeyboardButton('Выбрать валюту')
btns_1 = ReplyKeyboardMarkup(resize_keyboard=True).row(button_1_1)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   user_name = message.from_user.first_name
   await message.reply(f'Халлоу, {user_name}', reply_markup = btns_1)


button_2_1 = KeyboardButton('/BTC')
button_2_2 = KeyboardButton('/ETH')
button_2_3 = KeyboardButton('ТОП-10 криптовалют')
btns_2 = ReplyKeyboardMarkup(resize_keyboard=True).row(button_2_1,button_2_2,button_2_3)

@dp.message_handler(lambda message: message.text == 'ТОП-10 криптовалют')
async def choose_2(message: types.Message):
   await message.reply('ТОП-10: \n/BNB \n/XRP \n/ADA \n/MATIC \n/DOGE \n/SOL \n/DOT \n/SHIB \n/LTC \n/TRON')

@dp.message_handler(lambda message: message.text == 'Выбрать валюту')
async def choose_2(message: types.Message):
   await message.reply('Выбери валюту или укажите ее тикер (например, /bnb) чтобы узнать ее стоимость', reply_markup = btns_2)


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
urlkb = InlineKeyboardMarkup(row_width=1)
urlButton=InlineKeyboardButton(text='Перейти на coinmarketcap.com', url='https://coinmarketcap.com/')
urlkb.add(urlButton)

# Считывание сообщения пользователя и вывод цены криптовалюты
@dp.message_handler()
async def choose_3(message):
   txt = str(message['text'])
   txt = txt[1:]
   a='symbol'
   b=txt
   b=txt.upper()
   diction={a:b}
   from requests import Request, Session
   from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
   import json
   url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
   parameters = diction
   headers = {
   'Accepts': 'application/json',
   'X-CMC_PRO_API_KEY': '5b73a7b6-4155-4e42-9e66-00ec87ca3a9e',
   }
   session = Session()
   session.headers.update(headers)
   try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
   except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
   import math
   name = (data['data'][b]['name'])
   sym = (data['data'][b]['symbol'])
   price=round(data['data'][b]['quote']['USD']['price'],4)
   await message.reply(f'{name} | {sym} USD: ${price}',reply_markup=urlkb)
   # await message.reply(price)
   

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)