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

# btc-text
draw.text((10, 0), "BTC", inky_display.RED, fontLarge)

# price-text
w, h = fontSmall.getsize(price)
x = 60
y = 65

draw.text((x, y), price, inky_display.RED, fontSmall)
inky_display.set_image(img)
inky_display.show()