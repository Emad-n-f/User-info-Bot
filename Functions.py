from data_base import *
import datetime
#______ Functions ______

def check_token_bot(x):
    time = datetime.datetime.now()
    if x is None:
        token = input(''' ***  Wellcome  *** 
Please enter your bot token : ''')
        owner = int(input('Send chat id owner(just send) : '))
        db.inser_infobot(token,time,'Active',owner)
        return token
    else:
        return x


# بررسی ایدی عددی برای تشخیص ادمین بودن
def is_admin(id):
    admins = db.read_admin()
    if id in admins:
        return True
    else:
        return False
# بررسی نوع چت برای تشخیص چت شخصی
def is_pv(x):
    if x == 'private':
        return True
    else:
        return False

def check_type_help(x):
    if x == 'private':
        text = db.read_text('text_help')
        return text
    else:
        text = "📚 جهت دریافت شناسه عددی گروه ، لطفا کامند /get_id را ارسال نمایید 🌹"
        return text

def check_type_info_handle(x,id_,fname,user_name,language,is_prem):
    
    if x == 'private':
        txt = db.read_text('text_userinfo')
        text = txt.format(id=id_,fname=fname,user_name=user_name,language=language,is_prem=is_prem)
        return text
    else:
        return None

def check_type_back_home(x):
    if x == 'private':
        txt = 'به منوی اصلی بازگشتید'
        return txt
    else:
        return None

def check_type_info_chat(x,id,name):
    if x == 'group' or x == 'channel' or x == 'supergroup':
        txt = db.read_text('text_infochat')
        text = txt.format(id=id,name=name)
        return text
    else:
        return None


