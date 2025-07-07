# Пишем и подключаем свои модули
# from . lib import summ - из текущей директории
# from .. lib import summ - из уровня выше
# from .lib import summ - относительно текущего файла

# import lib
from lib import diff

if __name__ == '__main__':
    print(diff(7, 3))


def main():
    print(diff(7, 3))

# print(__name__)

if __name__ == '__main__':
    main()