from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from aiogram.types import CallbackQuery,FSInputFile
from keyboardd import *
from Functions import *
from data_base import *
import asyncio
import datetime

# ======== database ========

token = check_token_bot(db.read_token())
bot = Bot(token)
dp = Dispatcher()

# ========== Command ==========
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
    await message.answer(txt,parse_mode='HTML',reply_markup=start_menu(id))

@dp.message(Command('get_id'))
async def get_id_group(message: types.Message):
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

@dp.channel_post(Command('get_id'))
async def get_id_channel(message: types.Message):
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

# ========== handle ==========

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
    id = message.chat.id
    text = check_type_back_home(message.chat.type)
    if text is None:
        return
    else:
        txt = text
    await message.answer(txt,reply_markup=start_menu(id))


@dp.message(F.text == 'پنل مدیریت')
async def panel_handle(message: types.Message):
    admin = db.read_admin()
    chat_id = message.from_user.id
    chat_type = message.chat.type
    
    if is_admin(chat_id) and is_pv(chat_type) :
        text = db.read_text('text_admin_panel')
        await message.answer(text,reply_markup=panel_menu())
    elif is_admin(chat_id) and is_pv(chat_type) == False:
        return
    elif is_admin(chat_id) == False and is_pv(chat_type):
        text = db.read_text('text_erorr_admin_panel')
        
        await bot.send_message(admin[0],f'''⛔️ کاربر {chat_id} قصد ورود به پنل مدیریت داشت که داخل لیست ادمین ها نبود و ربات اجازه ورود نداد بهش''')
        await message.answer(text,reply_markup=back_home_menu())
    else:
        return
    
# =================== callback Query =======================
@dp.callback_query(F.data == 'test2')
async def update_callback(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('''این بخش در حال بروزرسانی است ♻️
/start''')


@dp.callback_query(F.data == 'back_home')
async def back_home_callback(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer('به منوی اصلی بازگشتید',reply_markup=start_menu(chat_id))


@dp.callback_query(F.data == 'settings')
async def settings_callback(callback: CallbackQuery):
    text = '''⚙ تنظیمات ربات
🗂 از این بخش میتوانید تنظیمات ربات را تغییر دهید و بکاپ خود را دریافت کنید'''
    await callback.answer()
    await callback.message.edit_text(text,reply_markup=setting_menu())
    


@dp.callback_query(F.data == 'back_panel_menu')
async def back_panel_callback(callback: CallbackQuery):
    text = db.read_text('text_admin_panel') 
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer(text,reply_markup=panel_menu())

@dp.callback_query(F.data == 'backup')
async def backup_callback(callback: CallbackQuery):
    file = FSInputFile('database.db')
    text = '📥 بکاپ ربات شما ارسال شد 👇'
    await callback.answer()
    await callback.message.answer_document(document=file)
    await callback.message.edit_text(text,reply_markup=back_panel_menu())

#===================================================
async def main():
    time_now = datetime.datetime.now()
    print('wait for checking token...')
    await asyncio.sleep(1)
    print('''====== Robot is runing ======
    type ctrl + c for off the bot''')
    x = db.read_admin()
    await bot.send_message(x[0],f'Robot is Runing !\n{time_now}\n/start')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())