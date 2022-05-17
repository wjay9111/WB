import sqlite3 as sq
from createbot import dp, bot
from aiogram import types

def sql_start():
	global base, cur
	base = sq.connect('database.db')
	cur = base.cursor()
	if base:
		print('Data Base connected!')
	base.execute('CREATE TABLE IF NOT EXISTS content(token TEXT, user_id TEXT PRIMARY KEY)')
	
	base.commit()