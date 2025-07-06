import telegram
import os
from dotenv import load_dotenv
import random
import time
import argparse
from support_scripts import send_file

def main():
    load_dotenv()
    tg_api_token = os.environ["TG_API_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]
    tg_time_delay = os.getenv("TG_TIME_DELAY", "4")
    parser = argparse.ArgumentParser(
        description="Программа отправляет случайное фото из указанной папки"
    )
    parser.add_argument('-d', '--directory', help='Папка с изображениями',
                        default="images", type=str)

    args = parser.parse_args()
    bot = telegram.Bot(token=tg_api_token)

    images = os.listdir(args.directory)
    random.shuffle(images)
    
    for img in images:
        send_file(os.path.join(args.directory, img), tg_chat_id, bot)
        time.sleep(int(tg_time_delay) * 3600)

if __name__ == "__main__":
    main()
