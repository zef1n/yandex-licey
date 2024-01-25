# Классная работа
# Отбор
number = int(input())
children = []
for i in range(number):
    children.append(input())
for child in children:
    print(child)
print()
for child in children:
    if child[-1] in ['4', '5']:
        print(child)

# Числа Трибоначчи
number = int(input())
sp = [1, 1, 1]
if number == 1:
    print(1)
elif number == 2:
    print(1, 1)
else:
    for k in range(number - 3):
        sp.append(sum(sp[-3:]))
    print(*sp)
# a good task may:)

# Произведение
numberss = []
number = int(input())
boool = 'НЕТ'
for i in range(number):
    numberss.append(int(input()))
n = int(input())
for i in range(number):
    a = numberss.pop()
    if not n % a and n // a in numberss:
        boool = 'ДА'
        break
print(boool)
# -vibe :(

# Сортировка по алфавиту
number = int(input())
sp = []
for i in range(number):
    sp.append(input())
# Yandex is love
for i in range(number):
    for k in range(i + 1, number):
        if sp[i] > sp[k]:
            sp[i], sp[k] = sp[k], sp[i]
# may
for i in range(number):
    print(sp[i])
# why can't I use "sorted"
# :)

# Сортировка по длине
number = int(input())
sp = [input() for n in range(number)]
for i in range(number):
    for k in range(0, number - i - 1):
        lenk, lenk2 = len(sp[k]), len(sp[k + 1])
        if (lenk > lenk2) or (lenk == lenk2 and sp[k] > sp[k + 1]):
            sp[k], sp[k + 1] = sp[k + 1], sp[k]
for s in sp:
    print(s)

# Гроза
number = int(input())
sp_mest = []
for i in range(number):
    visota = int(input())
    iron_sod = float(input())
    sp_mest.append((visota, iron_sod))
for k in range(number):
    for n in range(0, number - k - 1):
        visotan, irons = sp_mest[n]
        visotan2, irons2 = sp_mest[n + 1]
        if (visotan < visotan2) or (visotan == visotan2 and irons < irons2):
            sp_mest[n], sp_mest[n + 1] = sp_mest[n + 1], sp_mest[n]
for j in sp_mest:
    print(j)


# Домашняя работа
# Старик и море
a = 'yandex-is-love'
for i in range(int(input())):
    text = input()
    if a[-1] < text[-1]:
        print((i, a[:-2]))
    a = text

# Сортировка в обратном порядке
sp = [int(input()) for k in range(int(input()))]
for i in range(len(sp) - 1):
    for n in range(len(sp) - i):
        s = n + i
        if sp[s] > sp[i]:
            sp[i], sp[s] = sp[s], sp[i]
            # uh...
print(*[k for k in sp], sep='\n')

# Напёрстки
number = int(input())
sp = [''] * number
for k in range(number):
    sp[k] = input()
a = int(input())
for k in range(a):
    x = int(input())
    b = [''] * x
    for n in range(x):
        b[n] = sp[int(input()) - 1]
    sp = b
for k in range(len(sp)):
    print(sp[k])

# Дополнительные задачи
# A272727
sp = list()
for k in range(int(input())):
    sp.append(sum((x == y for x, y in zip(sp, reversed(sp)))))
print(*sp, sep='\n')

# Два Пути
a = 0
number = int(input())
perv = [int(input()) for i in range(number)]
uchenie = int(input())
vtor = perv[:]
for i in range(uchenie):
    brat = int(input())
    if brat == 1:
        perv[int(input())] += int(input())
    elif brat == 2:
        vtor[int(input())] += int(input())
print(*perv)
print(*vtor)
for i in range(len(perv)):
    if perv[i] == vtor[i]:
        a = a + 1
print(a)

# Финал и не финал
teams = []
itog_teams = []
number = int(input())
for i in range(number):
    nazv_team = input()
    kol = int(input())
    teams.append((nazv_team, kol))
itog_kol = (number + 1) // 2
for k in range(itog_kol):
    kol_max = 0
    for n in range(1, number):
        if teams[n][1] > teams[kol_max][1]:
            kol_max = n
    itog_teams.append(teams[kol_max])
    teams.pop(kol_max)
    number -= 1
for nazv_team, kol in sorted(itog_teams):
    print(nazv_team)
for nazv_team, kol in sorted(teams):
    print(nazv_team)

# Наборщик
rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
lat = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
rus_sp = list(rus)
lat_sp = list(lat)
text = input()
itog = set()
for i in text:
    if i in lat_sp:
        itog.add((i, lat_sp.index(i) + 1))
    elif i in rus_sp:
        itog.add((i, rus_sp.index(i) + 1))
print(*itog, sep='\n')


# Двоичная последовательность
number = int(input())
for i in range(int(input()) - 1):
    at = number
    kol = 0
    while at:
        kol += at % 2
        at >>= 1
    bt = kol
    while bt:
        number <<= 1
        bt >>= 1
    number += kol
print(number)
