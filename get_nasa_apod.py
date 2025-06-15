import requests
from support_scripts import get_file_extension, download_image
import os
import argparse
from dotenv import load_dotenv
load_dotenv()

def GET_NASA_APOD():
    NASA_API_KEY = os.getenv("NASA_API_KEY")
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": NASA_API_KEY,
        "count": 20
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    links_images = response.json()

    parser = argparse.ArgumentParser(
        description="Программа скачивает 20 случайных изображений из архива APOD"
    )
    parser.add_argument('-d', '--directory', help='Путь сохранения',
                        default="images", type=str)

    args = parser.parse_args()

    for index, link in enumerate(links_images):
        image_url = link["url"]
        file_extension = get_file_extension(image_url)
        filename = f'nasa_apod_{index}{file_extension}'
        download_image(image_url, filename, args.directory)

GET_NASA_APOD()