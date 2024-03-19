# Kлассная работа
# Существительные
import pymorphy3
import sys

newdb = ' '
nc = {}
morph = pymorphy3.MorphAnalyzer()
db = list(map(str.strip, sys.stdin))

for txt in db:
    for i in txt:
        if i.lower() not in ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя' or i == '\n' or i == '\v' or i == '\t':
            txt = txt.replace(i, ' ').lower()
    newdb += txt + ' '
newdb = newdb.split()

for k in newdb:
    p = morph.parse(k)[0]
    if p.tag.POS == 'NOUN' and p.score > 0.5:
        nc[p.normal_form] = nc.get(p.normal_form, 0) + 1
nc = [x[0] for x in sorted(nc.items(), key=lambda x: (x[1], x[0]), reverse=True)]

print(*nc[:10])

# Формы глаголов

# Домашняя работа
# 99 бутылок кваса

# Склоняй меня полностью

# Дополнительные задачи
# Спрягай меня полностью

# Оно живое!
