import telebot
from telebot import types

linkVK = "Ссылка"
linkTG = "Ссылка"
linkWA = "Ссылка"

token = "Ваш токен "

bot = telebot.TeleBot(token, parse_mode=False)

global user_state
user_state = {}

@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_id = message.from_user.id
    print(user_id)
    user_state[user_id] = "pool"
    markup = types.InlineKeyboardMarkup()
    butn1 = types.InlineKeyboardButton("Vk", url=linkVK)
    butn2 = types.InlineKeyboardButton("Telegram", url=linkTG)
    butn3 = types.InlineKeyboardButton("WhatsApp", url=linkWA)
    markup.row(butn1 , butn2, butn3)
    bot.reply_to(message, "Привет , вот ссылки для связи со мной !", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def unknown(message):
    user_id = message.from_user.id
    print(user_id)
    print(user_state)
    if user_id in user_state and (user_state[user_id] == "pool" or user_state[user_id] == "") or (user_id not in user_state):
        markup = types.InlineKeyboardMarkup()
        butn1 = types.InlineKeyboardButton("Vk", url=linkVK)
        butn2 = types.InlineKeyboardButton("Telegram", url=linkTG)
        butn3 = types.InlineKeyboardButton("WhatsApp", url=linkWA)
        markup.row(butn1, butn2, butn3)
        bot.reply_to(message , text = "Я вас не понимаю, пожалуйста нажмите кнопки, чтобы связаться со мной !",reply_markup = markup)

bot.infinity_polling()