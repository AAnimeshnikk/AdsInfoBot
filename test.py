import telebot
from telebot import types

bot = telebot.TeleBot("1215604656:AAE7UN3I5GCUwixjdJ1soFzHwXK7Yw16B5Y")

@bot.message_handler(commands=['start'])
def main(message):
    chat_id = message.from_user.id
    bot.send_message(chat_id, message)
bot.polling(none_stop = True)
