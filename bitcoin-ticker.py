from inky.auto import auto
inky_display = auto()
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)


from font_fredoka_one import FredokaOne

fontSmall = ImageFont.truetype(FredokaOne, 45)
fontLarge = ImageFont.truetype(FredokaOne, 65)

import requests
import math
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
priceFull = data["bpi"]["USD"]["rate"]
price = priceFull.split('.')[0]
message = price + " $"

# btc
draw.text((10, 0), "BTC", inky_display.RED, fontLarge)

# price
w, h = fontSmall.getsize(message)
x = 60
y = 65

draw.text((x, y), message, inky_display.RED, fontSmall)
inky_display.set_image(img)
inky_display.show()

