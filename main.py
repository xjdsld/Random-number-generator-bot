import random
import telebot
import sqlite3

bot = telebot.TeleBot('')
random_number = None
counter = 0
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, random_numbers INTEGER, tries INTEGER DEFAULT 0)""")
connection.commit()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    global random_number
    random_number = random.randint(1, 100)
    cursor.execute(""" INSERT OR REPLACE INTO users (id, random_numbers) VALUES (?, ?) """, (chat_id, random_number))
    connection.commit()
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
    global counter
    counter += 1
    if user_number == random_number:
        bot.send_message(chat_id, 'The number is correct!')
    elif user_number < random_number:
        bot.send_message(chat_id, 'The number is too low!')
    elif user_number > random_number:
        bot.send_message(chat_id, 'The number is too high!')
    cursor.execute("UPDATE users SET tries = ? WHERE id = ?", (counter, chat_id))
    connection.commit()

@bot.message_handler(commands=['again'])
def is_again(message):
    global random_number
    random_number = random.randint(1, 100)
    bot.send_message(message.chat.id, 'Please enter a number inbetween 1 and 100')

bot.polling()
