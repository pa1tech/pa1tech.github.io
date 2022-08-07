#https://medium.com/reflash-programming-adventures/python-telegram-games-aiogram-172e238582d3
#https://core.telegram.org/bots/games
#https://core.telegram.org/bots/api#inlinequeryresultgame

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultGame
from uuid import uuid4

TOKEN=""
bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()

@bot.callback_query_handler(lambda callback_query: callback_query.game_short_name == "tin")
def callback_query(callback_query):
	bot.answer_callback_query(callback_query.id,url="https://core.telegram.org/bots/games")

@bot.inline_handler(lambda query: len(query.query)>0)
def message_handler(inline_query):
	keyboard_markup = InlineKeyboardMarkup()
	keyboard_markup.add(InlineKeyboardButton(text="PLay!",callback_game="tin"))
	keyboard_markup.add(InlineKeyboardButton(text="PLgay!",url="https://core.telegram.org/bots/games"))
	bot.answer_inline_query(inline_query.id,
                                  [InlineQueryResultGame(id=str(uuid4()), 
                                                         game_short_name="tin",reply_markup=keyboard_markup)])

bot.infinity_polling()