# Kлассная работа
# Камень, ножницы, бумага
rules = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}

first = input().strip().lower()
second = input().strip().lower()


if first == second:
    print("ничья")
elif rules[first] == second:
    print("первый")
else:
    print("второй")
# Точки на плоскости
quadrant_counts = {
    "I": 0,
    "II": 0,
    "III": 0,
    "IV": 0
}
points = []

for i in range(int(input())):
    x, y = map(int, input().split())

    if x == 0 or y == 0:
        points.append(f"({x}, {y})")
    else:
        if x > 0 and y > 0:
            quadrant_counts["I"] += 1
        elif x < 0 and y > 0:
            quadrant_counts["II"] += 1
        elif x < 0 and y < 0:
            quadrant_counts["III"] += 1
        elif x > 0 and y < 0:
            quadrant_counts["IV"] += 1

for point in points:
    print(point)

result = ", ".join([f"{q}: {quadrant_counts[q]}" for q in ["I", "II", "III", "IV"]]) + "."

print(result)
# ГЕЗ, ЩЗКГУЯ!
alphabet = input().strip()
shift = int(input())
s = shift % len(alphabet)
print(f'{alphabet[s:] + alphabet[:s]} \n{alphabet} \n{alphabet[-s:] + alphabet[:-s]}')

# Репка
import sys

characters = sys.stdin.readline().strip().split(' -> ')
num = len(characters)
IndexName = {name: i for i, name in enumerate(characters)}

for i in range(int(sys.stdin.readline())):
    name = sys.stdin.readline().strip()
    idx = IndexName[name]

    if num == 1:
        print(name)

    elif idx == 0:
        print(f"{name} -> {characters[1]}")

    elif idx == num - 1:
        print(f"{characters[num - 2]} -> {name}")

    else:
        print(f"{characters[idx - 1]} -> {name} -> {characters[idx + 1]}")

# В фокусе
from PIL import Image

img = Image.open('image.png')
pix = img.load()
w, h = img.size
bg_color = pix[0, 0]


def find(pix, size, axis='x', direction='forward', bg_color=None):
    if axis == 'x':
        range_i = range(size[0]) if direction == 'forward' else range(size[0] - 1, -1, -1)
        for x in range_i:
            if any(pix[x, y] != bg_color for y in range(size[1])):
                return x
    elif axis == 'y':
        range_i = range(size[1]) if direction == 'forward' else range(size[1] - 1, -1, -1)
        for y in range_i:
            if any(pix[x, y] != bg_color for x in range(size[0])):
                return y
    return 0


left = find(pix, (w, h), axis='x', direction='forward', bg_color=bg_color)
right = find(pix, (w, h), axis='x', direction='backward', bg_color=bg_color)
top = find(pix, (w, h), axis='y', direction='forward', bg_color=bg_color)
bottom = find(pix, (w, h), axis='y', direction='backward', bg_color=bg_color)

cropped = img.crop((left, top, right + 1, bottom + 1))
cropped.save('res.png')

# Лепесток от телескопа, или спаниель в апельсинах

# Домашняя работа
# Камень, ножницы, бумага, ром, пират
choices = {
    "камень": {"ножницы", "ром"},
    "ножницы": {"бумага", "ром"},
    "бумага": {"камень", "пират"},
    "ром": {"бумага", "пират"},
    "пират": {"камень", "ножницы"}
}

player1 = input().strip().lower()
player2 = input().strip().lower()

if player1 == player2:
    print("ничья")
elif player2 in choices[player1]:
    print("первый")
else:
    print("второй")
# Ещё немного точек на плоскости
points = []
for i in range(n := int(input())):
    points.append(tuple(map(int, input().split())))
selected = [p for p in points if -abs(p[0]) < p[1] < abs(p[0])]
for p in selected:
    print(f"({p[0]}, {p[1]})")
if n > 0:
    left = min(points, key=lambda p: (p[0], points.index(p)))
    right = max(points, key=lambda p: (p[0], -points.index(p)))
    top = max(points, key=lambda p: (p[1], -points.index(p)))
    bottom = min(points, key=lambda p: (p[1], points.index(p)))
    print(
        f"left: ({left[0]}, {left[1]}) "
        f"\nright: ({right[0]}, {right[1]}) "
        f"\ntop: ({top[0]}, {top[1]}) "
        f"\nbottom: {bottom} ")
# :) <3

# Прикладная нумерология
from itertools import product
import sys

lin = sys.stdin.read().splitlines()


def sum_digits(n):
    return sum(int(d) for d in f"{n:02}")


happy_h = list(map(int, lin[0].split()))
happy = list(map(int, lin[1].split()))

h_s = {h: sum_digits(h) for h in happy_h}
min_s = {m: sum_digits(m) for m in happy}

itm_v = []
for h, m in product(happy_h, happy):
    if h_s[h] != min_s[m]:
        itm_v.append((h, m))

valid = sorted(itm_v)

for h, m in valid:
    print(f"{h:02}:{m:02}")

# Псевдояпонские имена
import sys

mapping = {
    'а': 'ка', 'б': 'зу', 'в': 'ру', 'г': 'джи', 'д': 'те',
    'е': 'ку', 'ё': 'ку', 'ж': 'зу', 'з': 'з', 'и': 'ки',
    'й': 'фу', 'к': 'ме', 'л': 'та', 'м': 'рин', 'н': 'то',
    'о': 'мо', 'п': 'но', 'р': 'ши', 'с': 'ари', 'т': 'чи',
    'у': 'мей', 'ф': 'лу', 'х': 'ри', 'ц': 'ми', 'ч': 'зи',
    'ш': 'ли', 'щ': 'ни', 'ъ': 'д', 'ы': 'хе', 'ь': 'ксе',
    'э': 'га', 'ю': 'до', 'я': 'ма'
}

name = sys.stdin.read().strip().lower()
jap_name = ''.join(mapping.get(char, '') for char in name)
if jap_name:
    jap_name = jap_name.capitalize()
print(jap_name)
# Пятнашки

# Дополнительные задачи
# Далеки
import sys

count = 0
for line in sys.stdin:
    if 'далек' in line.lower():
        count += 1
print(count)
# Далеки издалека
import sys

count = 0
for line in sys.stdin:
    words = line.lower().split()
    if any(word.startswith('далек') for word in words):
        count += 1
print(count)
# Далеки далеко
import sys

count = 0
text = {
    'далек', 'далеки', 'далека', 'далеков',
    'далеку', 'далекам', 'далеком', 'далеками',
    'далеке', 'далеках'
}
for line in sys.stdin:
    words = line.lower().replace('-', ' ').split()
    if any(word in text for word in words):
        count += 1
print(count)

# Вопросительное повествование без восклицаний
# Кабинеты из расписания
# Корпоративная почта
# Продавец мороженого
# Сапёр