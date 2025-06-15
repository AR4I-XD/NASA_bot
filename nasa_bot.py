import telegram
import os
from dotenv import load_dotenv
import random
import time
import argparse
from support_scripts import send_file


def main():
    load_dotenv()
    TG_API_TOKEN = os.getenv("TG_API_TOKEN")
    TG_CHAT_ID = os.getenv("TG_CHAT_ID")
    TG_TIME_DELAY = os.getenv("TG_TIME_DELAY")
    parser = argparse.ArgumentParser(
        description="Программа отправляет случайное фото из указанной папки"
    )
    parser.add_argument('-d', '--directory', help='Папка с изображениями',
                        default="images", type=str)

    args = parser.parse_args()
    bot = telegram.Bot(token=TG_API_TOKEN)

    images = os.listdir(args.directory)
    random.shuffle(images)
    
    for img in images:
        send_file(os.path.join(args.directory, img), TG_CHAT_ID, bot)
        time.sleep(int(TG_TIME_DELAY)*3600)
main()
