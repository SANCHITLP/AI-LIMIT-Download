import telebot
import requests
import telebot.types as types
import wget
import os
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot('6222084445:AAHgtfGJqxGZPZJVI1ockN3ePm8aww8dfK4')
@bot.message_handler(commands=['start'])
def start(message):
    buttons = types.InlineKeyboardMarkup(row_width=2)
    but1 = types.InlineKeyboardButton(text='👨🏻‍💻 Developer', url='https://t.me/SANCHIT_0FFICIAL')
    but2 = types.InlineKeyboardButton(text='🤡 Channel', url='https://t.me/+Q5RcaQe268lmYmI9')
    buttons.add(but1, but2)
    bot.send_message(message.chat.id, text=f"•⚜️ Hii {message.from_user.first_name} \n\n•😘 Welcome To SanchitGPT BOT\n\n•😇 Please Ask Your Questions\n\n•🙇 I Hope Can Help You 👍", reply_to_message_id=message.message_id, reply_markup=buttons)

@bot.message_handler(func=lambda message:True)
def replyy(message):
    message_text = message.text
    req = requests.get(f'https://educatedwindyoctal.66666612.repl.co/By?SD={message.text}').text
    
    headers = {"Host":'educatedwindyoctal.66666612.repl.co', "sec-ch-ua-platform": "Android", "dnt": '1', "upgrade-insecure-requests": '1', "user-agent": 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36', "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', "accept-encoding": 'gzip, deflate, br', "accept-language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7,hi-IN;q=0.6,hi;q=0.5"}
    print(req)
    bot.send_message(message.chat.id, f'<strong>{req}</strong>', parse_mode='html', reply_to_message_id=message.message_id)

bot.infinity_polling()
