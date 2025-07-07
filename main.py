# Ctrl + Alt + o - убрать лишний импорт

from PIL import Image

orig = Image.open('images/deep_blue.jpg').convert('RGB')

up = orig.crop((0, 0, 600, 200))
down = orig.crop((0, 200, 600, 400))

new = Image.new('RGB',(600, 400))
new.paste(down,(0, 0))
new.paste(up,(0, 200))

new.show()

