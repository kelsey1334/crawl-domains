import os
from telegram import Bot

BOT = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def bot_send(text):
    BOT.send_message(chat_id=CHAT_ID, text=text)
