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

# Get the aspect ratio of the image
response = requests.get(data['img'])
img_bytes = response.content
from PIL import Image
im = Image.open(BytesIO(img_bytes))
aspect_ratio = im.width / im.height

# Set the maximum width and height of the image
max_width = 382
max_height = 382

# Determine the width and height of the image to fit in a 382pt x 382pt box while maintaining aspect ratio
if aspect_ratio > 1:
    width = min(im.width, max_width)
    height = width / aspect_ratio
else:
    height = min(im.height, max_height)
    width = height * aspect_ratio

# Create HTML file to display the random comic with the resized image
with open('random_xkcd.html', 'w') as f:
    f.write(f'<html><body><img src="{data["img"]}" alt="{data["alt"]}" width="{width}" height="{height}"></body></html>')

# Open the HTML file in the default web browser
webbrowser.open('random_xkcd.html')
