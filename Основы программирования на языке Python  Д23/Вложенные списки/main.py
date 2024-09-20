# Kлассная работа
# Окно
sp = [int(input()) for i in range(int(input()))]
minimal = int(input())
maximum = int(input())
print(*[i for i in sp if minimal <= i <= maximum], sep='\n')

# Сборка текста
number = (map(int, input().split()))
text = list(map(str.lower, input().split()))
print(' '.join([text[i - 1] for i in number]).capitalize())

# bf--
text = input()
sp = [0] * 30000
k = 0
sp2 = []
for i in text:
    if i == '>':
        k = (k + 1) % 30000
    elif i == '<':
        k = (k - 1) % 30000
    elif i == '+':
        sp[k] = (sp[k] + 1) % 256
    elif i == '-':
        sp[k] = (sp[k] - 1) % 256
    elif i == '.':
        sp2.append(sp[k])
for j in sp2:
    print(j)

# Считать и вывести таблицу
number = int(input())
number2 = int(input())
table = []
sp2 = []
for i in range(number):
    sp2.clear()
    table.append(list(sp2))
    for k in range(number2):
        table[i].append(input())
for i in range(len(table)):
    print("\t".join(table[i]))

# Считать и вывести таблицу — 2
number = int(input())
number2 = int(input())
sp = list()
for i in range(number):
    sp2 = []
    for k in range(number2):
        sp2.append(input())
    sp.append(sp2)
for i in range(number):
    for k in range(number2):
        print(sp[i][k], end='\t')
    print()
print()
for i in range(number2):
    for k in range(number):
        print(sp[k][i], end='\t')
    print()

# CSV
sp = []
for i in range(int(input())):
    a = input().split(',')
    sp.append(a)
for i in range(int(input())):
    p = input().split(',')
    x, y = int(p[0]), int(p[1])
    print(sp[x][y])

# Бином Ньютона, или Треугольник Паскаля
sp = [1]
for i in range(int(input())):
    print(*sp)
    a = [1]
    a += [sp[k] + sp[k + 1] for k in range(len(sp) - 1)] + [1]
    sp = a

# Нолики-крестики
flag = False
number = int(input())
sp = [input() for _ in range(number)]
for i in sp:
    if 'ooo' in i:
        print('o')
        flag = True
        break
    elif 'xxx' in i:
        print('x')
        flag = True
        break
if not flag:
    sp2 = []
    s = ' '
    for k in range(number):
        for i in sp:
            s += i[k]
        sp2.append(s)
        s = ' '
    for i in sp2:
        if 'ooo' in i:
            print('o')
            flag = True
            break
        elif 'xxx' in i:
            print('x')
            flag = True
            break
if not flag:
    print('-')

# Домашняя работа
# Симметризовать таблицу
number = int(input())
table = [[0] * number for i in range(number)]
for i in range(1, number):
    sp = [int(k) for k in input().split()]
    for k in range(len(sp)):
        table[i][k] = sp[k]
        table[k][i] = sp[k]
for itog in table:
    print(*itog)

# Диагонали наоборот
number = int(input())
sp = [list(map(int, input().split(', '))) for i in range(number)]
a = 0
for k in range(number):
    sp[k][k], sp[k][~k] = sp[k][~k], sp[k][k]
    a += sp[k][k] + sp[k][~k]
for itog in sp:
    print(*itog)
print(a)

# bf
text = input()
sp = [0 for i in range(30001)]
p = 0
k = 0
while k < len(text):
    if text[k] == ">":
        p = p + 1
    elif text[k] == "<":
        p = p - 1
    elif text[k] == ".":
        print(sp[p])
    elif text[k] == "-":
        sp[p] = sp[p] - 1
        if sp[p] < 0:
            sp[p] = 255
    elif text[k] == "+":
        sp[p] = sp[p] + 1
        if sp[p] > 255:
            sp[p] = 0
    elif text[k] == '[':
        if sp[p] == 0:
            n = 1
            i = k + 1
            while True:
                if text[i] == '[':
                    n += 1
                if text[i] == ']':
                    n -= 1
                if n == 0:
                    k = i
                    break
                i += 1
    elif text[k] == ']':
        n = -1
        i = k - 1
        while True:
            if text[i] == ']':
                n -= 1
            if text[i] == '[':
                n += 1
            if n == 0:
                k = i - 1
                break
            i -= 1
    k += 1

# Дополнительные задачи
# Разные разности
n = 0
number = int(input())
sp = []
summm = []
for i in range(number):
    c = int(input())
    summm.append(c)
raz = summm
raz.reverse()
for i in summm:
    n = i
    for k in raz:
        razn = n - k
        sp.append(razn)
sp = set(sp)
sp = list(sp)
sp.sort()
for i in sp:
    print(i, end='\n')

# Считать и вывести таблицу — 3
rads = int(input())
stoblc = int(input())
table = []
for i in range(rads):
    rad = []
    for k in range(stoblc):
        rad.append(input())
    table.append(rad)
for i in range(rads):
    for k in range(stoblc):
        print(table[i][k], end='\t')
    print()

# Экономия
number = int(input())
sp = [[]]
for i in range(number - 1):
    sp.append([int(z) for z in input().split()])
stncia = input().split()
num1 = int(stncia[0])
num2 = int(stncia[1])
n = sp[max(num1, num2)][min(num1, num2)]
k = -1
for i in range(number):
    if i != num1 and i != num2:
        if n > sp[max(num1, i)][min(num1, i)] + sp[max(i, num2)][min(i, num2)]:
            n = sp[max(i, num2)][min(i, num2)] + sp[max(i, num2)][min(i, num2)]
            k = i
if k != -1:
    print(k)
else:
    print(num1)

# Где экономия?
number = int(input())
sp = [[]] + [list(map(int, input().split())) for z in range(number - 1)]
for k in range(0, number - 1):
    for j in range(k + 1, number):
        a = sp[max(k, j)][min(k, j)]
        b = -1
        for i in range(number):
            if i != k and i != j:
                ln = sp[max(i, k)][min(i, k)] + sp[max(i, j)][min(i, j)]
                a, b = (ln, i) if (a > ln) else (a, b)
        if b != -1:
            print(k, j)

# Сумма в виде Н
number = int(input())
maxx = 0
a = 0
sp = [list(map(int, input().split())) for i in range(number)]
for i in range(1, number - 1):
    for k in range(1, number - 1):
        a = sp[i][k] + sp[i][k - 1] + sp[i][k + 1] + sp[i - 1][k + 1]
        a += sp[i + 1][k + 1] + sp[i - 1][k - 1] + sp[i + 1][k - 1]
        if maxx < a:
            maxx = a
print(maxx)

# Бактериям — бой!
number = int(input())
sp = [([0] * number) for i in range(number)]
for i in range(number):
    for k in range(number):
        sp[i][k] = int(input())
num = int(input())
for i in range(num):
    b = int(input())
    a = int(input())
    if sp[a][b] >= 8:
        sp[a][b] -= 8
    else:
        sp[a][b] = 0
    if a > 0:
        if sp[a - 1][b] >= 4:
            sp[a - 1][b] -= 4
        else:
            sp[a - 1][b] = 0
        if b > 0:
            if sp[a - 1][b - 1] >= 4:
                sp[a - 1][b - 1] -= 4
            else:
                sp[a - 1][b - 1] = 0
        if b < (number - 1):
            if sp[a - 1][b + 1] >= 4:
                sp[a - 1][b + 1] -= 4
            else:
                sp[a - 1][b + 1] = 0
    if a < (number - 1):
        if sp[a + 1][b] >= 4:
            sp[a + 1][b] -= 4
        else:
            sp[a + 1][b] = 0
        if b > 0:
            if sp[a + 1][b - 1] >= 4:
                sp[a + 1][b - 1] -= 4
            else:
                sp[a + 1][b - 1] = 0
        if b < (number - 1):
            if sp[a + 1][b + 1] >= 4:
                sp[a + 1][b + 1] -= 4
            else:
                sp[a + 1][b + 1] = 0
    if b > 0:
        if sp[a][b - 1] >= 4:
            sp[a][b - 1] -= 4
        else:
            sp[a][b - 1] = 0
    if b < number - 1:
        if sp[a][b + 1] >= 4:
            sp[a][b + 1] -= 4
        else:
            sp[a][b + 1] = 0
for i in range(number):
    for k in range(number):
        print(sp[i][k], end=' ')
    print()

# Считать и отсортировать таблицу
rad = int(input())
stolbc = int(input())
for i in range(rad):
    sp = [input() for k in range(stolbc)]
    if i != 0 and i != rad - 1:
        sp = sorted(sp)
    for i in range(len(sp)):
        if i != len(sp) - 1:
            print(sp[i], end='\t')
        else:
            print(sp[i])
