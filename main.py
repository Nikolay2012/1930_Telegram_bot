import telebot

# створюємо об'єкт бота
bot = telebot.TeleBot("5696251180:AAFVyIGVTqrXvlRwObtmezXuC0UUPo_XvsQ")
# перевірка повідомленя "start" 
@bot.message_handler(commands=["start"])
# обробка та відповідь на повідомлення 
def bot_start(message):
    # відовідь на повідомлення за конкретною адресою чата
    bot.send_message(message.chat.id, "Hello User!")
# бот чекає команди чати
bot.polling()