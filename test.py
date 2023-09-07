import telebot
from telebot import types
from dotenv import load_dotenv
import os

@bot.messsage_handler()
if __name__ == "__main__":
    load_dotenv()
    TG_TOKEN = os.getenv('TG_TOKEN')
    bot = telebot.TeleBot(TG_TOKEN)
    bot.polling(none_stop=True)
