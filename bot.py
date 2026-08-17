from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from keyboardd import *
from Functions import *
from data_base import *
import asyncio
import time
import datetime

# === database ===

token = check_token_bot(db.read_token())
bot = Bot(token)
dp = Dispatcher()

# === Command ===
@dp.message(Command('start'))
async def start(message: types.Message):
    user = message.from_user
    x = message.chat.type
    id,fname,user_name,language,prem = user.id,user.first_name,user.username,user.language_code,user.is_premium
    if prem is None:
        is_prem = " ❌ خیر "
    else:
        is_prem = ' ✅ بله'
    text = check_type_info_handle(x,id,fname,user_name,language,is_prem)
    if text is None:
        return
    else:
        txt = text
    await message.answer(txt,parse_mode='HTML',reply_markup=start_menu())

@dp.message(Command('get_id'))
async def get_id(message: types.Message):
    chat_id = message.chat
    id = chat_id.id
    name = chat_id.title
    txt = check_type_info_chat(message.chat.type,id,name)
    if txt is None:
        await message.reply(db.read_text('text_eror_infochat'))
        return
    else:
        text = txt
    await message.answer(text,parse_mode='HTML')

# === handle ===
@dp.message(F.text == 'مشخصات من')
async def info_handle(message: types.Message):
    user = message.from_user
    x = message.chat.type
    id,fname,user_name,language,prem = user.id,user.first_name,user.username,user.language_code,user.is_premium
    if prem is None:
        is_prem = " ❌ خیر "
    else:
        is_prem = ' ✅ بله'
    text = check_type_info_handle(x,id,fname,user_name,language,is_prem)
    if text is None:
        return
    else:
        txt = text

    await message.answer(txt,parse_mode='HTML',reply_markup=back_home_menu()) 


@dp.message(F.text == 'راهنما')
async def help_handle(message: types.Message):
    x = message.chat.type
    a = check_type_help(x)
    await message.answer(a)

@dp.message(F.text == '• بازگشت به منوی اصلی •')
async def back_home_handle(message: types.Message):
    text = check_type_back_home(message.chat.type)
    if text is None:
        return
    else:
        txt = text
    await message.answer(txt,reply_markup=start_menu())

async def main():
    time_now = datetime.datetime.now()
    print('wait for checking token...')
    time.sleep(3)
    print('''====== Robot is runing ======
    type ctrl + c for off the bot''')
    x = db.read_admin()
    await bot.send_message(x,f'Robot is Runing !\n{time_now}\n/start')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())