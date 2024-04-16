# Kлассная работа
# Формальное приветствие
def great():
    name = input()
    lastname = input()
    print(f"Здравствуйте, {name} {lastname}.")


# Пробелы
def space_game(text):
    c = 0
    for i in text:
        if i == " ":
            c += 1
    if c % 2 == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")


# Какая четверть?
def quarter(xcoord, ycoord):
    if xcoord < 0 < ycoord:
        print('II четверть')
    elif xcoord and ycoord > 0:
        print('I четверть')
    elif xcoord < 0 and ycoord < 0:
        print('III четверть')
    elif xcoord > 0 > ycoord:
        print('IV четверть')


# Привет, как тебя там?
def who_are_you_and_hello():
    name = input()
    while True:
        if name.isalpha() and name[0].istitle() and name[1:].islower():
            break
        else:
            name = input()
    print(f'Привет, {name}!')


# Треугольник?
def triangle(a, b, c):
    if (a + b) > c and (c + b) > a and (a + c) > b:
        print('Это треугольник')
    else:
        print('Это не треугольник')


# Среднее значение
def print_average(arr):
    arr = arr or [0]
    print(sum(arr) / len(arr))


# Статистики
def print_statistics(arr):
    if not arr:
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
    else:
        nel = len(arr)
        mv = sum(arr) / nel
        minim = min(arr)
        maxim = max(arr)

        soort = sorted(arr)
        ser = nel // 2
        if nel % 2 == 0:
            med = (soort[ser - 1] + soort[ser]) / 2
        else:
            med = soort[ser]

        print(nel)
        print(mv)
        print(minim)
        print(maxim)
        print(med)


# Домашняя работа
# Улыбайтесь, господа!
def print_shrug_smile():
    print(':)')


def print_ktulhu_smile():
    print('{:€')


def print_happy_smile():
    print('(͡° ͜ʖ ͡°)')


# Скажи «пароль» и проходи
def ask_password():
    for i in range(0, 3):
        password = input()
        if password == 'password':
            print('Пароль принят')
            break
        elif i == 2:
            print('В доступе отказано')
    return


# Золотое сечение
def golden_ratio(i):
    x, y = 0, 1
    n = 1
    while n <= i:
        x, y = y, x + y
        n += 1
    print(y / x)


# Дополнительные задачи
# Правильная скобочная последовательность
# def bracket_check(text):
#     sp = []
#     for i in text:
#         if i == '(':
#             sp.append('(')
#         elif i == ')':
#             if not sp or sp[-1] != '(':
#                 print('NO')
#                 return
#             sp.pop()
#     if not sp:
#         print('YES')
#     else:
#         print('NO')

# Уравнение прямой
def equation(a, b):
    x1, y1 = float(a.split(';')[0]), float(a.split(';')[1])
    x2, y2 = float(b.split(';')[0]), float(b.split(';')[1])
    if x1 == x2:
        print(x1)
    else:
        if y1 == y2:
            print(y1)
        else:
            k = (y2 - y1) / (x2 - x1)
            print(k, y2 - k * x2)


# Таблица квадратов чисел !!!!
def squared(a, b, k):
    res = []
    for i in range(a, b + 1, 10):
        res.append([])
        for j in range(i, i + 10):
            if j ** 2 % k != 0:
                res[-1].append(j ** 2)


# Точка на прямой
def line(s, t):
    a = float(s.split('x')[0])
    b = float(s.split('x')[1])
    x = float(t.split(';')[0])
    y = float(t.split(';')[1])
    print(y == a * x + b)


# Крестики-нолики
def tic_tac_toe(field):
    lin = (*map("".join, field), *map("".join, zip(*field)),
           *map("".join, zip(*((k[num], k[-num - 1],) for num, k in enumerate(field)))))
    pobed = "x win" if "xxx" in lin else "0 win" if "000" in lin else "draw"
    print(pobed)


# Решето Эратосфена
def eratosthenes(n):
    sp1 = []
    sp2 = []

    if n < 4:
        return

    for i in range(2, n + 1, 1):
        sp1.append(i)

    while sp1:
        for i in sp1[1:]:
            if i % sp1[0] == 0:
                sp2.append(i)
                sp1.remove(i)
        sp1 = sp1[1:]

    for i in sp2:
        print(i, end=" ")


# Длинношеее
def print_long_words(text):
    text = text.lower()
    for i in text:
        if i not in ' абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz':
            text = text.replace(i, ' ')
    text1 = text.split()
    for z in text1:
        b = 0
        for k in z:
            b += 1 if k in 'аоэиуыеёюяaeiouy' else 0
        if b >= 4:
            print(z)
    return


print_long_words('Как и в прочих заданиях этого урока, в вашем решении функция должна быть определена, но не должна вызываться.')
