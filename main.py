# Библиотека pymorphy
# pip install pymorphy3
# pip install -U pymorphy3-dicts-ru
import pymorphy3

morph = pymorphy3.MorphAnalyzer()

print(morph.parse('Дмитрий'))


