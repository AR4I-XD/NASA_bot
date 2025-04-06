import requests
from support_scripts import *
from dotenv import load_dotenv
load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")

def NASA_APOD(NASA_API_KEY):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": NASA_API_KEY,
        "count": 40
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    links_images = response.json()

    for index, link in enumerate(links_images):
        image_url = link["url"]
        file_extension = get_file_extension(image_url)
        filename = f'nasa_apod_{index}{file_extension}'
        download_image(image_url, filename)

NASA_APOD(NASA_API_KEY)