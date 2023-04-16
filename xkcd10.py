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
html_text = f'''
<html>
  <head>
    <script>
      const img = new Image();
      img.onload = function() {{
        const imgWidth = img.width;
        const imgHeight = img.height;
        let newWidth, newHeight;
        if (imgWidth > imgHeight) {{
          newWidth = 382;
          newHeight = Math.round((imgHeight / imgWidth) * newWidth);
        }} else {{
          newHeight = 382;
          newWidth = Math.round((imgWidth / imgHeight) * newHeight);
        }}
        document.getElementById("comic").src = img.src;
        document.getElementById("comic").width = newWidth;
        document.getElementById("comic").height = newHeight;
      }};
      img.src = "{data["img"]}";
    </script>
  </head>
  <body>
    <a id="comic-link" href="{data["img"]}" target="_blank"><img id="comic" src="" alt=""/></a>
  </body>
</html>
'''

# <a id="comic-link" href="{data["img"]}"><img id="comic" src="" alt="{data["alt"]}" /></a>
# <a id="comic-link" href="{data["img"]}"><img id="comic" src="" alt="" /></a>

with open('index.html', 'w') as f:
    f.write(html_text)
