
import telebot
import random 
from env import TOKEN


bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1, button2)



@bot.message_handler(commands=['start', 'hi'])
def start_function(message):
    msg = bot.send_message(message.chat.id, f'Привет {message.chat.first_name} начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, answer_check)
#     bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI2WWIZxS0lQqw9RPzcAQi-4KJgEM33AAJuBQACP5XMCoY62V2IvLc1IwQ')
#     bot.send_photo(message.chat.id, 'https://dataenginer.ru/wp-content/uploads/2020/11/Dm6ice0.png')


def answer_check(msg):
    if msg.text == 'Да':
        bot.send_message(msg.chat.id, 'у тебя есть 3 попытки угадать число от 1 до 10')
        random_number = random.randint(1, 10)
        p = 3
        start_game(msg, random_number, p)
    else:
        bot.send_message(msg.chat.id, 'Ну и ладно!')
        
def start_game(msg, random_number, p):
    msg = bot.send_message(msg.chat.id, 'Введи число от 1 до 10: ')
    bot.register_next_step_handler(msg, check_func, random_number, p-1)

def check_func(msg, random_number, p):
    if msg.text == str(random_number):
        bot.send_message(msg.chat.id, 'Вы победили!')
    elif p == 0:
        bot.send_message(msg.chat.id, f'Вы проиграли! Число было - {random_number}')
    else:
        bot.send_message(msg.chat.id, f'Попробуй еще раз, у тебя осталось {p} попыток')
        start_game(msg, random_number, p)


# @bot.message_handler()
# def echo_all(message):
#     bot.send_message(message.chat.id, message.text)



bot.polling() 

