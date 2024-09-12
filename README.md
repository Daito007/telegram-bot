# Telegram Image Hash Bot

This is a simple Telegram bot that allows users to send .jpg or .jpeg images, and it responds with the MD5 hash of the image file. The bot is built using Python and the Telethon library.

## Features

- Responds to the /start command with a welcome message.
- Calculates the MD5 hash of .jpg and .jpeg image files sent to the bot.
- Responds with an error message for unsupported file types or non-media messages.

## Prerequisites

Make sure you have the following installed on your machine:

- Python 3.8+
- [Telethon](https://docs.telethon.dev/) library for interacting with the Telegram API.
- [dotenv](https://pypi.org/project/python-dotenv/) for loading environment variables.

## Setup

### 1. Clone the Repository

git clone https://github.com/Daito007/telegram-bot.git
cd telegram-bot


### 2.⁠Install the Dependencies
You can install the required Python libraries using the requirements.txt file.

pip install -r requirements.txt
The requirements.txt file should include:


telethon
python-dotenv

## 3.⁠Create a .env File
Create a .env file in the project directory with the following content:
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token


You can obtain these credentials by creating a bot on Telegram via BotFather and registering an app on the Telegram API site.
⁠Run the Bot

## 4.To start the bot, run the following command:
python main.py
You should see Bot is running... in the terminal, indicating the bot is active.

## 5.Usage
Start a chat with the bot in Telegram.
Type /start to receive a welcome message.
Send a .jpg or .jpeg image to the bot.
The bot will respond with the MD5 hash of the image.
If you send an unsupported file or text, the bot will notify you.

Example
/start: Responds with a welcome message.
Send an image: The bot responds with the MD5 hash of the image.
Send unsupported files or text: The bot responds with an error message.