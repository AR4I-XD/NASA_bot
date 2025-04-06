import requests
import os
import urllib

def get_file_extension(file_url):
    encoded = urllib.parse.unquote(file_url)
    url_parts = urllib.parse.urlsplit(encoded)
    path = url_parts.path
    file_path, file_extension = os.path.splitext(path)
    return file_extension


def download_image(url, filename):
    DIRECTORY = "images"
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    filename = os.path.join(DIRECTORY, filename)
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)