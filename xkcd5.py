import requests
import random
import webbrowser

# Send GET request to XKCD API to retrieve information about the latest comic
response = requests.get('https://xkcd.com/info.0.json')
data = response.json()
latest_comic_number = data['num']

# Generate a random comic number between 1 and the latest comic number
random_comic_number = random.randint(1, latest_comic_number)

# Send GET request to XKCD API to retrieve information about the random comic
response = requests.get(f'https://xkcd.com/{random_comic_number}/info.0.json')
data = response.json()

# Resize the image to fit in a 382pt x 382pt box while maintaining aspect ratio
response = requests.get(data['img'])
img_bytes = response.content
with open('temp_image.png', 'wb') as f:
    f.write(img_bytes)

from PIL import Image
im = Image.open('temp_image.png')
im.thumbnail((382, 382))
im.save('temp_image.png')

# Create HTML file to display the random comic
with open('random_xkcd.html', 'w') as f:
    f.write(f'<html><body><img src="temp_image.png" alt="{data["alt"]}" width="{im.width}" height="{im.height}"></body></html>')

# Open the HTML file in the default web browser
webbrowser.open('random_xkcd.html')
