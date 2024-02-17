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
# sp = []
# while True:
#     number = int(input())
#     sp.append(int(number))
#
# if len(sp) == 0:
#     print(-1)
# else:
#     print(sum(sp) / len(sp))


# Ваши комментарии


# Сортировка по делителям
# sp = list()
# while (num := int(input())) != 0:
#     count = 2
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             count += 2
#     if i * i == num:
#         count -= 1
#     sp.append((num, count))
#
# sp.sort(key=lambda x: (x[1], x[0]))
# print(sp)

# Домашняя работа
# Есть ли 0
print(any(not all(map(int, x.split())) for x in input().split('\n')))

# Сумма чисел в строке
# Гематрия по-английски
# Дополнительные задачи
# Оформленные комментарии
# Циклический сдвиг строки
# Ох уж эти анаграммы
