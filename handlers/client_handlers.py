from aiogram import types, Dispatcher
from create_bot import bot
from aiogram.dispatcher.filters import Text
from database.sqlite_db import db


waiting_for_message = []

def is_int(text):
    try:
        val = int(text)
        return True
    except ValueError:
        return False

async def start_command(message: types.Message):
    user = message.from_user.id
    users = []
    for m in db.get_users():
        users.append(m[0])
    if user not in users:
        db.add_user(user_id=message.from_user.id, nickname=message.from_user.username)
        await bot.send_message(message.from_user.id, 'Приветствую! 👋\nЗдесь вы можете пройти регистрацию на бесплатный онлайн вебинар.')
        await bot.send_message(message.from_user.id, 'Как вас зовут?')

async def send_notif(message: types.Message):
    admins = []
    for user in db.get_admins():
        admins.append(user[0])
    if message.from_user.id in admins:
        db.set_waiting(message.from_user.id, 1)
        await bot.send_message(message.from_user.id, 'Пришли текст оповещения')

async def no_type_message(message: types.Message):
    # Призваивание переменной user значение id пользователя для дальнейшега удобства в использовании
    user = message.from_user.id
    users = []
    for m in db.get_users():
        users.append(m[0])

    admins = []
    for admin in db.get_admins():
        admins.append(admin[0])
    if user in admins:
        if db.get_waiting(user)[0] == 1:
            db.set_waiting(user, 0)
            for bot_user in users:
                await bot.send_message(bot_user, message.text)
            await bot.send_message(user, 'Сообщение успешно разослано пользователям!')

    if user in users and db.get_name(user)[0] == None:
        db.set_name(user, message.text)
        await bot.send_message(message.from_user.id, 'Приятно познакомиться! Подскажи, сколько тебе лет?')
    elif user in users and db.get_name(user)[0] != None and db.get_age(user)[0] == None:
        if is_int(message.text):
            db.set_age(user, int(message.text))
            await bot.send_message(message.from_user.id, 'Регистрация прошла успешно!')
            await bot.send_message(message.from_user.id, 'https://t.me/+n4Vp4UpZJgs4ZDAy')
        else:
            await bot.send_message(message.from_user.id, 'Я тебя не понял. Пришли мне свой возраст числом.')
    


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(send_notif, commands=['send'])
    dp.register_message_handler(no_type_message, content_types=['text'])