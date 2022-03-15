#! /usr/bin/env python3
import requests
import math
from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

inky_display = auto()
inky_display.set_border(inky_display.WHITE)

fontSmall = ImageFont.truetype(FredokaOne, 45)
fontLarge = ImageFont.truetype(FredokaOne, 65)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
priceFull = data["bpi"]["USD"]["rate"]
price = priceFull.split('.')[0] + " $"

# Note the constants - The third color whether red or yellow is the same
# inky_display.WHITE = 0
# inky_display.BLACK = 1
# inky_display.RED = 2
# inky_display.YELLOW = 2
textcolor = 2

# btc-text (left aligned on top 50%)
coinsymbol = "BTC"
w, h = fontLarge.getsize(coinsymbol)
x = 5
y = int(((inky_display.HEIGHT * .50)/2) - (h/2))
draw.text((x, y), coinsymbol, textcolor, fontLarge)

# price-text (right aligned on bottom 50%)
w, h = fontSmall.getsize(price)
x = inky_display.WIDTH - w - 5
y = int(inky_display.HEIGHT - ((inky_display.HEIGHT * .50)/2) - (h/2))
draw.text((x, y), price, textcolor, fontSmall)

# render
inky_display.set_image(img)
inky_display.show()
