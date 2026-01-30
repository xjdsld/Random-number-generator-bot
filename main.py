
import random
import telebot
import sqlite3

bot = telebot.TeleBot('')
random_number = None

@bot.message_handler(commands=['start'])
def send_welcome(message):
  chat_id = message.chat.id
  global random_number
  random_number = random.randint(1, 100)
  bot.send_message(chat_id, 'Hello, this is a random number generator. Please enter a number inbetween 1 and 100')

  
def check_user_number(message):
  global random_number
  chat_id = message.chat.id

  if random_number is None:
    bot.send_message(message.chat.id, 'Type /start to begin')
    return

  if not message.text.isdigit():
    bot.send_message(message.chat.id, 'Please send a number')
    return
    
  user_number = int(message.text)
  if user_number == random_number:
    bot.send_message(chat_id, 'The number is correct!')
  elif user_number < random_number:
    bot.send_message(chat_id, 'The number is too low!')
  elif user_number > random_number:
    bot.send_message(chat_id, 'The number is too high!')
    
@bot.message_handler(commands=['again'])
def is_again(message):
  global random_number
  random_number = random.randint(1, 100)
  bot.send_message(message.chat.id, 'Please enter a number inbetween 1 and 100')

    
bot.polling()
