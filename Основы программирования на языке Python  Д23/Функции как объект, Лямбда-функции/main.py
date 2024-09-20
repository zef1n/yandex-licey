# Kлассная работа
# Функция в функции
def function(*data, func):
    return func(data)


# Набор юного арифметика
def arithmetic_operation(operation):
    if operation == '+':
        return lambda x, y: x + y
    elif operation == '-':
        return lambda x, y: x - y if x >= y else -(y - x)
    elif operation == '*':
        return lambda x, y: x * y
    elif operation == '/':
        return lambda x, y: x / y


# Просто map
def simple_map(transformation, values):
    res = []
    for i in values:
        c = transformation(i)
        res.append(c)
    return res


# Комбинируй и властвуй
# print
(sum(map(lambda n: n ** 2, filter(lambda n: not n % 9, range(10, 100)))))


# Голографическая Вселенная
def hologram(*args, transformation=1):
    if transformation == 1:
        return list(map(lambda x: x.title(), args))
    elif transformation == 2:
        return list(map(lambda x: ''.join(x[i] for i in range(len(x)) if i % 2 == 0), args))
    elif transformation == 3:
        return list(map(lambda x: str(len(x)), args))
    elif transformation == 4:
        return list(map(lambda x: ''.join(sorted(set(x))) if len(x) % 2 != 0 else x, args))


# Домашняя работа
# Мимикрия
transformation = lambda x: x

# Коллбэки
consonantal = ['b', 'c', 'd', 'f', 'g', 'h',
               'j', 'k', 'l', 'm', 'n', 'p',
               'q', 'r', 's', 't', 'v', 'w',
               'x', 'z']
vowel = ['a', 'e', 'i', 'o', 'u', 'y']


def ask_password(login, password, success, failure):
    consonantal_password = list(map(lambda x: x.lower(), filter(lambda x: x.lower() in consonantal, password)))
    vowel_password = list(map(lambda x: x.lower(), filter(lambda x: x.lower() in vowel, password)))
    consonantal_login = list(map(lambda x: x.lower(), filter(lambda x: x.lower() in consonantal, login)))
    if len(vowel_password) == 3 and (consonantal_password == consonantal_login):
        success(login)
        return True, ''
    if len(vowel_password) != 3 and (consonantal_password == consonantal_login):
        failure(login, "Wrong number of vowels")
        return False, 'Wrong number of vowels'
    if len(vowel_password) == 3 and (consonantal_password != consonantal_login):
        failure(login, "Wrong consonants")
        return False, "Wrong consonants"
    if len(vowel_password) != 3 and (consonantal_password != consonantal_login):
        failure(login, "Everything is wrong")
        return False, "Everything is wrong"


def main(login, password):
    def success(login):
        return

    def failure(login, err):
        return

    log, err = ask_password(login, password, success, failure)
    if log:
        print('Привет, ' + login.lower() + '!')
    else:
        print('Кто-то пытался притвориться пользователем ' + login.lower() + ', но в пароле '
                                                                             'допустил ошибку: ' + err.upper() + '.')


# Самая далёкая планета

# Дополнительные задачи
# Пам-парам парам-пам парам

# Астроида

# Все равны, как на подбор

# Соответствие

# Таблица операции
