# Множества
# Классная работа

# Города
number = int(input())
history = set()
c = 0
k = 0
while k == 0:
    if c == number:
        b = input()
        break
    else:
        a = input()
    c = c + 1
    history.add(a)
if b not in history:
    print('OK')
else:
    print('TRY ANOTHER')

# Поездка на автобусе
history = set()
i = 1
b = False
while True:
    number = input()
    if i == 1:
        if number == '':
            i += 1
        else:
            history.add(number)
    else:
        if number in history and i == 2:
            b = True
            print(number)
        elif number == '':
            break
if not b:
    print('EMPTY')

# Языки - 0
number_angl = int(input())
number_nem = int(input())
angl = set()
nem = set()

for i in range(number_angl):
    familia = input()
    angl.add(familia)
for i in range(number_nem):
    familia = input()
    nem.add(familia)

angl_nem = angl.union(nem)
nemec = len(angl_nem) - number_angl
anglisk = len(angl_nem) - number_nem
english_german = nemec + anglisk

if english_german > 0:
    print(english_german)
else:
    print('NO')

# Языки – 1
english = int(input())
german = int(input())
lastnames = set()
yasiki = set()
for i in range(english + german):
    lastname = input()
    if lastname in yasiki:
        lastnames.add(lastname)
    else:
        yasiki.add(lastname)
a = yasiki - lastnames
if not a:
    print('NO')
else:
    print(len(a))

# Языки - 2
children = set()
a = set()
nem = int(input())
fr = int(input())
angl = int(input())
k = 0
for i in range(nem + fr + angl):
    name = input()
    if name in children:
        k += 1
        a.add(name)
    children.add(name)
if (nem == angl == fr) and len(children) == nem:
    print('NO')
else:
    if len(a) + k > 0:
        if (len(a) + k) % 2 != 0:
            print((len(a) + k) % 2)
        else:
            print((len(a) + k) // 2)
    else:
        print('NO')

# Домашняя работа

# Книги на лето
knig_dom = set()
knig_dom_kol = int(input())
knig_leto = set()
knig_leto_kol = int(input())
for i in range(knig_dom_kol):
    kniga = input()
    knig_dom.add(kniga)
for i in range(knig_leto_kol):
    kniga = input()
    knig_leto.add(kniga)
    if kniga in knig_dom:
        print('YES')
    else:
        print('NO')

# Посещаемость
uchen = set()
a = int(input())
b = int(input())
for k in range(b):
    uchen.add(input())
for k in range(a - 1):
    n = set()
    for i in range(int(input())):
        n.add(input())
    uchen = uchen & n
for i in uchen:
    print(i)

# Однофамильцы
number = int(input())
a = set()
b = set()
for i in range(number):
    lastname = input()
    if lastname in a:
        b.add(lastname)
    else:
        a.add(lastname)
itogo = a - b
kol = number - len(itogo)
print(kol)

# Дополнительные задачи

# Рецепты
ingred = set()
ingred_eat = set()
number_products_hold = int(input())
for i in range(number_products_hold):
    ingred.add(input())
number_recepts = int(input())
for i in range(number_recepts):
    products_name = input()
    number_ingred = int(input())
    flag = True
    for j in range(number_ingred):
        ingred_eat.add(input())
    for k in ingred_eat:
        if not (k in ingred):
            flag = False
    if flag:
        print(products_name)
    ingred_eat = set()

# Новые блюда
menu = set()
menu_usesese = set()
for i in range(int(input())):
    menu.add(input())
for i in range(int(input())):
    for k in range(int(input())):
        menu_usesese.add(input())
print(*(menu - menu_usesese), sep='\n')

# Лекарственные травы
number = int(input())
sp = set()
for i in range(number):
    for j in range(int(input())):
        ingr = input()
        if ingr not in sp:
            sp.add(ingr)
for lek in sp:
    print(lek)

# Палитра
kol = 0
sp = set()
sp2 = set()
for i in range(int(input())):
    for k in range(int(input())):
        a = input()
        ((sp.add(a)), kol := kol + 1) if a in sp2 else sp2.add(a)
print(lennn := len(sp), kol + lennn)

# Антиматерия
sp1 = set()
sp2 = set()
sp3 = set()
while (s := input()) != '':
    k = int(s)
    (sp3 := sp3 | (sp1 & sp2), sp1 := sp1 | sp2, sp2.clear()) if k == -1 else sp2.add(k)
print(*(sp1 - sp3))
