# Вложенные циклы
# Классная работа

# Таблица умножения
number = int(input())
i = 1
while i <= number:
    k = 1
    while k <= number:
        print(i * k, end="\t")
        k += 1
    i += 1
    print()

# Таблица не в виде таблицы
number = int(input())
for k in range(1, number + 1):
    for i in range(1, number + 1):
        print(k, '*', i, '=', k * i)

# Примеры
num1 = int(input())
num2 = int(input())
num3 = int(input())
for i in range(num1, num2 + 1, num3):
    for j in range(num1, num2 + 1, num3):
        print(i, '+', j, '=', i + j, end='\t')
    print()

# Ёлочный счёт
number = int(input())
a = 1
i = 1
k = 0
while True:
    while a <= number:
        print(a, end=' ')
        a += 1
        k += 1
        if k == i:
            print()
            i += 1
            k = 0
    break

# Логистический максимин
number = int(input())
maxim = 0
doroga = 1
for i in range(number):
    tunneli = int(input())
    m = 100000000
    for k in range(tunneli):
        visota = int(input())
        if m > visota:
            m = visota
    if maxim < m:
        maxim = m
        doroga = i + 1
print(doroga, maxim)


# Домашняя работа

# Таблица деления
kolonki = int(input())
stroks = int(input())
for x in range(1, stroks + 1):
    print(*(y / x for y in range(1, kolonki + 1)), sep=' ')

# Рисуем прямоугольник
num2 = int(input())
num1 = int(input())
simvol = input()
print(simvol * num1)
for i in range(num2 - 2):
    print(simvol, ' ' * (num1 - 2), simvol, sep='')
print(simvol * num1)

# Сумма степеней
number = int(input())
stepeni = 0
for i in range(1, number + 1):
    stepeni += pow(i, sum(range(i % 2, i + 1, 2)))
print(stepeni)

# Дополнительные задачи

# Обратный отсчёт: серия пусков
for i in range(1, int(input()) + 1):
    for k in range(i, 0, -1):
        print('Осталось секунд:', k - 1)
    print('Пуск', i)

# Простые числа на миллион долларов
number = int(input())
listi = []
j = 0
for i in range(2, number):
    for k in range(2, i):
        if i % k == 0:
            j = j + 1
    if j == 0:
        listi.append(i)
    else:
        j = 0
for x in listi:
    print(x)

# Начинающий фермер
subsidii = int(input())
golovi = int(input())
for i in range(1, subsidii // 20 + 1):
    for k in range((subsidii - i * 20) // 10 + 1):
        a = golovi - i - k
        if i * 20 + k * 10 + a * 5 == subsidii:
            print(i, k, a)

# Числовая дружба
for i in range(1, 10000):
    k = 0
    n = 0
    for zapobedu in range(1, i):
        if i % zapobedu == 0:
            k += zapobedu
    for funya in range(1, k):
        if k % funya == 0:
            n += funya
    if i == min(i, k) and i != k and i == n:
        print(i, k)

# Дальние командировки
number = int(input())
a = 9
i = 1
k = 0
while i * a < number:
    number -= a * i
    i += 1
    a = 10 * a
if i - 1:
    k = int("9" * (i - 1))
b = number // i + k
print(b)

# Пифагоровы тройки
f = ''
number = int(input())
m = int(number ** 0.5) + 1
for i in range(1, m + (m + 1) % 2, 2):
    for k in range(2, m + m % 2, 2):
        if i * i + k * k < number + 1:
            a = 2 * i * k
            b = abs(i * i - k * k)
            c = i * i + k * k
            a1, b1 = a, b
            while a1 != b1:
                if a1 > b1:
                    a1 = a1 - b1
                else:
                    b1 = b1 - a1
            b1 = c
            while a1 != b1:
                if a1 > b1:
                    a1 = a1 - b1
                else:
                    b1 = b1 - a1
            d = a1
            d2 = str(min(a // d, b // d)) + ' ' + str(max(a // d, b // d)) + ' ' + str(c // d) + ' '
            if d2 not in f:
                print(d2)
            f += d2
