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

# Уравнение прямой

# Таблица квадратов чисел

# Точка на прямой

# Крестики-нолики

# Решето Эратосфена

# Длинношеее
