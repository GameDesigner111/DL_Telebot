import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()

TG_TOKEN = os.getenv('TG_TOKEN')
bot = telebot.TeleBot(TG_TOKEN)
isTherePoints = False


@bot.message_handler(commands=["start"])
def start(message):
    driving_completed = False
    markup = types.InlineKeyboardMarkup()
    wake_up = types.InlineKeyboardButton(text="ПРОСНУТЬСЯ", callback_data="wake_up")
    markup.add(wake_up)
    bot.send_message(message.chat.id, "Начало", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def delete_message(message):
    bot.delete_message(message.chat.id, message.message_id)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    markup1 = types.InlineKeyboardMarkup()
    go_to_storage = types.InlineKeyboardButton(text="ВЫЕХАТЬ НА СКЛАД", callback_data="go_to_storage")
    markup1.add(go_to_storage)

    markup2 = types.InlineKeyboardMarkup()
    arrive_to_storage = types.InlineKeyboardButton(text="ПРИБЫТЬ НА СКЛАД", callback_data="arrive_to_storage")
    markup2.add(arrive_to_storage)

    markup3 = types.InlineKeyboardMarkup()
    load = types.InlineKeyboardButton(text="ПОГРУЗИТЬСЯ", callback_data="load")
    markup3.add(load)

    markup4 = types.InlineKeyboardMarkup()
    say_address = types.InlineKeyboardButton(text="СООБЩИЛИ АДРЕС", callback_data="say_address")
    markup4.add(say_address)

    markup5 = types.InlineKeyboardMarkup()
    arrive_to_point = types.InlineKeyboardButton(text="ПРИБЫТЬ НА ТОЧКУ", callback_data="arrive_to_point")
    markup5.add(arrive_to_point)

    markup6 = types.InlineKeyboardMarkup()
    unload = types.InlineKeyboardButton(text="РАЗГРУЗИТЬСЯ", callback_data="unload")
    markup6.add(unload)

    markup7 = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text="ДА", callback_data="yes")
    no = types.InlineKeyboardButton(text="НЕТ", callback_data="no")
    markup7.add(yes, no)

    markup8 = types.InlineKeyboardMarkup()
    complete_driving = types.InlineKeyboardButton(text="ЗАВЕРШИТЬ РЕЙС", callback_data="complete_driving")
    markup8.add(complete_driving)

    markup9 = types.InlineKeyboardMarkup()
    arrive_to_storage1 = types.InlineKeyboardButton(text="ПРИБЫТЬ НА СКЛАД", callback_data="1arrive_to_storage")
    markup9.add(complete_driving)

    if call.data == "wake_up":
        bot.edit_message_text("Вы проснулись", call.message.chat.id, call.message.message_id, reply_markup=markup1)
    elif call.data == "go_to_storage":
        bot.edit_message_text("Вы выехали на склад", call.message.chat.id, call.message.message_id, reply_markup=markup2)
    elif call.data == "arrive_to_storage":
        bot.edit_message_text("Вы прибыли на склад", call.message.chat.id, call.message.message_id, reply_markup=markup3)
    elif call.data == "load":
        bot.edit_message_text("Вы погрузились", call.message.chat.id, call.message.message_id, reply_markup=markup4)
    elif call.data == "say_address":
        bot.edit_message_text("Вам сообщили адрес", call.message.chat.id, call.message.message_id, reply_markup=markup5)
    elif call.data == "arrive_to_point":
        bot.edit_message_text("Вы прибыли на точку", call.message.chat.id, call.message.message_id, reply_markup=markup6)
    elif call.data == "unload":
        bot.edit_message_text("Есть еще адрес?", call.message.chat.id, call.message.message_id, reply_markup=markup7)
    elif call.data == "yes":
        bot.edit_message_text("Вам сообщили адрес?", call.message.chat.id, call.message.message_id, reply_markup=markup5)
    elif call.data == "no":
        bot.edit_message_text("Точек больше нет", call.message.chat.id, call.message.message_id, reply_markup=markup8)
        bot.send_message(call.message.chat.id, text="", reply_markup=markup8)
    elif call.data == "complete_driving":
        bot.send_message(call.message.chat.id, text="Рейс завершен")


bot.polling(none_stop=True)

