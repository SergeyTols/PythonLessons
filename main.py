# Ctrl + Alt + o - убрать лишний импорт

from PIL import Image, ImageFilter, ImageEnhance

orig = Image.open('images/Kaa.jpg')
# Размытие
blur_image = orig.filter(ImageFilter.GaussianBlur(radius=3))


blur_image.show()

