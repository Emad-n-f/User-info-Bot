from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
from data_base import db
import asyncio


def start_menu(id):
    owner_id = db.read_admin()
    btn_panel = KeyboardButton(text='پنل مدیریت')
    btn_help = KeyboardButton(text='راهنما',style='danger',icon_custom_emoji_id="5452069934089641166")
    btn_info = KeyboardButton(text='مشخصات من',style='primary',icon_custom_emoji_id="5260399854500191689")
    if id in owner_id:
        start_key = ReplyKeyboardMarkup(
            keyboard=[[btn_help,btn_info],[btn_panel]],resize_keyboard=True)
    else:
        start_key = ReplyKeyboardMarkup(
            keyboard=[[btn_help,btn_info]],resize_keyboard=True)
    return start_key

def back_home_menu():
    btn_back = KeyboardButton(text='• بازگشت به منوی اصلی •',style='success')
    back_home_key = ReplyKeyboardMarkup(
        keyboard=[[btn_back]],resize_keyboard=True)
    return back_home_key

def panel_menu():
    btn_statistics = InlineKeyboardButton(text='📊 آمار کاربران ربات',style='success',callback_data='test2')
    btn_change_text = InlineKeyboardButton(text='📋 متن های ربات',style='primary',callback_data='test2')
    btn_change_button = InlineKeyboardButton(text='💠 دکمه های ربات',style='primary',callback_data='test2')
    btn_settings = InlineKeyboardButton(text='⚙ تنظیمات ربات',style='danger',callback_data='settings')
    btn_user_management =  InlineKeyboardButton(text='👤 مدیریت کاربران',style='danger',callback_data='test2')
    btn_back = InlineKeyboardButton(text='• بازگشت به منوی اصلی •',callback_data='back_home')

    panel_key = InlineKeyboardMarkup(
        inline_keyboard=[[btn_statistics],[btn_change_text,btn_change_button],[btn_settings,btn_user_management],[btn_back]])
    return panel_key

def setting_menu():
    btn_status = InlineKeyboardButton(text='⚙ وضعیت ربات',callback_data='test2')
    btn_backup = InlineKeyboardButton(text='📥 دریافت بکاپ ربات',callback_data='backup')
    btn_back_panel_menu = InlineKeyboardButton(text='• بازگشت به منوی اصلی •',callback_data='back_panel_menu')

    setting_key = InlineKeyboardMarkup(
        inline_keyboard=[[btn_status],[btn_backup],[btn_back_panel_menu]])
    return setting_key

def back_panel_menu():
    btn_back_panel_menu = InlineKeyboardButton(text='• بازگشت به منوی اصلی •',callback_data='back_panel_menu')

    back_home_key = InlineKeyboardMarkup(
        inline_keyboard=[[btn_back_panel_menu]])
    return back_home_key