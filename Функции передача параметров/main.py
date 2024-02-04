# Kлассная работа
# Электронный попугай
def parrot(phrase, phrasess={}):
    if phrase in phrasess:
        print(phrase)
    else:
        phrasess[phrase] = True


# Счёт за обед
daily_food = [0, 150, 150]


def count_food(days):
    return sum([daily_food[i - 1] for i in days])


# Покажите отличие
# sp_sort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# sp_sort.sort()
# print("Список после использования метода sort():", sp_sort)
#
# sp = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# sp_sorted = sorted(sp)
#
# print("Отсортированный список с использованием функции sorted():", sp_sorted)
# print("Исходный список после использования функции sorted():", sp)


# Продолжите ряд
def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)


# Зеркало
def mirror(arr):
    mirrored_part = arr[::-1]
    arr.extend(mirrored_part)


# Фрактальный список — 1

fractal = [0, 1, 2, 3]
fractal = [0, fractal, fractal, 2]

# От перестановки мест

# Что ты имела в виду?

# Домашняя работа
# Числа в строке

# Билеты

# Транспонирование

# Дополнительные задачи
# Обмен личностями

# Остатки

# Фрактальный список – 2

# Печать фрактала

# Фрактальное дерево
