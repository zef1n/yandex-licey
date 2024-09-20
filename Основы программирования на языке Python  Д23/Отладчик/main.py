# # Классная работа
# # Банк
print("Добро пожаловать в интернет-банк!")
print("У нас фантастические процентные ставки!")
print("Для вкладов до 10 тысяч ₽ включительно прибыль составит 10%,")
print("для вкладов на сумму до 100 тысяч включительно - 20%,")
print("для более 100 тысяч - 30%!")
print("На какую сумму желаете сделать вклад?")
money = float(input())
if money <= 10000:
    money *= 1.1
elif money > 100000:
    money *= 1.3
elif money <= 100000:
    money *= 1.2
print("Вы получаете", money, "₽, поздравляем!")
#
# # Фибоначи
number = int(input())
(a, b) = (1, 1)
while a <= number:
    print(a)
    (a, b) = (b, a + b)
#
# # Ним-пасьянс
kol = int(input())
while kol != 0 and kol > 0:
    hod = int(input())
    kol -= hod
    if kol < 0:
        print("0")
    else:
        print(kol)
#
# # Псевдоним-пасьянс
kol = int(input())
while kol != 0:
    hod = int(input())
    if hod <= kol and hod > 0 and hod <= 3:
        kol = kol - hod
        print(kol)
    else:
        print(kol)

# # Псевдоним v2.0
kol = int(input())
hod = -1
while kol != 0:
    if hod == -1:
        b = kol % 4
        if b == 0:
            b = 2
    elif hod == 1:
        b = int(input())
        while not (1 <= b <= 3 and b <= kol):
            if b < 1 or b > 3:
                print("Некорректный ход:", b)
            else:
                print("Некорректный ход:", b)
            b = int(input())

    kol -= b
    hod = -hod
    print(b, kol)
if hod == 1:
    print("ИИ выиграл!")
else:
    print("Вы выиграли!")
#
# # Домашнее задание
# Перевод
number1 = int(input())
number2 = 0
while number1 > 0:
    b = number1 % 10
    number1 = number1 // 10
    number2 = number2 * 10
    number2 = number2 + b
print(number2)
#
# # Остров невезения
d = int(input())
m = int(input())
m -= 2
k = int(input())
if m < 1:
    m = m + 12
    k = k - 1
c = k // 100
y = k % 100
print((d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7)

# # Цирк, цирк, цирк
kol = int(input())
kol_hod = 0
while kol > 1:
    kol_hod += 1 + kol % 2
    kol //= 2
print(kol_hod)
#
# # Дополнительные задачи
# # Псевдоним-мизер
kol = int(input())
hods = 0
hod = 1
while kol > 1:
    hods = kol % 4
    if hods == 0:
        hods = 3
    elif hods == 1:
        hods = 1
    else:
        hods -= 1
    print("ИИ забрал", hods)
    kol -= hods
    print("Осталось камней", kol)
    if kol == 1:
        print("ИИ выиграл!")
    else:
        hods = 0
        hod = 0
        while hod > 3 or hod < 1 or hod > kol:
            print("Бери!")
            hod = int(input())
        kol -= hod
        print("Осталось камней", kol)
        if kol == 1:
            print("Вы выиграли!")

# # Ним2-пасьянс
number = int(input())
number2 = int(input())
while number or number2:
    n = int(input())
    if n == 2:
        h = int(input())
        number2 -= h
    elif n == 1:
        h = int(input())
        number -= h
    print(number, number2)
#
# # Лабиринт 2
print("Лабиринт")
print('Выберите куда вы хотите пойти "налево", "направо", "прямо"')
dver = 1
while dver > 0:
    if dver == 1:
        print(
            "Вы находитесь в пещере на развилке. Вы можете пойти «налево», «направо» или «прямо»."
        )
        vibor = input()
        while vibor != "налево" and vibor != "прямо" and vibor != "направо":
            vibor = input()
        if vibor == "налево":
            print("Вы открыли левую дверь. Вы успешно сбежали из лабиринта :)")
            dver = 2
        elif vibor == "прямо":
            print("Вы пошли прямо. Вы увидели человека!")
            dver = -1
        elif vibor == "направо":
            print(
                "Вы открыли правую дверь. Но за ней вас ждал вампир и укусил вас! Вы проснулись и оказались около "
                "туннелей :("
            )
            dver = -1
    elif dver == 2:
        print("Вы выберете «левый» или «правый»? Или повернёте «назад»?")
        vibor = input()
        while vibor != "левый" and vibor != "правый" and vibor != "назад":
            vibor = input()
        if vibor == "левый":
            print("Вы вернулись в начало лабиринта :(")
            dver = -1
        elif vibor == "правый":
            print("Незнакомец, помог вам выйти из лабиринта! :)")
            dver = -2
        elif vibor == "назад":
            print("Вас съел зомби :( -мяу ")
            dver = 1
#
# # Бот-говорилка
print("Как у вас дела?")
text = input()
if ("хорош" or "прекрасн") in text:
    print("Круто! У меня тоже всё прекрасно :) Какие планы на сегодня?")
    text = input()
    if "раб" in text:
        print("Работайте не много. Отдыхать тоже нужно! ;(")
    elif "отдых" in text:
        print("Я тоже отдыхать планирую :)")
    else:
        print("Хорошие планы!")
elif "плох" in text:
    print("Что случилось?")
    text = input()
    print("Ничего себе! Какое ужас!И что вы сделаете?")
    text = input()
    print("Насчет этого решения лучше поговорите с кем-нибудь из друзей.")
elif "ужасн" in text:
    print("Всё образуется, лучше сходите развеяться на улицу.")
    text = input()
    if ("ок" or "хорош" or "обязательн") in text:
        print("И позвите друзей, чтобы было, что поделать!")
    elif ("не" or "хоч") in text:
        print("Грустно :(! А ведь это бы подняло ваше настроение!")
elif "не" in text:
    print("Извините, я вас не понимаю")
elif "?" in text:
    print("Извините, я вас не понимаю")
else:
    print("Извините, я вас не понимаю")

# Ним - 2 (не засчитано)
print("Введите количество камней в первой и во второй кучке")
vopros = int(input())
vopros2 = int(input())
number = 0
if vopros > vopros2:
    print("ИИ взял", vopros - vopros2)
    vopros = vopros - (vopros - vopros2)
    print("Осталось:", vopros, vopros2)
elif vopros < vopros2:
    print("ИИ взял", vopros2 - vopros)
    vopros2 = vopros2 - (vopros2 - vopros)
    print("Осталось:", vopros, vopros2)
else:
    print("ИИ взял 1")
    vopros -= 1
    print("Осталось:", vopros, vopros2)
while vopros + vopros2 != 0:
    vopros3 = int(input("Введите из какой кучки вы заберёте камни, 1 или 2: "))
    while vopros3 != 2 and vopros3 != 1:
        vopros3 = int(
            input(
                "Введите из какой кучки вы заберёте камни,\
1 или 2: "
            )
        )
    answer4 = int(input("Введите сколько камней вы возьмёте: "))
    if vopros3 == 2:
        while answer4 > vopros2:
            print("Введите сколько камней вы возьмёте:")
            answer4 = int(input())
    elif vopros3 == 1:
        while answer4 > vopros:
            answer4 = int(input("Введите сколько камней вы возьмёте: "))
    if vopros3 == 2:
        number += 1
        vopros2 = vopros2 - answer4
        print(vopros, vopros2)
        print("Вы взяли", answer4, ",осталось:", vopros, vopros2)
    elif vopros3 == 1:
        number += 1
        vopros = vopros - answer4
        print("Вы взяли", answer4, ",осталось:", vopros, vopros2)
    if vopros > vopros2:
        number += 1
        print("ИИ взял:", vopros - vopros2)
        vopros = vopros2
        print(vopros, vopros2)
    elif vopros < vopros2:
        number += 1
        print("ИИ взял:", vopros2 - vopros)
        vopros2 = vopros
        print(vopros, vopros2)
if number % 2 == 1:
    print("ИИ победил")
if number % 2 == 0:
    print("Вы победили")
