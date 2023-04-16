import requests
import re
import random

# Send GET request to Abstruse Goose homepage to retrieve HTML content
response = requests.get('https://abstrusegoose.com/')
html_content = response.text

# Use regex to find URLs of comic images on the homepage
regex = r'https://abstrusegoose\.com/strips/.*?\.(?:png|jpg|jpeg|gif)'
matches = re.findall(regex, html_content)

# Choose a random comic image URL
random_comic_url = random.choice(matches)

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
      img.src = "{random_comic_url}";
      document.getElementById("comic-link").href = img.src;
    </script>
  </head>
  <body>
    <a id="comic-link" href=""><img id="comic" src="" alt="Abstruse Goose Comic" /></a>
  </body>
</html>
'''

with open('index.html', 'w') as f:
    f.write(html_text)
