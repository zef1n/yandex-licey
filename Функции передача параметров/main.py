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
sp_sort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sp_sort.sort()
print("Список после использования метода sort():", sp_sort)

sp = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sp_sorted = sorted(sp)

print("Отсортированный список с использованием функции sorted():", sp_sorted)
print("Исходный список после использования функции sorted():", sp)


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
fractal = []
fractal.extend([0, fractal, fractal, 2])


# От перестановки мест

# Что ты имела в виду?
numbers = [2, 5, 7, 7, 8, 4, 1, 6]
odd = []
even = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Четные числа:", even)
print("Нечетные числа:", odd)


# Домашняя работа
# Числа в строке
def from_string_to_list(string, container):
    numbers = [int(num) for num in string.split()]
    container.extend(numbers)


# Билеты
def allocation(data):
    not_alloc = []

    for rad, mest in data:
        if places[rad - 1][mest - 1] == 0:

            places[rad - 1][mest - 1] = 1
        else:
            not_alloc.append((rad, mest))
    return not_alloc


# Транспонирование
def transpose(matrix):
    stroki = len(matrix)
    koloni = len(matrix[0])
    tr_matrix = [[matrix[j][i] for j in range(stroki)] for i in range(koloni)]
    matrix.clear()
    matrix.extend(tr_matrix)

# Дополнительные задачи
# Обмен личностями

# Остатки

# Фрактальный список – 2

# Печать фрактала

# Фрактальное дерево
