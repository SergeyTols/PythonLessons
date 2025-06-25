hour = 13

if hour >23:
    hour = 23
if hour < 0:
    hour = 0

if hour <= 7 and hour < 12:
    print('утро')
elif hour <= 12 and hour < 18:
    print('день')
elif hour <= 19 and hour < 23:
    print('вечер')
else:
    print('ночь')