import requests
from support_scripts import get_file_extension, download_image
import os
import argparse
from dotenv import load_dotenv

def get_nasa_apod(api_key, directory):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": api_key,
        "count": 20
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    links_images = response.json()

    for index, link in enumerate(links_images):
        if link.get("media_type") != "image":
            continue
        
        image_url = link.get("url")
        if not image_url:
            continue

        file_extension = get_file_extension(image_url)
        if file_extension.lower() not in [".jpg", ".jpeg", ".png", ".gif"]:
            continue

        filename = f'nasa_apod_{index}{file_extension}'
        download_image(image_url, filename, directory)


def main():
    load_dotenv()
    api_key = os.environ["NASA_API_KEY"]

    parser = argparse.ArgumentParser(
        description="Программа скачивает 20 случайных изображений из архива APOD"
    )
    parser.add_argument('-d', '--directory', help='Путь сохранения',
                        default="images", type=str)
    args = parser.parse_args()

    get_nasa_apod(api_key, args.directory)

if __name__ == "__main__":
    main()