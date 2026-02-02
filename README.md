Random Number Telegram Bot

A simple Telegram bot where users guess a random number between 1 and 100. Tracks attempts in a SQLite database.

Commands

/start — Start the game and generate a random number.

/again — Generate a new number to play again.

Features

Gives feedback: "too low", "too high", or "correct".

Tracks number of tries per user in database.db.

Supports multiple users simultaneously.

Setup

Install dependencies: pip install pyTelegramBotAPI

Replace YOUR_API_TOKEN_HERE with your Telegram bot token.

Run the bot: python your_bot_file.py
