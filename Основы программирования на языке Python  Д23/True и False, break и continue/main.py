# True и False, break и continue
# Классная работа
# Найди кота
number = int(input())
c = False
for i in range(number):
    words = input()
    if "кот" in words or "Кот" in words:
        c = True
        break
if c:
    print("МЯУ")
else:
    print("НЕТ")

# Найди кота - 2
n = 0
c = -1
while (word := input()) != "СТОП":
    n += 1
    if "Кот" in word or "кот" in word:
        c = n
        break
print(c)

# Найди кота (break)
c = False
for i in range(int(input())):
    words = input()
    if ("кот" in words) or ("Кот" in words):
        print("МЯУ")
        c = True
        break
if not c:
    print("НЕТ")

# Найди кота — 2 (break)
number = 0
i = -1
while (a := input()) != "СТОП":
    number += 1
    if "кот" in a or "Кот" in a:
        i = number
        break
print(i)

# Сложиться до 10
numbers = -1
a = 0
summa = 0
while numbers != 0:
    numbers = int(input())
    a += 1
    summa += numbers
    if summa == 10:
        print(a)
        break

# Подарок лепрекона
end = ""
zlo = 0
dobro = 0
while (word := input()) != "":
    if word == "Какой подарок?":
        if dobro > zlo and end == "добрый":
            print("серебряный шиллинг")
        elif dobro < zlo and end == "злой":
            print("золотой шиллинг")
        else:
            print("Ах, не знаю!")
            break
        zlo = dobro = 0
    elif word == "добрый":
        end = "добрый"
        dobro += 1
    elif word == "злой":
        end = "злой"
        zlo += 1

# Домашняя работа
# Найди кота — 3
number = 0
i = 0
while (a := input()) != "СТОП":
    if i == 0:
        number += 1
    if "кот" in a or "Кот" in a:
        i += 1
if i != 0:
    print(i, number)
else:
    print("0 -1")

# Караул
while True:
    number = int(input())
    if number == 0:
        break
    elif not number % 7 and not number % 3:
        print("Караул!")
        break
    elif not number % 7:
        print("опасное")
    elif not number % 3:
        print("несчастливое")
    else:
        print(number)

# Ищем клад - 2
x = 0
y = 0
n = 0
x_input = int(input())
y_input = int(input())
a = True
kompas = input()
c = int(input())
while kompas != "стоп":
    if x_input == x and y_input == y:
        a = False
    if kompas == "север":
        y += c
        if a:
            n += 1
    elif kompas == "запад":
        x -= c
        if a:
            n += 1
    elif kompas == "юг":
        y -= c
        if a:
            n += 1
    elif kompas == "восток":
        x += c
        if a:
            n += 1
    kompas = input()
    if kompas != "стоп":
        c = int(input())
print(n)

# Доп задачи
# Найди кота - 4
number = int(input())
kotik = False
for i in range(number):
    text = input()
    if "Кот" in text or "кот" in text:
        kotik = True
    if "Пёс" in text or "пёс" in text:
        kotik = False
if kotik is True:
    print("МЯУ")
elif kotik is False:
    print("НЕТ")

# Школа танцев
terpila = int(input())
number = 1
ter = 0
right = 0
while ter != terpila:
    s = input()
    if number == 1 and s == "раз":
        right += 1
        number += 1
    elif number == 2 and s == "два":
        right += 1
        number += 1
    elif number == 3 and s == "три":
        right += 1
        number += 1
    elif number == 4 and s == "четыре":
        right += 1
        number = 1
    else:
        print("Правильных отсчётов было " + str(right) + ", но теперь вы ошиблись.")
        right = 0
        ter += 1
        number = 1
print("На сегодня хватит.")

# Многоразовый калькулятор
znak = ""
k = 1
while znak != "x":
    number1 = int(input())
    znak = input()
    if znak == "x":
        print(number1)
        break
    else:
        if znak == "+":
            number2 = int(input())
            print(number1 + number2)
        elif znak == "!" and number1 > 0:
            for i in range(1, number1 + 1):
                k *= i
            print(k)
        elif number1 == 0 and znak == "!":
            print("1")
        elif znak == "*":
            number2 = int(input())
            print(number1 * number2)
        elif znak == "-":
            number2 = int(input())
            print(number1 - number2)
        elif znak == "/":
            number2 = int(input())
            if number2 == 0:
                continue
            else:
                print(number1 // number2)
        elif znak == "%":
            number2 = int(input())
            if number2 == 0:
                continue
            else:
                print(number1 % number2)

# Биржевой робот
cenaakc = int(input())
cenaakc1 = int(input())
stok = False
while cenaakc1 != 0:
    if not stok:
        if cenaakc < cenaakc1:
            incena = cenaakc1
            stok = True
    if stok:
        if cenaakc > cenaakc1:
            outcena = cenaakc1
            break
    cenaakc = cenaakc1
    cenaakc1 = int(input())
print(incena, outcena, outcena - incena)

# Заводные жуки в квадрате
import math

x = float(input())
y = float(input())
k = 0
if x < y:
    print(k)
    exit()
while not abs(x - y) <= 0.01:
    x = math.sqrt(y**2 + (x - y) ** 2)
    k += 1
print(k)

# Проверка блокчейна
number = int(input())
k = 0
nepravilheh = -1
for i in range(number):
    b = int(input())
    h, r, m = b % 256, (b // 256) % 256, b // 256**2
    n = ((m + r + k) * 37) % 256
    if h >= 100 or n != h:
        nepravilheh = i
        break
    k = h
print(nepravilheh)
