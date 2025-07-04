# Вешние библиотеки
# Графика
# PIL - Pythom Imagine Library (pillow - подушка)
# Команды в терминал:
# pip install pillow
# pip freeze > requirements.txt - создание файла зависимости
# pip install -r requirements.txt - установка списка библиотек
# PyPI - Python Package Index (pypi.org)
from PIL import Image, ImageDraw

RED = (255, 0, 0)
POLY = [(50, 50), (150, 50), (180, 120)]
image = Image.new('RGB', (600, 400), (0, 0, 255))

draw = ImageDraw.Draw(image)

draw.line((0, 0, 600, 400), fill=(0, 255, 0), width=5)
draw.line((600, 0, 0, 400), fill=RED, width=5)
draw.rectangle((10, 10, 590, 390), outline=RED, width=10)
draw.ellipse((10, 10, 590, 390), outline=RED, width=10)
draw.polygon(POLY, outline='green', width=15)
draw.text((100, 80), text='ghfdsg', fill=(0, 0, 0), font_size=40)


image.save('images/deep_blue.jpg')

