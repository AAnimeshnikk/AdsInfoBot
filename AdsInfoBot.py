import telebot
from telebot import types
import sqlite3
from bs4 import BeautifulSoup
import requests
import vk_api

vk_session = vk_api.VkApi('+380968417052', '@zhini.net')
vk_session.auth()

vk = vk_session.get_api()

chat_id = ''

conn = sqlite3.connect("AdsInfo.db")
c = conn.cursor()

bot = telebot.TeleBot("1111222606:AAF4xRQz4d846CfQ3ObTzAhIhNLS4-UuxOg")

@bot.message_handler(commands=['start'])
def dadova(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text = '🏦Клиенты🏦', callback_data = 'client')
    btn2 = types.InlineKeyboardButton(text = '💵Рекламодатели💵', callback_data = 'client')
    markup.row(btn1)
    markup.row(btn2)
    bot.send_message(chat_id, text = 'Выберите категорию :', reply_markup = markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'client':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text = '✏️Добавить✏️', callback_data = 'add')
        btn2 = types.InlineKeyboardButton(text = '❌Удалить❌', callback_data = 'delete')
        btn3 = types.InlineKeyboardButton(text = '📖Список📖', callback_data = 'list')
        btn4 = types.InlineKeyboardButton(text = '🔍Найти🔍', callback_data = 'find')
        btn5 = types.InlineKeyboardButton(text = '🔙Назад🔙', callback_data = 'main')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        markup.row(btn5)
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,
        text = 'Выберите действие :', reply_markup = markup
        )


    elif call.data == 'main':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text = '🏦Клиенты🏦', callback_data = 'client')
        btn2 = types.InlineKeyboardButton(text = '💵Рекламодатели💵', callback_data = 'client')
        markup.row(btn1)
        markup.row(btn2)
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Выберите категорию :', reply_markup = markup)

    elif call.data == 'add':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text = '❌Отмена❌', callback_data = 'client')
        markup.row(btn1)
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,
        text = 'Введите ссылку на пользователя : ', reply_markup = markup
        )



        @bot.message_handler(content_types=['text'])
        def send_link(message):
            m = message.text
            if m[:15] == 'https://vk.com/':
                bot.send_message(chat_id = call.message.chat.id, text = 'Верно!')


bot.polling(none_stop = True)
