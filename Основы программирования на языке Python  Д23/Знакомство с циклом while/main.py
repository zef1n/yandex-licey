# Знакомство с циклом while
# Классная работа

# Вспомнить всё: if
temp = float(input())
if temp > 28:
    print('ЖАРКО')
elif temp < 15.5:
    print('ХОЛОДНО')
else:
    print('НОРМАЛЬНО')

# password 123
password = input()
password2 = input()
if len(password) < 8:
    print('Короткий!')
elif password2 != password:
    print('Различаются')
else:
    print('OK')

# Числа до нуля
a = int(input())
while a != 0:
    print(a)
    a = int(input())

# Строки до пустой
a = input()
while a != '':
    print(a)
    a = input()

# Учитель
x = int(input())
while x > 7:
    x = x / 8
print(int(x // 1))

# Скидки
itog = 0
while (a := float(input())) > 0:
    if a > 1000:
        a = ((a / 100) * 95)
    itog += a
print(itog)

# Таких берут в космонавты
min1 = 190
max1 = 150
col = 0
while (rost := input()) != '!':
    rost = int(rost)
    if 150 <= rost <= 190:
        col += 1
        if max1 < rost:
            max1 = rost
        if min1 > rost:
            min1 = rost
print(col)
print(min1, max1)

# Домашняя работа
# Сколько строк?
psixolog = 1
while (user := input()) != 'Спасибо.':
    psixolog += 1
print(psixolog)

# Среднее
b = 0
summ = 0
while (a := float(input())) > -300:
    b += 1
    summ += a
print(round(summ / b, 2))

# 1024 и все-все-все
number = int(input())
f = 1
a = number
while a > 2:
    a = a / 2
    f += 1
if number == 1:
    print(0)
elif a ** f == number:
    print(f)
else:
    print('НЕТ')

# Дополнительные задачи
# password123456
password = input()
if len(password) < 8:
    print('Короткий!')
    pass
elif '123' in password:
    print("Простой!")
elif (password2 := input()) != password:
    print('Различаются')
else:
    print('OK')

# Круглые
number = int(input())
b = (number % 10) // 2
if number % 10 == b:
    while number % 10 == b:
        print(number)
        number = int(input())

# password
n = 0
while n == 0:
    password1 = input()
    password2 = input()
    if len(password1) < 8:
        print('Короткий!')
    elif '123' in password1:
        print('Простой!')
    elif password1 != password2:
        print('Различаются.')
    else:
        n = 1
        print('OK')

# Лабиринт с правом на ошибку
print('Лабиринт')
print('Выберите куда вы хотите пойти "налево(1)", "направо(2)", "прямо(3)"')
print('Введите целое число: 1 2 или 3?')
dver = int(input())
while dver != 1 and dver != 2 and dver != 3:
    dver = int(input('Вы ввели некорректный номер!:'))
else:
    if dver == 1:
        print('Вы пошли налево. Через время вы дошли до двух дверей.')
        print('1. Вы выберете "левую"?')
        print('2. или "правую"?')
        vibor = int(input())
        while vibor != 1:
            print('''Вы открыли правую дверь. Но за ней вас ждал вампир и убил вас! Какую дверь выберите снова? :(
            1. левую
            2. правую ''')
            vibor = int(input())
        else:
            print('Вы открыли левую дверь. Вы успешно сбежали из лабиринта :)')
    elif dver == 2:
        print('Вы пошли направо. Через время вы дошли до двух дверей. Вы выберете "правую"(1) или "левую"(2)?')
        vibor2 = int(input())
        while vibor2 != 2:
            print('''Двери за вами захлопнулись, выберите другой вариант
            1. Налево
            2. Направо''')
            vibor2 = int(input())
        else:
            print('Вы встретили зомби, но вы смогли сбежать! :)')
    elif dver == 3:
        print('Вы пошли прямо. Вы увидели человека, ваши действия?')
        print('1. Пройти мимо')
        print('2. Узнать дорогу из лабиринта')
        vibor3 = int(input())
        while vibor3 != 2:
            print('''Вы бы потерялись в лабиринте, выберите другой вариант
            1. Просто пройти мимо
            2. Узанть дорогу''')
            vibor3 = int(input())
        else:
            print('Незнакомец, помог вам выйти из лабиринта! :)')

# Сиракузская последовательность
number = int(input())
summa = 0
while number != 1:
    if number % 2 == 0:
        number = number // 2
        summa += 1
    else:
        number = 3 * number + 1
        summa += 1
print(summa)

# Бинарная угадайка v2.0
y = 0
y1 = 1001
print('500')
znak = input()
while znak != '=':
    if znak == '>':
        y = y + (y1 - y) // 2
        x = y + (y1 - y) // 2
    elif znak == '<':
        y1 = y1 - (y1 - y) // 2
        x = y1 - (y1 - y) // 2
    print(x)
    znak = input()
if znak == '=':
    print('Угадал')

# Ищем клад — 1
minim = 0
x = int(input())
y = int(input())
x1 = 0
y1 = 0
dvij = 'север'
napravlenie = input()
while napravlenie != 'стоп':
    if int(x) == x1 and int(y) == y1:
        print(minim)
        print(dvij)
        break
    else:
        minim += 1
        if napravlenie == 'вперёд':
            steps = int(input())
            if dvij == 'север':
                y1 += steps
            elif dvij == 'запад':
                x1 -= steps
            elif dvij == 'юг':
                y1 -= steps
            elif dvij == 'восток':
                x1 += steps
        elif napravlenie == 'направо':
            if dvij == 'север':
                dvij = 'восток'
            elif dvij == 'восток':
                dvij = 'юг'
            elif dvij == 'юг':
                dvij = 'запад'
            elif dvij == 'запад':
                dvij = 'север'
        elif napravlenie == 'налево':
            if dvij == 'север':
                dvij = 'запад'
            elif dvij == 'запад':
                dvij = 'юг'
            elif dvij == 'юг':
                dvij = 'восток'
            elif dvij == 'восток':
                dvij = 'север'
        elif napravlenie == 'разворот':
            if dvij == 'север':
                dvij = 'юг'
            elif dvij == 'юг':
                dvij = 'север'
            elif dvij == 'запад':
                dvij = 'восток'
            elif dvij == 'восток':
                dvij = 'запад'
        if int(x) == x1 and int(y) == y1:
            print(minim)
            print(dvij)
            break
        napravlenie = input()
else:
    if x == 0 and y == 0:
        print(0)
        print("север")
