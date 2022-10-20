from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
TOKEN = "5327216230:AAHrg1tzBgWDWEfy2fDQ-vHWir9Be1qmQ-8"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])  #Явно указываем в декораторе, на какую команду реагируем.
async def send_welcome(msg: types.Message):
    await msg.reply_to_message(f'Я бот. Приятно познакомиться,{msg.from_user.first_name}')

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    print(msg.text)
    if msg.text.lower() in ('привет', '/привет'):
       await msg.answer('Привет!')
    else:
       await msg.answer('Не понимаю, что это значит.')  

if __name__ == '__main__':
   executor.start_polling(dp)                             