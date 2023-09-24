from decouple import config
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from film_names import films
import random

bot = telebot.TeleBot(config('TOKEN'))


@bot.message_handler(commands=['start', 'привет'])
def get_hello(message):
    text = f'привет {message.from_user.first_name} !!! Добро пожаловать, выберите жанр который вас интерисует'
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in films:
        button = KeyboardButton(i.get('genre'))
        markup.add(button)
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(content_types=["text"])
def get_films(message):
    markup = InlineKeyboardMarkup(row_width=2)
    for i in films:
        if i.get("genre") == message.text:
            my_film = random.choice(i.get("films"))
            button2 = InlineKeyboardButton(text=my_film.get('title'), url=my_film.get('link'))
            markup.add(button2)
    text = f"<b>Я рекомендую вам фильм {my_film.get('title')} c рейтингом {my_film.get('rating')} " \
           f"перейдите по ссылке приятного просмотра!!!</b>"
    bot.reply_to(message, text, parse_mode='html', reply_markup=markup)

bot.polling()