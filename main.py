#
import telebot
import random
# ідентифікатор чату - message.chat.id
# ідентифікатор користувача - message.from_user.id
# ідентифікатор текст повідомлення - message.text
# ідентифікатор першого імені користувача - message.from_user.first_name
# ідентифікатор другого імені користувача - message.from_user.last_name
# ідентифікатор псевдоніму користувача - message.from_user.username

# створюємо об'єкт бота
bot = telebot.TeleBot("5696251180:AAFVyIGVTqrXvlRwObtmezXuC0UUPo_XvsQ")
#
button = telebot.types.KeyboardButton("Play")
#
menu_bar = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
#
menu_bar.add(button)
#
@bot.message_handler(commands=["start"])
#
def start(message):
    bot.send_message(message.chat.id, "Hi User!", reply_markup = menu_bar)
    bot.register_next_step_handler(message, start_play)

def start_play(message):
    if message.text == "Play":
        number = random.randint(1, 6)
        menu_bar1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
        button1 = telebot.types.KeyboardButton("1")
        button2 = telebot.types.KeyboardButton("2")
        button3 = telebot.types.KeyboardButton("3")
        button4 = telebot.types.KeyboardButton("4")
        button5 = telebot.types.KeyboardButton("5")
        button6 = telebot.types.KeyboardButton("6")

        menu_bar1.row(button1, button2)
        menu_bar1.add(button3, button4)
        menu_bar1.add(button5, button6)
        # menu_bar1.add(button4)
        bot.send_message(message.chat.id, "Гру почато! Відгадай число від 1 до 6.", reply_markup = menu_bar1)
        bot.register_next_step_handler(message, win_or_over, number)
        
def win_or_over(message, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, "Відповідь зараховано!")
    else:
        bot.send_message(message.chat.id, "Ви не вгадали(", reply_markup = menu_bar)
        bot.register_next_step_handler(message, start_play)

#
bot.polling()