# Kлассная работа
# Словарный порядок
# print(*sorted(input().split(), key=str.lower))

# Отличники
# sp = list()
# c = int(input())
# for num in range(c):
#     sp2 = set()
#     for i in range(int(input())):
#         k = input().split()
#         if k[1] == '5':
#             sp2.add(k[1])
#     sp.append(sp2)
# if all(map(lambda x: x == {'5'}, sp)) and len(sp) == c:
#     print('ДА')
# else:
#     print('НЕТ')
# Суммарный цифровой минимум
# import sys
#
# print(min(iter(input, ''), key=lambda tas: (sum(map(int, tas)), -len(tas), int(tas))))

# Средний рост


# Ваши комментарии
import sys

# Лямбда-функция, которая возвращает True, если строка содержит только комментарий
is_comment_only = lambda line: line.strip().startswith('#')

# Считывание строк из стандартного ввода
lines = sys.stdin.readlines()

# Подсчет строк, удовлетворяющих условию
count = sum(map(is_comment_only, lines))

print(count)


# Сортировка по делителям
# Домашняя работа
# Есть ли 0
# Сумма чисел в строке
# Гематрия по-английски
# Дополнительные задачи
# Оформленные комментарии
# Циклический сдвиг строки
# Ох уж эти анаграммы
