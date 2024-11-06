import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козерог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Рыбы"
    return None

def create_main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    btn2 = types.KeyboardButton("Задать вопрос")
    btn3 = types.KeyboardButton("Определить знак зодиака")
    markup.add(btn1, btn2, btn3)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    markup = create_main_keyboard()
    bot.send_message(
        message.chat.id,
        text="Привет, {0.first_name}! Выбери какую-нибудь кнопку-команду".format(message.from_user),
        reply_markup=markup
    )

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Поздороваться":
        bot.send_message(message.chat.id, text="Привет! Я бот-помощник Даниела")
    
    elif message.text == "Задать вопрос":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как тебя зовут?")
        btn2 = types.KeyboardButton("Что ты можешь?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif message.text == "Как тебя зовут?":
        bot.send_message(message.chat.id, "Меня зовут DannyBot")
    
    elif message.text == "Что ты можешь?":
        bot.send_message(message.chat.id, text="Поздороваться, ответить на вопросы, определить ваш знак зодиака")

    elif message.text == "Определить знак зодиака":
        bot.send_message(message.chat.id, "Пожалуйста, введи свою дату рождения в формате дд.мм")

    elif message.text == "Вернуться в главное меню":
        markup = create_main_keyboard()
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif "." in message.text and len(message.text) == 5:
        try:
            day, month = map(int, message.text.split('.'))
            if 1 <= day <= 31 and 1 <= month <= 12:
                sign = get_zodiac_sign(day, month)
                if sign:
                    bot.reply_to(message, f"Твой знак зодиака: {sign}!")
                else:
                    bot.reply_to(message, "Пожалуйста, введи реальную дату (дд.мм)")
            else:
                bot.reply_to(message, "Пожалуйста, введи реальную дату (дд.мм)")
        except ValueError:
            bot.reply_to(message, "Пожалуйста, введи реальную дату (дд.мм)")
    
    else:
        bot.send_message(message.chat.id, text="Пожалуйста, введи реальную дату (дд.мм)")

bot.polling(none_stop=True)
