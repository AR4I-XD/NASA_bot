import requests
import datetime
from support_scripts import *
from dotenv import load_dotenv
load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")

def NASA_EPIC(NASA_API_KEY):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {
        "api_key": NASA_API_KEY
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images_info = response.json()

    for index, info in enumerate(images_info):
        image_name = info["image"]
        date = datetime.datetime.fromisoformat(info["date"])
        date = date.strftime("%Y/%m/%d")
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_name}.png?api_key={NASA_API_KEY}"
        file_extension = get_file_extension(image_url)
        filename = f'nasa_epic_{index}{file_extension}'
        download_image(image_url, filename)

NASA_EPIC(NASA_API_KEY)