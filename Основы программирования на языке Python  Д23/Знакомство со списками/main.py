# Kлассная работа
# Список покупок
number = int(input())
list = []
for i in range(number):
    list.append(input())
for number in list:
    print(number)

# Пра-пра-пра-Яндекс
itog = []
for i in range(int(input())):
    itog.append(input())
find = input()
for i in itog:
    if find in i:
        print(i)

# Буква каждого слова
listtt = []
number = int(input())
for i in range(number):
    listtt.append(input())
number1 = int(input())
for i in range(number):
    c = listtt[i]
    if len(c) >= number1:
        print(c[number1 - 1], end='')

# Автоматическое объявление
number = int(input())
word = []
for i in range(number):
    word.append(input())
number2 = int(input())
for k in range(number2):
    number3 = int(input())
    print(word[number3 - 1])

# Супы
sups = ["щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански"]
number = int(input())
n = -1
for i in range(number):
    if n != 4:
        n += 1
        print(sups[n])
    else:
        n = 0
        print(sups[n])

# Инвестиционный фонд
number = int(input())
sp = []
for i in range(number):
    ch = int(input())
    sp.append(ch)
    print(ch, sep='\n')
print()
for k in range(number):
    a = sp[k] * 3
    print(a, sep='\n')

# Пра-пра-пра-Яндекс - 2
number = int(input())
inpsearch = []
fdsearch = []
f = False
for i in range(number):
    fdsearch.append(input())
num1 = int(input())
for i in range(num1):
    inpsearch.append(input())
for i in fdsearch:
    for k in inpsearch:
        if k in i:
            f = True
        else:
            f = False
            break
    if f:
        print(i)

# От и до
number = int(input())
sp = []
summa = 0
for i in range(number):
    sp.append(input())
a = int(input())
b = int(input())
for i in range(a - 1, b):
    summa += int(sp[i])
print(summa)

# Домашняя работа
# Белый список
belsp = []
for i in range(int(input())):
    belsp.append(input())
poisk = []
for k in range(int(input())):
    poisk.append(input())
for n in poisk:
    if n in belsp:
        print(n)

# Не бином Ньютона
number = []
num = int(input())
for i in range(num):
    number.append(int(input()))
for i in range(num - 1):
    print(number[i] + number[i + 1])

# Проверка чека
number = input()
sp = []
sp2 = []
bag = 0
vesh = int(number[:4])
itog = int(number[4:])
for i in range(vesh):
    a = input()
    cenaaa = int(a[0:7])
    kolvo = int(a[8:12])
    summaaa = int(a[13:18])
    if cenaaa * kolvo != summaaa:
        sp.append(i + 1)
    summ1 = kolvo * cenaaa
    sp2.append(summ1)
for i in sp2:
    bag += i
print(itog - bag)
for i in sp:
    print(i, end=' ')

# Дополнительные задачи
# Подробный список покупок
sp_sum_pokup = []
sp_pokup = []
number = int(input())
for i in range(number):
    pokup = input()
    sp_pokup.append(pokup)
    sum_pokup = input()
    sp_sum_pokup.append(sum_pokup)
for k in range(number - 1, -1, -1):
    print(sp_pokup[k], sp_sum_pokup[k])

# RLE
a = input()
slovo = a[0]
kol = 1
for slov in a[1:]:
    if slovo == slov:
        kol += 1
    else:
        print(kol, slovo)
        slovo = slov
        kol = 1
print(kol, slovo)

# Крупные буквы
alfa = {'A': [' *   ', '* *  ', '***  ', '* *  ', '* *  '],
        'B': ['**   ', '* *  ', '**   ', '* *  ', '**   '],
        'C': [' *   ', '* *  ', '*    ', '* *  ', ' *   '],
        'D': ['**   ', '* *  ', '* *  ', '* *  ', '**   '],
        'E': ['***  ', '*    ', '**   ', '*    ', '***  '],
        'F': ['***  ', '*    ', '**   ', '*    ', '*    '],
        'G': [' **  ', '*    ', '* *  ', '* *  ', ' **  '],
        'H': ['* *  ', '* *  ', '***  ', '* *  ', '* *  '],
        'I': ['***  ', ' *   ', ' *   ', ' *   ', '***  '],
        'J': [' **  ', '  *  ', '  *  ', '* *  ', ' *   '],
        'K': ['* *  ', '**   ', '*    ', '**   ', '* *  '],
        'L': ['*    ', '*    ', '*    ', '*    ', '***  '],
        'M': ['* *  ', '***  ', '***  ', '***  ', '* *  '],
        'N': ['* *  ', '***  ', '***  ', '* *  ', '* *  '],
        'O': ['***  ', '* *  ', '* *  ', '* *  ', '***  '],
        'P': ['***  ', '* *  ', '***  ', '*    ', '*    '],
        'Q': ['***  ', '* *  ', '* *  ', '***  ', '***  '],
        'R': ['**   ', '* *  ', '**   ', '* *  ', '* *  '],
        'S': [' **  ', '*    ', ' *   ', '  *  ', '**   '],
        'T': ['***  ', ' *   ', ' *   ', ' *   ', ' *   '],
        'U': ['* *  ', '* *  ', '* *  ', '* *  ', '***  '],
        'V': ['* *  ', '* *  ', '* *  ', '* *  ', ' *   '],
        'W': ['* *  ', '* *  ', '* *  ', '***  ', '* *  '],
        'X': ['* *  ', '* *  ', ' *   ', '* *  ', '* *  '],
        'Y': ['* *  ', '* *  ', '* *  ', ' *   ', ' *   '],
        'Z': ['***  ', '  *  ', ' *   ', '*    ', '***  ']}
slov = input()
for i in range(5):
    for n in slov:
        print(alfa.get(n)[i], end='')
    print()

# Периодическая десятичная дробь
sp = []
itog = []
number = int(input())
a = 1
while a not in sp:
    sp.append(a)
    itog.append(10 * a // number)
    a = 10 * a % number
print(*itog[sp.index(a):], sep='')

# Масштабирование
number = int(input())
number2 = int(input())
sp = [input() for i in range(number)]
for i in sp[::2]:
    for k in i[::2]:
        print(k, end='')
    print()
# :)
