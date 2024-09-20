# Kлассная работа
# Бинго!
import random


def make_bingo():
    bingo_data = random.sample(range(1, 100), 24)
    bingo_data.insert(12, 0)
    return tuple(tuple(bingo_data[i:i + 5]) for i in [0, 5, 10, 15, 20])


# Выбор тайного друга
import sys
import random


def choose_friends():
    name_and_last_name = list(map(str.strip, sys.stdin))
    random.shuffle(name_and_last_name)
    a = 1
    for i in range(0, len(name_and_last_name)):
        if i == len(name_and_last_name) - 1:
            print(name_and_last_name[i], ' - ', name_and_last_name[0])
        else:
            print(name_and_last_name[i], ' - ', name_and_last_name[a])
            a += 1


# Генератор визуально различимых паролей (базовый)
# import random
# import string
#
#
# def generate_password(m):
#     pas = string.ascii_letters + string.digits
#     danger_char = 'lIoO01'
#     chars = ''.join([char for char in pas if char not in danger_char])
#     return ''.join(random.choice(chars) for i in range(m))
#
#
# def main(n, m):
#     list_passw = set()
#     while len(list_passw) < n:
#         list_passw.add(generate_password(m))
#     return list(list_passw)
#
#
# # Дни рождения друзей
# import datetime as dt
#
# count_days = int(input())
# my_date = dt.datetime.now()
#
# new_date = dt.timedelta(days=count_days) + my_date
# print(new_date.day, new_date.month)

# Домашняя работа
# Генератор визуально различимых паролей (A)
from random import sample

symbols_without_prohibitions = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'


def generate_password(m):
    return ''.join(sample(symbols_without_prohibitions, m))


def main(n, m):
    password = set()
    while len(password) < n:
        password.add(generate_password(m))
    return password


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")

# Генератор визуально различимых паролей (B)
import random


def generate_password(m):
    upper = "ABCDEFGHJKLMNPQRSTUVWXYZ"
    lower = "abcdefghjkmnpqrstuvwxyz"
    digits = "23456789"
    symbols = lower + upper + digits

    password = [random.choice(lower), random.choice(upper), random.choice(digits)]
    while len(password) < m:
        password.append(random.choice(symbols))
    random.shuffle(password)
    return "".join(password)


def main(n, m):
    passwords = []
    while len(passwords) < n:
        password = generate_password(m)
        if password not in passwords:
            passwords.append(password)
    return passwords


# Биоритмы
import math
from datetime import datetime


def calculate_biorhythm(birth_date, target_date):
    physical = 23
    emotional = 28
    intellectual = 33

    days = (target_date - birth_date).days

    physical_biorhythm = math.sin((2 * math.pi * days) / physical) * 100
    emotional_biorhythm = math.sin((2 * math.pi * days) / emotional) * 100
    intellectual_biorhythm = math.sin((2 * math.pi * days) / intellectual) * 100

    return physical_biorhythm, emotional_biorhythm, intellectual_biorhythm


def parse_date(date_str):
    return datetime.strptime(date_str, '%d.%m.%Y')


birth_date_str = input().strip()
target_date_str = input().strip()

birth_date = parse_date(birth_date_str)
target_date = parse_date(target_date_str)

physical, emotional, intellectual = calculate_biorhythm(birth_date, target_date)

print(round(physical, 2))
print(round(emotional, 2))
print(round(intellectual, 2))

# Дополнительные задачи
# Найти приближённое значение Пи

# Генератор визуально различимых паролей (A + B)

# Коровы и быки. Секретный уровень

# Генерация текстов
