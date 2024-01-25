# Kлассная работа
# От и до — 2
numbers = [int(i) for i in input().split()]
sp1, sp2 = [int(i) for i in input().split()]
numbers = numbers[sp1 : sp2 + 1]
print(sum(numbers))

# От и до — 3
numbers = list(map(int, input().split()))
a, b = map(int, input().split())
itog = sum(x**2 for x in numbers[a : b + 1])
print(itog)

# Найди кота — 6
number = int(input())
text = ""
for i in range(1, number + 1):
    a = input()
    if a.find("кот") != -1:
        text += str(i) + " " + str(a.find("кот") + 1) + "\n"
print(text)

# Слово для Гиннесса
print(max([len(i) for i in input().split()]))

# Комментарии в программе
sp = []
for i in range(int(input()[1:])):
    code = input()
    if "#" in code:
        flag = code.index("#")
        code = "".join(code[:flag])
    sp.append(code)
for i in range(len(sp)):
    print(sp[i].rstrip())

# Маленький частотный анализ
# text = input().lower()
print(max(sorted(list(text.replace(" ", ""))), key=text.count))

# М-И-Р Б-У-Д-Е-Т Н-А-Ш
print(*["-".join(map(str.upper, i)) for i in input().split()])

# Польский калькулятор
sp = []
text = input().split()
for i in text:
    if i.isdigit() or (i[0] == "-" and i[1:].isdigit()):
        sp.append(int(i))
    else:
        b = sp.pop()
        a = sp.pop()
        if i == "+":
            sp.append(a + b)
        elif i == "-":
            sp.append(a - b)
        elif i == "*":
            sp.append(a * b)

itog = sp.pop()
print(itog)

# Домашняя работа
# Знаков без пробелов
print(len(input().replace(" ", "").replace("\t", "")))

# Длинношеееед
s = input().lower()
print(max(s.count(c) for c in set(s)))

# Пирамида из кубиков
for i in range(int(input())):
    number = [int(i) for i in input().split()]
    sp = []
    number_cop = number.copy()
    while number:
        if number[0] > number[-1]:
            sp.append(number[0])
            number.pop(0)
        else:
            sp.append(number[-1])
            number.pop()
    if sp != sorted(number_cop, reverse=True):
        print("НЕТ")
    else:
        print(" ".join([str(i) for i in sorted(sp, reverse=True)]))

# Дополнительные задачи
# Средние в статистике
numbers = list(map(float, input().split()))
numbers.sort()
print(
    sum(numbers) / len(numbers),
    (numbers[len(numbers) // 2] + (numbers[len(numbers) // 2 + len(numbers) % 2 - 1]))
    / 2,
)

# Модные средние в статистике
numbers = list(map(int, input().split()))
snumbers = sorted(numbers)
med = snumbers[len(numbers) // 2]
kol = {}
for num in set(numbers):
    kol[num] = numbers.count(num)
mkol = max(kol.values())
moda = [num for num, count in kol.items() if count == mkol][0]
print(med, moda)


# Парадоксы статистики - не засчитало
def paradoks():
    def medi(arr):
        arr.sort()
        return arr[len(arr) // 2]

    def modi(arr):
        return max(arr, key=arr.count)

    num = int(input())
    med = []
    mod = []
    numbers = []
    for i in range(num):
        number = list(map(int, input().split()))
        numbers.extend(number)
        med.append(medi(number))
        mod.append(modi(number))
    print(*med)
    print(*mod)
    print(medi(med))
    print(modi(mod))
    print(medi(numbers))
    print(modi(numbers))


paradoks()

# Кто последний?
number = int(input())
sp = []
for i in range(number):
    text = input()
    if text[:3] == "Кто":
        sp.append(text[19 : len(text) - 1])
    elif text[:3] == "Я т":
        sp.reverse()
        sp.append(text[23 : len(text) - 1])
        sp.reverse()
    elif text[:3] == "Сле":
        if len(sp) == 0:
            print("В очереди никого нет.")
        else:
            print("Заходит {}!".format(sp[0]))
            sp = sp[1:]

# Пристраиваемся в очередь
sp = []
sp1 = ["встала", "встал", "в", "очередь."]
sp2 = ["Привет,", "будет", "за", "тобой."]
number = int(input())
for i in range(number):
    text = input()
    if "встал" in text or "встала" in text:
        flag = ""
        for k in text.split():
            if k not in sp1:
                flag = flag + k + " "
        sp.append(flag.strip())

    elif "Привет," in text:
        a = text.split("! ")[0][8:]
        index = sp.index(a)
        flag = ""
        for k in text.split():
            if k not in sp2 and "!" not in k:
                if k == a:
                    flag += k + " "
                if k not in a:
                    flag += k + " "
        sp.insert(index + 1, flag.strip())

    elif "хватит" in text:
        b = text.split(", ")[0]
        sp.pop(sp.index(b))
for i in sp:
    print(i)


# Некорректные логины
sp = []
for i in list(map(str, input().split(","))):
    for k in list(i):
        if not k.isalnum() and k != "_":
            sp.append(i)
            break
sp.sort()
lsp = [len(i) for i in sp]
if lsp:
    n = max(lsp)
else:
    n = 0
for i in sp:
    a = n - lsp.pop(0)
    print(" " * a + i)
# Польский калькулятор - 2
sp = []
numbert = input().split()
for i in numbert:
    if i.isdigit() or i[1:].isdigit():
        sp.append(i)
    else:
        if i in ("+", "-", "*", "/"):
            el1, el2 = sp[-2], sp[-1]
            sp.pop(-1)
            r = eval(el1 + i + el2)
            if i == "/":
                r = int(el1) // int(el2)
            sp[-1] = str(r)
        else:
            if i == "~":
                sp[-1] = str(int(sp[-1]) * -1)
            elif i == "#":
                sp.append(sp[-1])
            elif i == "!":
                s = 1
                for i in range(2, int(sp[-1]) + 1):
                    s *= i
                sp[-1] = str(s)
            else:
                sp[-1], sp[-2], sp[-3] = sp[-3], sp[-1], sp[-2]
print(sp[-1])
