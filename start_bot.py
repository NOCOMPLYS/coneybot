from aiogram.utils import executor
from create_bot import dp
from aiogram.utils.executor import start_webhook
from handlers import client_handlers
#import asyncio, aioschedule


async def on_startup(_):
    print('The bot has been successfully launched')


async def on_shutdown(_):
    await dp.storage.close()
    await dp.storage.wait_closed()
    print('The bot has been successfully shut down')

client_handlers.register_client_handlers(dp=dp)
#admin_handlers.register_admin_handlers(dp=dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)