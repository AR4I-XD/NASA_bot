import requests
import datetime
import os
from support_scripts import get_file_extension, download_image
import argparse
from dotenv import load_dotenv
from urllib.parse import urljoin
from requests import Request, exceptions

def get_nasa_epic(api_key, directory):
    base_api_url = "https://api.nasa.gov/EPIC/api/natural/images"
    archive_base_url = "https://api.nasa.gov/EPIC/archive/natural/"
    params = {
        "api_key": api_key
        }

    response = requests.get(base_api_url, params=params)
    response.raise_for_status()
    images_info = response.json()

    for index, info in enumerate(images_info):
        image_name = info["image"]
        date = datetime.datetime.fromisoformat(info["date"])
        formatted_date = date.strftime("%Y/%m/%d")
        image_path = f"{formatted_date}/png/{image_name}.png"

        prep = Request(
            method='GET',
            url=urljoin(archive_base_url, image_path),
            params=params
        ).prepare()
        image_url = prep.url

        file_extension = get_file_extension(image_url)
        filename = f'nasa_epic_{index}{file_extension}'

        try:
            download_image(image_url, filename, directory)
        except exceptions.RequestException as req_err:
            print(f"Сетевая ошибка при скачивании {image_url}: {req_err}")
        except OSError as os_err:
            print(f"Ошибка файловой системы при сохранении {filename}: {os_err}")

if __name__ == "__main__":
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser(
        description="Программа скачивает изображения из архива EPIC"
    )
    parser.add_argument('-d', '--directory', help='Путь сохранения',
                        default="images", type=str
    )
    args = parser.parse_args()

    get_nasa_epic(nasa_api_key, args.directory)
