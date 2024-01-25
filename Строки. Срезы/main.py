# Kлассная работа

# Шах и мат, программисты
number = int(input())
b = 64
for i in range(number, 0, -1):
    for j in range(1, number + 1):
        print(chr(b + j), i, sep="", end=" ")
    print()

# Имя пользователя
simvols = ["_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
nicname = list(input())
for i in nicname:
    if i not in "1234567890_qwertyuiopasdfghjklzxcvbnm":
        print("Неверный символ:", i)
        break
else:
    print("OK")

# Быки и коровы
text = str(input())
text2 = str(input())
c = d = 0
for i in range(len(text)):
    if text[i] == text2[i]:
        c += 1
    elif text[i] in text2:
        d += 1
print(c, d)

# Слова и буквы
word = input()
sp = []
while word != "стоп":
    sp.append(word)
    word = input()
maximum = max(sp, key=len)
minimum = min(sp, key=len)
if set(maximum).issuperset(set(minimum)):
    print("ДА")
else:
    print("НЕТ")


# Вредные советы
number = int(input())
for k in range(number):
    soveti = input()
    if soveti[:3] == "Не " or soveti[:3] == "не ":
        print(soveti[3:])
    else:
        print(soveti)

# Анонс новости
dlina = int(input())
number = int(input())
for i in range(number):
    news = input()
    if len(news) <= dlina:
        print(news)
    else:
        print(news[: dlina - 3] + "...")

# Найди кота — 5
for number in range(int(input())):
    text = input()
    if text.find("кот") != -1:
        print(number + 1, text.find("кот") + 1)

# Домашняя работа

# Американский формат
number = input()
print("+1", "(", number[0:3], ")", number[3:6], "-", number[6:10], sep="")

# Буквоедство
word = input()
while len(word):
    print(word)
    word = word[1:-1]

# Фильтр
number = int(input())
for i in range(number):
    words = input()
    if words[:2] == "%%":
        print(words[2:])
    elif words[:4] == "####":
        pass
    else:
        print(words)

# Дополнительные задачи

# Именно та буква
word = input()
number = int(input())
letter = input()
if (0 < number <= len(word)) and letter == word[number - 1] and len(letter) == 1:
    print("ДА")
elif (0 < number <= len(word)) and letter != word[number - 1] and len(letter) == 1:
    print("НЕТ")
else:
    print("ОШИБКА")

# Минификатор
number = int(input())
itog = []
simv = 0
flag = False
sl = False
for i in range(number):
    string = input()
    while string[simv] == " ":
        itog.append(" ")
        simv += 1
    for i2 in range(simv, len(string)):
        if not sl:
            if string[i2] == "\\":
                itog.append(string[i2])
                sl = True
            elif string[i2] == "'":
                itog.append(string[i2])
                flag = not flag
            elif string[i2] == " ":
                if flag:
                    itog.append(string[i2])
                else:
                    if i2 + 1 != len(string):
                        if string[i2 + 1] == " ":
                            itog.append("")
                        else:
                            itog.append(string[i2])
            elif string[i2] == "#":
                if flag:
                    itog.append(string[i2])
                else:
                    break
            else:
                itog.append(string[i2])
        else:
            sl = False
            itog.append(string[i2])
    print("".join(itog))
    itog = []
    simv = 0
    flag = False
    sl = False

# Слова для кадавра
itog = []
cons = "бвгджзйклмнпрстфхцчшщьъ"
vow = "аеёиоуыэюя"
text = input()
for j in iter(input, ""):
    a = text
    k = 0
    if "*" in a and len(j) + 2 > len(a):
        a = a.replace("*", "?" * (len(j) - len(a) + 1))
    if len(j) == len(a):
        dlin = len(j)
        for i in range(dlin):
            if (
                a[i] == "?"
                or (j[i] in vow and a[i] == "0")
                or (j[i] in cons and a[i] == "1")
            ):
                k = 1
            else:
                k = 0
                break
    if k:
        itog.append(j)
print(*itog, sep="\n") if itog else print("Есть нечего, значить!")

# Резиновые слова
word = input()
if len(word) % 2 == 0:
    number = len(word) // 2
    for i in range(number):
        print(
            " " * (number - i - 1)
            + word[number - i - 1]
            + " " * i
            + " " * i
            + word[number + i]
        )
else:
    number2 = (len(word) + 1) // 2
    print(
        " " * ((len(word) - 1) // 2) + word[number2 - 1] + " " * ((len(word) - 1) // 2)
    )
    for i in range(1, number2):
        print(
            " " * (number2 - i - 1)
            + word[number2 - i - 1]
            + " " * i
            + " " * (i - 1)
            + word[number2 + i - 1]
        )

# Ползём вниз
text = input()
posicia = 0
text_form = text[1::].replace("V", "!V!").split("!")
if len(text) == 1 or text[1] == "V":
    k = 1
else:
    k = 0
for i in text_form:
    if i == "":
        continue
    elif i[0] == "<":
        posicia -= len(i)
        print(posicia * " " + text[0] + i.replace("<", text[0]))
        k = 0
    elif i[0] == "V":
        if k:
            print(posicia * " " + text[0])
        k = 1
    elif i[0] == ">":
        print(posicia * " " + text[0] + i.replace(">", text[0]))
        posicia += len(i)
        k = 0
if k:
    print(posicia * " " + text[0])
