
from PIL import Image, ImageDraw
from PIL.ImageFont import ImageFont

image = Image.new('RGB', (600, 400), (0, 0, 255))
draw = ImageDraw.Draw(image)

draw.ellipse((470, -120, 800, 120), outline='yellow', fill='yellow')
draw.text((150, 180), text="It's a sunny day", fill='yellow', font_size=40)
draw.text((500, 380), text="Made by Sarge", fill='white', font_size=10)
image.save('images/deep_blue.jpg')
