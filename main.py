# Встроеннные библиотеки
# PyPI - Python Package Index (pypi.org)
# sample (в отличие от choice) выбирает уникальные (без повторов)

import datetime as dt

my_time = dt.time(15, 27, 32)
print(my_time)
my_day = dt.date(2025, 7, 4)
print(my_day)
my_date_time = dt.datetime.combine(my_day, my_time)
print(my_date_time)

date1 = dt.date(2025, 6 , 15)
date2 = dt.date(2025, 7 , 3)
delta = date1 - date2

print(delta)

# # print(dt.datetime.now().time())
# time = dt.datetime.now()
# ftime = time.strftime('%d-%m-%Y') # %y - будет только 25
# ftime1 = time.strftime('%H:%M:%S')
#
# print(ftime)
# print(ftime1)