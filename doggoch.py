import requests
import json
import IDs
import sendImage
from time import time, sleep

while True:
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    jsonobj = json.loads(response.text)
    url = jsonobj["message"]
    print(url)
    img_data = requests.get(url).content
    with open(IDs.PHOTO_PATH, 'wb') as handler:
        handler.write(img_data).imag
    sendImage.send_photo(IDs.TELEGRAM_CHAT_ID, open(IDs.PHOTO_PATH, 'rb'))
    sleep(1*60*60*24)        # repeat after 24 hours







