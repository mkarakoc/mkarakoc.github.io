import random
import requests
from bs4 import BeautifulSoup

# The highest XKCD comic number available
maxComicNum = 2500

# Choose a random comic number
randomComicNum = random.randint(1, maxComicNum)

# Retrieve the XKCD comic page
url = f"https://xkcd.com/{randomComicNum}"
response = requests.get(url)

# Parse the HTML response
soup = BeautifulSoup(response.text, "html.parser")
comicElement = soup.find(id="comic")
comicImg = comicElement.find("img")

# Get the comic image URL and alt text
comicUrl = f"https:{comicImg['src']}"
comicTitle = comicImg['title']

# Get the image dimensions
response = requests.get(comicUrl)
imgWidth = response.headers['Content-Length']
imgHeight = response.headers['Content-Length']

# Scale down the image while maintaining aspect ratio
newWidth = 382
newHeight = round(float(imgHeight) / float(imgWidth) * newWidth)

# Generate the HTML for the comic image
html = f"""
<!doctype html>
<html>
    <body>
        <a id="comic-link" href="https://xkcd.com/{randomComicNum}" target="_blank" title="{comicTitle}">
            <img id="comic" src="{comicUrl}" alt="{comicTitle}" width="{newWidth}" height="{newHeight}">
        </a>
    </body>
</html>
"""

print(html)
