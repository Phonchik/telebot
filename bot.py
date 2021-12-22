import telebot
import config
import random

from telebot import types

a = int(input())

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Сгенерировать пароль")

    markup.add(item1,)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ бот для генерации пароля".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    pas = None
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            for x in range(a):  # Количество символов
                pas = pas + random.choice(list(
                    '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))  # Символы, из которых будет составлен пароль
            print('Ваш пароль: ', pas)

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


# RUN
bot.polling(none_stop=True)
