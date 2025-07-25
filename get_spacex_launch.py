import requests
import os
from support_scripts import get_file_extension, download_image
import argparse


def get_spacex_launch(launch_id: str, directory: str):
    os.makedirs(directory, exist_ok=True)

    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    
    for index, url in enumerate(links):
        file_extension = get_file_extension(url)
        filename = f'spacex{index}{file_extension}'
        download_image(url, filename, directory)


def main():
    parser = argparse.ArgumentParser(
        description='Можно получить фото запуска SpaceX по id запуска'
    )
    parser.add_argument('-id', help='ID запуска', nargs='?', default='latest')

    parser.add_argument('-d', '--directory', help='Путь сохранения',
                        default="images", type=str)
    
    args = parser.parse_args()

    get_spacex_launch(args.id, args.directory)


if __name__ == "__main__":
    main()
