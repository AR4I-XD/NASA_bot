import requests
import datetime
import os
from support_scripts import get_file_extension, download_image
import argparse
from dotenv import load_dotenv
from urllib.parse import urlencode
load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")

def GET_NASA_EPIC(NASA_API_KEY):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {
        "api_key": NASA_API_KEY
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images_info = response.json()

    parser = argparse.ArgumentParser(
        description="Программа скачивает 20 случайных изображений из архива APOD"
    )
    parser.add_argument('-d', '--directory', help='Путь сохранения',
                        default="images", type=str)

    args = parser.parse_args()

    for index, info in enumerate(images_info):
        image_name = info["image"]
        date = datetime.datetime.fromisoformat(info["date"])
        date = date.strftime("%Y/%m/%d")
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_name}.png" + "?" + urlencode(payload)
        file_extension = get_file_extension(image_url)
        filename = f'nasa_epic_{index}{file_extension}'
        download_image(image_url, filename, args.directory)

GET_NASA_EPIC(NASA_API_KEY)