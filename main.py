import aiogram
from aiogram.utils import executor
from createbot import dp, bot
from DataBase import db



async def on_startup(_):
	print('Бот вышел в онлайн')
	await bot.send_message(chat_id=admin.ADMIN_ID, text=emojize('Я онлайн, и готов работать :wink: /start'))
	sqlite_db.sql_start()


from clients import client

client.register_handlers_client(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)