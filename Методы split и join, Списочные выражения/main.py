# Классаня работа

# Глория Скотт
print(*input().split()[2::3])

# Списочная квадратура
print(*[i**2 for i in range(int(input()))], sep="\n")


# Горизонтальная диаграмма
number = input().split(" ")
for i in number:
    print("*" * int(i), sep="\n")

# Списочная квадратура - 2
# print(' '.join([str(i * i) for i in range(int(input()))]))

# Списочная квадратура - 3
print(" ".join([str(int(i) ** 2) for i in (input()).split(" ")]))

# Списочная квадратура - 4
print(
    *[x for x in [i**2 for i in map(int, input().split()) if i % 2] if x % 10 != 9],
    sep=" "
)

# Домашняя работа

# Список строк
listo4ek = str(input().split()).replace("'", '"')
print(listo4ek)

# Единицы в квадрате
listo4ek = [int(input())]
i = 1
k = ""
while i < listo4ek[0]:
    k += str(i**2) + ", "
    i = int(str(i) + "1")
print(k[:-2])

# Только без лука!
listo4ek = [input() for i in range(int(input()))]
a = ""
for i in listo4ek:
    if not (("Лук" in i) or ("лук" in i)):
        a += i + ", "
print(a[:-2])

# Дополнительные задачи
# Маяковский
print(*(str(input()).split()), sep="\n")

# /etc/passwd
sp = []
sp2 = list(input().split(":"))
while sp2 != [""]:
    sp.append(sp2)
    sp2 = list(input().split(":"))
sp3 = list(input().split(";"))
for i in range(len(sp)):
    if sp3.count(sp[i][1]) != 0:
        print("To:", sp[i][0])
        k = sp[i][4].split(",")
        print(k[0] + "," + " ваш пароль слишком простой, смените его.")

# Вертикальная диаграмма
number = list(map(int, input().split()))
maxy = max(number)
maxx = len(number)
print("*" * (maxx + 2))
print("*" + " " * maxx + "*")
for i in range(1, maxy + 1):
    print(end="*")
    for k in number:
        if k >= maxy - i + 1:
            print(end="*")
        else:
            print(end=" ")
    print("*")

# GET
url = input().split("?")
del url[0]
url = "".join(url)
url = str(url)
url = url.split("&")
sp = {}
for i in url:
    cur = i.split("=")
    sp[cur[0]] = cur[1]
print(sp[input()])

# Джек-Победитель-Великанов
number = int(input())
sp = []
while number:
    sp2 = []
    while True:
        text = input()
        if text == "*":
            break
        else:
            sp2 += text.strip().split()
    number -= 1
    sp.append("-".join(sp2))
    sp2 = []
print(", ".join(sp[::-1]))
# :)

# Только миллиардеры
# jur = input().split(';')
# itog = [','.join([str(kol) for kol in map(int, jurrik.split(',')) if kol >= 1000000000]) for jurrik in jur]
# print('\n'.join(itog))

# Колобок и кочки
number = int(input())
sp = [int(input()) for m in range(number)]
sp2 = [input() for m in range(number)]
flag = ""
a = ""
s = 0
k = -1
f = 0
r = 0
e = 0
babuling = True

for i in sp2:
    k += 1
    for n in range(len(i)):
        for g in range(len(i)):
            if i[n] == i[g]:
                s += 1
        if s == sp[k]:
            flag += i[n]
        s = 0

for g in sp:
    f += g

if f != len(flag):
    babuling = False
    print("нечленораздельно", end="")

if babuling:
    a = flag[0]
for z in range(1, len(flag)):
    if not babuling:
        break
    if flag[z] == flag[z - 1] and r < sp[e]:
        r += 1
        continue
    r = 1
    e += 1
    a += flag[z]

if f != len(flag) and babuling:
    print("нечленораздельно")
elif a == "упс":
    print("нечленораздельно")
else:
    print(a)
