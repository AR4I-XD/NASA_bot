import telegram
import os
from dotenv import load_dotenv

load_dotenv()
BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telegram.Bot(token=BOT_API_TOKEN)
print(bot.get_me())


updates = bot.get_updates()

bot.send_message(text='Helo', chat_id=CHAT_ID)