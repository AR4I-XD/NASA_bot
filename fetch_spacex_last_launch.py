import requests
import os
from support_scripts import *
import argparse


def fetch_spacex_last_launch(args):      
    if not os.path.exists('images'):
        os.makedirs('images')

    url = f"https://api.spacexdata.com/v5/launches/{args.id}"
    
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    
    for index, url in enumerate(links):
        file_extension = get_file_extension(url)
        filename = f'spacex{index}{file_extension}'
        download_image(url, filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Можно получить фото запуска SpaceX по id запуска')
    parser.add_argument('id', help='ID запуска', nargs='?', default='latest')
    args = parser.parse_args()
    fetch_spacex_last_launch(args)