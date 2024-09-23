from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import asyncio

loop = asyncio.get_event_loop()
bot = Bot(token='7554613342:AAHq7G6wfPpUpNc8TsHCdrffzu4lJ-sJrjo')
dp = Dispatcher(bot)
