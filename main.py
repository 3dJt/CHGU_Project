import telebot # Библиотека TeleBot
from telebot import types # Для указания типов

token = '7053017827:AAFKlU8JDZLOwO61WTtB5h-VNDR7ZBMHrIE'

bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['test1'])
def firstTest(message):
    bot.reply_to(message, 'Ссылка на викторину 5-7 классов: https://forms.gle/2M6W4o1kKyNRh6rv7')

@bot.message_handler(commands= ['test2'])
def secondTest(message):
    bot.reply_to(message, 'Ссылка на викторину 8-11 классов: https://forms.gle/5V8asbE3xUpJRgcu5')

@bot.message_handler(commands= ['start'])
def start_func(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Викторина 5-7 классов", url='https://forms.gle/2M6W4o1kKyNRh6rv7')
    button2 = types.InlineKeyboardButton("Викторина 8-11 классов", url='https://forms.gle/5V8asbE3xUpJRgcu5')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на нужную кнопку и перейди в викторину.".format(message.from_user), reply_markup=markup)

bot.polling()