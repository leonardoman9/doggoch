import shutil
import requests
import json

import urllib.request

response = requests.get("https://dog.ceo/api/breeds/image/random")
jsonobj = json.loads(response.text)
url = jsonobj["message"]
#print(url)

img_data = requests.get(url).content
with open('currentdoggo.jpg', 'wb') as handler:
    handler.write(img_data).imag
