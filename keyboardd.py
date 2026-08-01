from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
import asyncio


def start_menu():
    btn_help = KeyboardButton(text='🆘 راهنما')
    btn_info = KeyboardButton(text='💠 مشخصات من')
    start_key = ReplyKeyboardMarkup(
        keyboard=[[btn_help,btn_info]],resize_keyboard=True)
    return start_key

def back_home_menu():
    btn_back = KeyboardButton(text='• بازگشت به منوی اصلی •')
    back_home_key = ReplyKeyboardMarkup(
        keyboard=[[btn_back]],resize_keyboard=True)
    return back_home_key

