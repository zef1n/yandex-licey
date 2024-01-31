# Kлассная работа
# Число цифр
def num_digits(number):
    return len(str(number))


# Мелочь оставь себе
def take_large_banknotes(banknotes):
    b = list()
    for i in banknotes:
        if i > 10:
            b.append(i)
    return b


# Число словами
def number_to_words(n):
    num_word = {
        1: 'один', 2: 'два', 3: 'три',
        4: 'четыре', 5: 'пять', 6: 'шесть',
        7: 'семь', 8: 'восемь', 9: 'девять',
        10: 'десять', 11: 'одиннадцать', 12: 'двенадцать',
        13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
        16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать',
        19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
        40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят',
        70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}
    k = n % 10
    if n > 19 and k > 0:
        return " ".join((num_word[n - k], num_word[k]))
    return num_word[n]


# Среднее значение – 2
def average(values):
    values = values or [0]
    if (sum(values) / len(values)) == int(sum(values) / len(values)):
        return int(sum(values) / len(values))
    else:
        return sum(values) / len(values)


# Скажи словами
num1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', '']
num2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']


def number_in_english(number):
    if not number:
        return 'zero'
    if number // 100 and number % 100:
        result = '{} hundred and '.format(num1[number // 100 - 1])
    elif number // 100:
        result = '{} hundred'.format(num1[number // 100 - 1])
    else:
        result = ''
    if number % 100 <= 19:
        result += num1[number % 100 - 1]
    else:
        result = result + num2[number % 100 // 10 - 2] + ' ' + num1[number % 10 - 1]
    return result.strip()


# Секретные материалы
def print_document(pages):
    f = 0
    for i in pages:
        if i[:8] != 'Секретно':
            f += 0
            print(i, end='\n')
        elif i[:8] == 'Секретно':
            f += 1
            break
    if f == 0:
        print('Напечатано без купюр')
    else:
        print('Дальнейшие материалы засекречены')

# Поиски возвышенного


# Домашняя работа
# Месяц/Month

# Простые числа

# Ход конём


# Дополнительные задачи
# Уравнения степени не выше второй

# Палиндромы

# Числа Каталана

# Тень, знай своё место

# Морской бой

# Опоздание

# Надёжный пароль

# Пин-код
