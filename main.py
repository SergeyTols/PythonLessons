# Периодические задачи
#
# pip install schedule

import schedule
import datetime

i = 1


def job():
    global i
    print(f'Скрипт запустится {i}-раз')
    i += 1
    t = datetime.datetime.now()
    print('Время:', t.strftime('%H:%M:%S'))


schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()