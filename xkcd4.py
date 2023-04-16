import requests
import random
#import webbrowser

# Send GET request to XKCD API to retrieve information about the latest comic
response = requests.get('https://xkcd.com/info.0.json')
data = response.json()
latest_comic_number = data['num']

# Generate a random comic number between 1 and the latest comic number
random_comic_number = random.randint(1, latest_comic_number)

# Send GET request to XKCD API to retrieve information about the random comic
response = requests.get(f'https://xkcd.com/{random_comic_number}/info.0.json')
data = response.json()

# Create HTML file to display the random comic
with open('index.html', 'w') as f:
    f.write(f'<html><body><img src="{data["img"]}" alt="{data["alt"]}"></body></html>')

# Open the HTML file in the default web browser
#webbrowser.open('random_xkcd.html')
