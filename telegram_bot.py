import os
from telegram import Bot
from telegram.constants import ParseMode

BOT = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def bot_send(text):
    await BOT.send_message(chat_id=CHAT_ID, text=text, parse_mode=ParseMode.HTML)
