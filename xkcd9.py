import requests
import random

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
    f.write('<html><head>')
    f.write('<script>')
    f.write('const img = new Image();')
    f.write('img.onload = function() {')
    f.write('const imgWidth = img.width;')
    f.write('const imgHeight = img.height;')
    f.write('let newWidth, newHeight;')
    f.write('if (imgWidth > imgHeight) {')
    f.write('newWidth = 382;')
    f.write('newHeight = Math.round((imgHeight / imgWidth) * newWidth);')
    f.write('} else {')
    f.write('newHeight = 382;')
    f.write('newWidth = Math.round((imgWidth / imgHeight) * newHeight);')
    f.write('}')
    f.write('document.getElementById("comic").src = img.src;')
    f.write('document.getElementById("comic").width = newWidth;')
    f.write('document.getElementById("comic").height = newHeight;')
    f.write('};')
    f.write(f'img.src = "{data["img"]}";')
    f.write('document.getElementById("comic-link").title = "BREAKING: Senator\'s bold pro-podium stand leads to primary challenge from prescriptivist base."')
    f.write('</script>')
    f.write('</head><body>')
    f.write(f'<a id="comic-link" href="{data["img"]}"><img id="comic" src="" alt="{data["alt"]}" /></a>')
    f.write('</body></html>')
