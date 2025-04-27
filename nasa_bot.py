import telegram
import os
from dotenv import load_dotenv
import random
import time

load_dotenv()
BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
TIME_DELAY = os.getenv("TIME_DELAY")
DIRECTORY = "images"

bot = telegram.Bot(token=BOT_API_TOKEN)

images = os.listdir(DIRECTORY)
random.shuffle(images)
for img in images:
    bot.send_photo(chat_id=CHAT_ID, photo=open(f'images/{img}', 'rb'))
    time.sleep(int(TIME_DELAY)*3600)
