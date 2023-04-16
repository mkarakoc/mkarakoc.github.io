from html.parser import HTMLParser
from urllib.request import Request, urlopen
from random import randint


class XKCDParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.comic_url = ""
        self.comic_title = ""
        self.img_width = 0
        self.img_height = 0
        self.found_comic_div = False

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for attr in attrs:
                if attr[0] == "id" and attr[1] == "comic":
                    self.found_comic_div = True

        elif self.found_comic_div and tag == "img":
            for attr in attrs:
                if attr[0] == "src":
                    self.comic_url = attr[1]
                elif attr[0] == "alt":
                    self.comic_title = attr[1]
                elif attr[0] == "width":
                    self.img_width = int(attr[1])
                elif attr[0] == "height":
                    self.img_height = int(attr[1])
                    
                    # Scale down the image while maintaining aspect ratio
                    newWidth, newHeight = self.scale_down(self.img_width, self.img_height)
                    
                    # Update the image size and URL
                    html = f'<a id="comic-link" href="https://xkcd.com/{self.comic_num}" target="_blank" title="{self.comic_title}">'
                    html += f'<img id="comic" src="{self.comic_url}" alt="{self.comic_title}" width="{newWidth}" height="{newHeight}">'
                    html += '</a>'
                    print(html)
                    
                    # Reset the parser
                    self.found_comic_div = False
                    self.comic_url = ""
                    self.comic_title = ""
                    self.img_width = 0
                    self.img_height = 0

    def scale_down(self, width, height):
        if width > height:
            newWidth = 382
            newHeight = round((height / width) * newWidth)
        else:
            newHeight = 382
            newWidth = round((width / height) * newHeight)
        return newWidth, newHeight

maxComicNum = 2500
randomComicNum = randint(1, maxComicNum)
xkcd_url = f"https://xkcd.com/{randomComicNum}/"
req = Request(xkcd_url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode()
parser = XKCDParser()
parser.comic_num = randomComicNum
parser.feed(html)
