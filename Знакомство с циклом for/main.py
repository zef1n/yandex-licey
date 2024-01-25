# Знакомство с циклом for
# Классаня работа
# Плюсики
separate = input()
word1 = input()
word2 = input()
word3 = input()
print(word1, word2, word3, sep=sep)

# Повторение - мать учения: ultimate edition
word = input()
kol = int(input())
for i in range(kol):
    print(word)

# Вышел зайчик погулять
a = int(input())
for i in range(a + 1):
    print(i, end=' ')

# Кубизм
a = int(input())
for i in range(a + 1):
    print('Куб числа', i, "равен", i * i * i)

# Факториал
a = int(input())
b = 1
for i in range(a):
    i += 1
    b = b * i
print(b)

# Перемножить без трюков
number = 1
for i in range(6):
    a = int(input())
    if a != 0:
        number = number * a
print(number)

# Расписание
a = int(input())
m = int(input())
b = a
print(b, end=' ')
while b + m <= 31:
    b += m
    print(b, end=' ')

# Делите ли
number = int(input())
a = 0
for i in range(1, int(number) + 1):
    if number % i == 0:
        if i != (int(number)):
            print(i, end=' ')
        else:
            print(i, end='')
        a += 1
if number == 1:
    print('\nНЕТ')
elif a < 3:
    print('\nПРОСТОЕ')
else:
    print('\nНЕТ')

# Домашняя работа
# Обратный отсчёт
number = int(input())
a = 1
if number >= 0:
    while number >= 0:
        print('Осталось секунд: ', number)
        number -= 1
    print('Пуск!')
else:
    print('Пуск!')

# Дзета-функция Римана
pep8 = 3.141592653589793
n = 0
number = int(input())
for i in range(1, number + 1):
    n += 1 / (i ** 2)
print(pep8 ** 2 / n)

# Прамида
number = int(input()) - 1
a = 1
while number > -1:
    print(' ' * number + '*' * a)
    a += 2
    number -= 1

# Дополнительные задачи
# Тест на делимость
for i in range(0, 17):
    number = int(input())
    if i % number == 0:
        print('ДА')
    else:
        print('НЕТ')

# Сумма ряда
number = int(input())
a = 0
b = 1
itog = 0
while number != 0:
    n = int(input())
    a += 1
    while a % 2 == 0:
        itog -= n
        break
    while a % 2 != 0:
        itog += n
        break
    number -= 1
print(itog)

# Число пи
number = int(input())
i = 0
for number in range(1, number * 2, 2):
    i += ((number + 1) % 4 - 1) / number
print(i * 4)

# Умнее среднего
number = int(input())
iq = int(input())
print(0)
i = 1
s = iq
while i < number:
    sredn = s / i
    iq = int(input())
    if iq > sredn:
        print('>')
    elif iq < sredn:
        print('<')
    else:
        print(0)
    i += 1
    s += iq

# Конфетное изобилие
number = int(input())
number_max = int((2 * number) ** (1 / 2))
for i in range(number_max, 0, -1):
    if (2 * number - i * i + i) % (2 * i) == 0:
        print((2 * number - i * i + i) // (2 * i))
        break

# Шварценеггер против Годзиллы
number = 0
uron = 1
for i in range(int(input())):
    a = int(input())
    b = int(input())
    number = b * number + uron * a
    uron *= b
x = number
y = uron
while y > 0:
    x, y = y, x % y
print(number // x, '/', uron // x, sep='')
