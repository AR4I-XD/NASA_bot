import requests
import os
import urllib

def get_file_extension(file_url):
    encoded = urllib.parse.unquote(file_url)
    url_parts = urllib.parse.urlsplit(encoded)
    path = url_parts.path
    file_path, file_extension = os.path.splitext(path)
    return file_extension


def download_image(url, filename, directory):
    os.makedirs(directory, exist_ok=True)
    filename = os.path.join(directory, filename)
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def send_file(path, tg_chat_id, bot):
    with open(path, 'rb') as file:
        bot.send_photo(chat_id=tg_chat_id, photo=file)