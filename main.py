# Вешние библиотеки
# Графика
# PIL - Pythom Imagine Library (pillow - подушка)
# Команды в терминал:
# pip install pillow
# pip freeze > requirements.txt - создание файла зависимости
# pip install -r requirements.txt - установка списка библиотек
# PyPI - Python Package Index (pypi.org)
from PIL import Image

image = Image.open('images/Kaa.jpg')

x, y = image.size
mode = image.mode
pixel = image.load() # загрузить таблицу пикселей

print(f'Ширина = {x}, высота = {y}')
print(f'Цветовая схема: {mode}')

image_rotate = image.rotate(90)
image_flip = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
image_cropped = image.crop((180, 0, 600, 250))
resized = image.resize((400, 200))

# # Grayscale
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixel[i, j]
#         average = (r + g + b) // 3
#         pixel[i, j] = average, average, average

# # Негатив
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixel[i, j]
#         pixel[i, j] = 255 - r, 255 - g, 255 - b

# # Инверсия
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixel[i, j]
#         pixel[i, j] = g, r, b


image.save('images/pyton2.jpg')
image_rotate.save('images/pyton3.jpg')
image_flip.save('images/pyton4.jpg')
image_cropped.save('images/pyton5.jpg')
resized.save('images/pyton6.jpg')