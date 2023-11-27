import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from api import txt

BOT_TOKEN = '6661365099:AAFNVoAa3-WiGqKk4zpvb_tcvX2A203Wbu0'
# BOT_NAME = '@YeshaTestBot' 

dispatcher = Dispatcher()

# Command Handler
@dispatcher.message(CommandStart)
async def welcome(message: types.Message):
	# reply_txt = f'Hi, {hbold(message.from_user.first_name)}!!! \nWelcome to our bot. Please enter your Company Email'
	
	await message.answer(f'Hi, {hbold(message.from_user.first_name)}!!! {txt()}')

# @dispatcher.message(CommandBtn)
# async def on_text(message: types.Message):
# 	btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("First Button"))

# 	await message.answer(message.from_user.id, message.text, reply_markup=btn)

async def main():
	bot = Bot(token=BOT_TOKEN, parse_mode='HTML')

	await dispatcher.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main()) 
	