import random
import urllib.request
from html.parser import HTMLParser

class XKCDParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.img_src = None
        self.img_alt = None
        self.in_div = False

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for attr in attrs:
                if attr[0] == "id" and attr[1] == "comic":
                    self.in_div = True
                    break
        elif self.in_div and tag == "img":
            for attr in attrs:
                if attr[0] == "src":
                    self.img_src = attr[1]
                elif attr[0] == "alt":
                    self.img_alt = attr[1]

    def handle_endtag(self, tag):
        if self.in_div and tag == "div":
            self.in_div = False

def get_random_xkcd():
    max_comic_num = 2500
    random_comic_num = random.randint(1, max_comic_num)
    xkcd_url = f"https://xkcd.com/{random_comic_num}"
    with urllib.request.urlopen(xkcd_url) as response:
        html = response.read()
    parser = XKCDParser()
    parser.feed(html.decode("utf-8"))
    return parser.img_src, parser.img_alt, random_comic_num

img_src, img_alt, comic_num = get_random_xkcd()
html = f'''<!doctype html>

<html>
    <body>
        <a id="comic-link" href="#" target="_blank">
            <img id="comic" src="{img_src}" alt="{img_alt}">
        </a>
        <script>
            const maxComicNum = 2500; // The highest XKCD comic number available
            const randomComicNum = {comic_num};
            const randomComicUrl = `https://cors-anywhere.herokuapp.com/https://xkcd.com/${randomComicNum}`;
            fetch(randomComicUrl)
                .then(response => response.text())
                .then(data => {{
                    const parser = new DOMParser();
                    const htmlDocument = parser.parseFromString(data, "text/html");
                    const comicElement = htmlDocument.querySelector("div#comic img");
                    const comicUrl = comicElement.src;
                    const comicTitle = comicElement.alt;

                    // Get the image size
                    const img = new Image();
                    img.src = comicUrl;
                    img.onload = function() {{
                        const imgWidth = img.width;
                        const imgHeight = img.height;
                        let newWidth, newHeight;

                        // Scale down the image while maintaining aspect ratio
                        if (imgWidth > imgHeight) {{
                            newWidth = 382;
                            newHeight = Math.round((imgHeight / imgWidth) * newWidth);
                        }} else {{
                            newHeight = 382;
                            newWidth = Math.round((imgWidth / imgHeight) * newHeight);
                        }}

                        // Update the image size and URL
                        document.getElementById("comic").src = comicUrl;
                        document.getElementById("comic").width = newWidth;
                        document.getElementById("comic").height = newHeight;
                        document.getElementById("comic-link").href = `https://xkcd.com/${randomComicNum}`;
                        document.getElementById("comic-link").title = comicTitle;
                    }}
                }})
                .catch(error => console.error(error));
        </script>        
    </body>
</html>'''

with open("random_xkcd.html", "w") as file:
    file
