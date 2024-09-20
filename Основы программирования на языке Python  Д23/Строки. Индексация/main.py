# Строки. Индексация
# Классная работа

# Скажите а
words = input()
letter = words[0]
if letter == 'а':
    print('ДА')
else:
    print('НЕТ')

# Пятая буква
word = input()
if len(word) >= 5:
    print(word[4])
else:
    print('НЕТ')

# Последняя буква
words = input()
letter = words[-1]
print(letter)

# Игра в города: один раунд
word = input()
word2 = input()
if word[-1] == word2[0]:
    print('ВЕРНО')
else:
    print('НЕВЕРНО')

# Игра в города
word = input()
while True:
    word2 = input()
    if word[-1] != word2[0]:
        print(word2)
        break
    word = word2

# Сколько-то букв по вертикали
word = input()
print(*word, sep='\n')

# Начинающий шифровальщик
words = input()
for i in range(len(words)):
    print(ord(words[i]), end='')
    if i != (len(words) - 1):
        print(', ', end='')

# Бурсацкое развлечение
number = int(input())
while str(number)[0] != '1' and number <= 1000000000:
    number = number * int(str(number)[0])
print(number)

# Меденнее
word = input()
for i in range(len(word)):
    print(word[i] * (i + 1), end='')

# Какая-то там буква
word = input()
numbers = int(input())
len_word = len(word)
if numbers > len_word:
    print('ОШИБКА')
elif numbers <= 0:
    print('ОШИБКА')
else:
    print(word[numbers - 1])

# Цезарь его знает
alfavit = "АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
znaki = '1234567890@!?,.~`[]<>#–—$_&-+()/*":;% '
chag_shifra = int(input())
shifr = str(input())
for i in range(len(shifr)):
    for k in range(len(alfavit)):
        if shifr[i] == alfavit[k]:
            k += chag_shifra + chag_shifra
            if k > 64:
                k = k - 64
                print(alfavit[k], end="")
            else:
                print(alfavit[k], end="")
    else:
        if shifr[i] in znaki:
            print(shifr[i], end="")

# Дополнительные задачи
# Скажите а (заглавное)
print((lambda a: 'ДА' if a[0] == 'а' or a[0] == 'А' else 'НЕТ')(input()))

# Последняя буква 2
print(input()[-1])

# Продолжайте говорить «А»
while True:
    word = input()
    a = (word[0])
    if a == "а" or a == "А":
        print(word)
    elif a != "а" or a != "А":
        break

# Игра в города: мягкий знак
a = input()
b = input()
if a[-1] == 'ь':
    if b[0] == a[-2]:
        print('ВЕРНО')
    else:
        print('НЕВЕРНО')
else:
    if b[0] == a[-1]:
        print('ВЕРНО')
    else:
        print('НЕВЕРНО')

# Ххооллоодд
sp = [i * 2 for i in input()]
print(''.join(sp))

# Розенкранц и Гильденстерн меняют профессию
a = input()
b = 0
n = 0
maximum = 0
for i in a:
    if i == 'о' and n != 0:
        b = 1
        n = 0
    elif i == 'о' and n == 0:
        b += 1
    else:
        n = 1
    if b > maximum:
        maximum = b
print(maximum)
