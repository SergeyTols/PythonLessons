# Ctrl + Alt + o - убрать лишний импорт

from PIL import Image, ImageFilter, ImageEnhance

orig = Image.open('images/Kaa.jpg').convert('RGB')
# # Размытие
# blur_image = orig.filter(ImageFilter.GaussianBlur(radius=3))

# Усиление резкости
enchancer = ImageEnhance.Sharpness(orig)
sharpned_image = enchancer.enhance(7.0)
sharpned_image.show()

