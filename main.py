# Функции
# Функция с аннотацией
num_to_str = {

}

                      #any
def number_to_words(n: int) -> str:  # При использовании ретерн
    """
    Функция... (тут описание)
    :param n: двузначное число
    :return: это число словами
    """
    if len(str(n)) > 2:
        return  'Введите двузначное число'
    if len(str(n)) == 1 or n in num_to_str:
        return num_to_str[int(n)]
    return num_to_str[int(str(n)[0] + '0')] + ' ' + num_to_str[int(str(n)[1])]


print(number_to_words(13))
