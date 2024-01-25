# # Классная работа
# Каникулы капризного ребёнка
city1 = input()
city2 = input()
if (city1 == 'Тула') or (city2 == 'Пенза'):
    if (city1 == 'Тула') and (city2 == 'Пенза'):
        print('НЕТ')
    elif city1 != city2:
        print('ДА')
    else:
        print('НЕТ')
else:
    print('НЕТ')

# Факториал: первое знакомство
numbers = 1
numbers2 = 2
numbers3 = 3
numbers4 = 4
numbers5 = 5
numbers6 = 6
numbers7 = 7
numbers8 = 8
numbers9 = 9
print(numbers * numbers2 * numbers3 * numbers4 * numbers5 * numbers6 * numbers7 * numbers8 * numbers9)

# Полтора землекопа
a = 1400
b = 6
print(a // b + a % b - 1)

# Количество минут в году
days_per_year = 365
hours_per_day = 24
minutes_per_hour = 60
print(hours_per_day * minutes_per_hour * days_per_year)

# Сложить два числа
a = int(input())
b = int(input())
summ = a + b
print(summ)

# Одно число
number = float(input())
if number > 0.000001:
    print(number ** -1)
elif number == -0.0000001:
    print(1000000)
elif number < 0:
    print(number ** -1)
else:
    print(1000000)

# Длина
a = input()
b = len(a)
print(f'Слово {a} имеет длину {b}')

# На раз-два-три, рассчитайсь!
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(f'{c}\n{b}\n{a}')
elif (a == b) and (c > a):
    print(f'{c}\n{b}\n{a}')
elif (b == c) and (a > b):
    print(f'{a}\n{c}\n{b}')
elif (a == c) and (b > a):
    print(f'{b}\n{c}\n{a}')
elif (a > b and a > c) and (b > c):
    print(f'{a}\n{b}\n{c}')
elif (a > b and a > c) and (c > b):
    print(f'{a}\n{c}\n{b}')
elif (b > a and b > c) and (a > c):
    print(f'{b}\n{a}\n{c}')
elif (b > a and b > c) and (c > a):
    print(f'{b}\n{c}\n{a}')
elif (c > a and c > b) and (a > b):
    print(f'{c}\n{a}\n{b}')
elif (c > a and c > b) and (b > a):
    print(f'{c}\n{b}\n{a}')


# Домашняя работа
# Плюс-минус
number = float(input())
if number > 0:
    print('+')
elif number < 0:
    print('-')
else:
    print('0')

# Какулькатор
a = float(input())
b = float(input())
c = str(input())
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/':
    if (a == 0) or (b == 0):
        print('0')
    else:
        print(a / b)
elif c == '*':
    print(a * b)
else:
    print('888888')

# Високосность
a = int(input())
if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0):
    print('Високосный')
else:
    print('Не високосный')

# Дополнительные задачи
# Уравнение
a = 999999
b = 142857
x = a - b
print(x)

# Пополам
a = int(input())
if a % 2 == 0:
    print('чётное')
else:
    print('нечётное')

# Верстаем визитную карточку
name = input()
print(len(name) * 2 + 3)

# Собери число
number = int(input())
b = (number // 10 % 10 + number % 10)
c = (number // 100 + number // 10 % 10)
if c < b:
    print(str(b) + str(c))
else:
    print(str(c) + str(b))

# Красивое число
number = int(input())
b = number // 10 % 10
c = number % 10
number = number // 100
if number > b > c:
    if (number + c) / 2 == b:
        print('Вы ввели красивое число')
    else:
        print('Жаль, вы ввели обычное число')
elif number > c > b:
    if (number + b) / 2 == c:
        print('Вы ввели красивое число')
    else:
        print('Жаль, вы ввели обычное число')
elif b > number > c:
    if (b + c) / 2 == number:
        print('Вы ввели красивое число')
    else:
        print('Жаль, вы ввели обычное число')
elif b > c > number:
    if (b + number) / 2 == c:
        print('Вы ввели красивое число')
    else:
        print('Жаль, вы ввели обычное число')
elif c > number > b:
    if (c + b) / 2 == number:
        print('Вы ввели красивое число')
    else:
        print('Жаль, вы ввели обычное число')
elif c > b > number:
    if (c + number) / 2 == b:
        print('Вы ввели красивое число')
    else:
        print('Жаль, вы ввели обычное число')
elif number == b:
    if (number + c) / 2 == b:
        print('Вы ввели красивое число')
    else:
        print('Жаль, вы ввели обычное число')
elif number == c:
    if (number + b) / 2 == c:
        print('Вы ввели красивое число')
    else:
        print('Жаль, вы ввели обычное число')
elif b == c:
    if (number + c) / 2 == b:
        print('Вы ввели красивое число')
    else:
        print('Жаль, вы ввели обычное число')
elif number == c == b:
    print('Вы ввели красивое число')

# Четырёхзначный минимум
number = int(input())
a = number // 1000
b = number // 100 % 10
c = number // 10 % 10
d = number % 10
d1 = min(a, b, c, d)
d4 = max(a, b, c, d)
d2 = 0
d3 = 0
if a == d1:
    d2 = min(b, c, d)
    if b == d2:
        d3 = min(c, d)
    elif c == d2:
        d3 = min(c, b)
    elif d == d2:
        d3 = min(b, c)
elif b == d1:
    d2 = min(a, c, d)
    if a == d2:
        d3 = min(c, d)
    elif c == d2:
        d3 = min(d, a)
    elif d == d2:
        d3 = min(a, c)
elif c == d1:
    d2 = min(b, a, d)
    if a == d2:
        d3 = min(b, d)
    elif b == d2:
        d3 = min(d, a)
    elif d == d2:
        d3 = min(a, b)
elif d == d1:
    d2 = min(a, c, b)
    if a == d2:
        d3 = min(c, b)
    elif c == d2:
        d3 = min(b, a)
    elif b == d2:
        d3 = min(a, c)
if d1 == 0 and d2 != 0 and d3 != 0 and d4 != 0:
    print(f'{d2}{d1}{d3}{d4}')
elif d2 == 0 and d1 != 0 and d3 != 0 and d4 != 0:
    print(f'{d1}{d2}{d3}{d4}')
elif d3 == 0 and d2 != 0 and d3 != 0 and d4 != 0:
    print(f'{d1}{d3}{d2}{d4}')

elif d1 == 0 and d2 == 0 and d3 != 0 and d4 != 0:
    print(f'{d3}{d1}{d2}{d4}')
elif d2 == 0 and d3 == 0 and d1 != 0 and d4 != 0:
    print(f'{d1}{d2}{d3}{d4}')
elif d3 == 0 and d4 == 0 and d2 != 0 and d1 != 0:
    print(f'{d1}{d3}{d4}{d2}')
elif d1 == 0 and d4 == 0 and d2 != 0 and d3 != 0:
    print(f'{d2}{d1}{d4}{d3}')

elif d1 == 0 and d2 == 0 and d3 == 0 and d4 != 0:
    print(f'{d4}{d1}{d2}{d3}')
elif d2 == 0 and d1 == 0 and d4 == 0 and d3 != 0:
    print(f'{d3}{d2}{d1}{d4}')
elif d1 == 0 and d4 == 0 and d3 != 0 and d2 != 0:
    print(f'{d2}{d3}{d4}{d1}')
elif d2 == 0 and d4 == 0 and d3 != 0 and d1 != 0:
    print(f'{d1}{d3}{d4}{d2}')

elif d1 != 0 and d2 != 0 and d3 != 0 and d4 != 0:
    print(f'{d1}{d2}{d3}{d4}')

