# Пишем и подключаем свои модули
# from . lib import summ - из текущей директории
# from .. lib import summ - из уровня выше
# from .lib import summ - относительно текущего файла

# import lib
from lib import diff

# from package1.module import  greet

# from package1 import *  # Для __all__
# import package1

from package1 import greet, add

print(greet('Мир!'))
print(add(3, 7))

# print(package1.module._hidden_function())