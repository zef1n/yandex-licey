# Классная работа
# Нобелевские лауреаты по литературе
laureats = {'Луиза Глюк': '2020', 'Петер Хандке': '2019', 'Ольга Токарчук': '2018', 'Кадзуо Исигуро': '2017',
            'Боб Дилан': '2016', 'Светлана Алексиевич': '2015', 'Патрик Модиано': '2014',
            'Элис Энн Манро': '2013', 'Мо Янь': '2012', 'Тумас Транстремер': '2011', 'Марио Варгас Льоса': '2010',
            'Герта Мюллер': '2009', 'Жан-Мари Гюстав Леклезио': '2008', 'Дорис Лессинг': '2007',
            'Орхан Памук': '2006', 'Гарольд Пинтер': '2005', 'Эльфрида Елинек': '2004', 'Джон Максвелл Кутзее': '2003',
            'Имре Кертес': '2002', 'Видиадхар Сураджпрасад Найпол': '2001',
            'Гао Синцзянь': '2000', 'Гюнтер Грасс': '1999', 'Жозе Сарамаго': '1998', 'Дарио Фо': '1997',
            'Вислава Шимборска': '1996', 'Шеймус Хини': '1995', 'Кэнзабуро Оэ': '1994', 'Дерек Уолкотт': '1992',
            'Надин Гордимер': '1991', 'Октавио Пас': '1990', 'Камило Хосе Села': '1989', 'Нагиб Махфуз': '1988',
            'Иосиф Бродский': '1987', 'Воле Шойинка': '1986', 'Клод Симон': '1985',
            'Ярослав Сейферт': '1984', 'Уильям Голдинг': '1983', 'Габриэль Гарсия Маркес': '1982',
            'Элиас Канетти': '1981', 'Чеслав Милош': '1980', 'Одисеас Элитис': '1979',
            'Исаак Башевис Зингер': '1978', 'Висенте Алейксандре': '1977', 'Сол Беллоу': '1976',
            'Эудженио Монтале': '1975', 'Эйвинд Йонсон': '1974', 'Харри Мартинсон': '1974',
            'Патрик Виктор Мартиндейл Уайт': '1973', 'Генрих Белль': '1972', 'Пабло Неруда': '1971',
            'Александр Исаевич Солженицын': '1970', 'Сэмюэл Беккет': '1969',
            'Ясунари Кавабата': '1968', 'Мигель Астуриас': '1967', 'Шмуэль Йозеф Агнон': '1966', 'Нелли Закс': '1966',
            'Михаил Александрович Шолохов': '1965', 'Жан-Поль Сартр': '1964',
            'Георгос Сеферис': '1963', 'Джон Стейнбек': '1962', 'Иво Андрич': '1961', 'Сен-Жон Перс': '1960',
            'Сальваторе Квазимодо': '1959', 'Борис Леонидович Пастернак': '1958',
            'Альбер Камю': '1957', 'Хуан Рамон Хименес': '1956', 'Хальдоур Кильян Лакснесс': '1955',
            'Эрнест Миллер Хемингуэй': '1954',
            'Уинстон Леонард Спенсер Черчилль': '1953', 'Франсуа Мориак': '1952', 'Пер Фабиан Лагерквист': '1951',
            'Бертран Рассел': '1950', 'Уильям Фолкнер': '1949', 'Томас Стернз Элиот': '1948', 'Андре Жид': '1947',
            'Герман Гессе': '1946',
            'Габриела Мистраль': '1945', 'Йоханнес Йенсен': '1944', 'Франс Эмиль Силланпя': '1939', 'Перл Бак': '1938',
            'Роже Мартен Дю Гар': '1937', 'Юджин ОНил': '1936', 'Луиджи Пиранделло': '1934',
            'Иван Алексеевич Бунин': '1933',
            'Джон Голсуорси': '1932', 'Эрик Карлфельдт': '1931', 'Синклер Льюис': '1930', 'Томас Манн': '1929',
            'Сигрид Унсет': '1928', 'Анри Бергсон': '1927', 'Грация Деледда': '1926', 'Джордж Бернард Шоу': '1925',
            'Владислав Станислав Реймонт': '1924',
            'Уильям Батлер Йитс': '1923', 'Хасинто Бенавенте - И - Мартинес': '1922', 'Анатоль Франс': '1921',
            'Кнут Гамсун': '1920', 'Карл Фридрих Георг Шпиттелер': '1919', 'Карл Адольф Гьеллеруп': '1917',
            'Хенрик Понтоппидан': '1917', 'Карл Густав Вернер фон Хейденстам': '1916', 'Ромен Роллан': '1915',
            'Рабиндранат Тагор': '1913', 'Герхардт Гауптман': '1912', 'Морис Метерлинк': '1911',
            'Пауль Йоханн Людвиг фон Хейзе': '1910', 'Сельма Лагерлеф': '1909',
            'Рудольф Кристоф Эйкен': '1908', 'Джозеф Редьярд Киплинг': '1907', 'Джозуэ Кардуччи': '1906',
            'Генрик Сенкевич': '1905', 'Фредерик Мистраль': '1904',
            'Хосе Мария Вальдо Эчегарай - И - Эйсагирре': '1904',
            'Бьернстерне Мартиниус Бьернсон': '1903', 'Теодор Моммзен': '1902', 'Рене Сюлли-Прюдом': '1901'}
z = input()
print(laureats[z])

# Азбука Морзе
morsik = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
}
for words in input().split():
    print(' '.join(morsik[c] for c in words.upper()))

# Проверка связи
words = {}
ans = []
for i in input().split():
    if i in list(words.keys()):
        words[i] += 1
    else:
        words[i] = 1
    ans.append(words[i])
print(*ans)

# Карта сокровищ
number = int(input())
count = []
itog = []
for i in range(number):
    number, m = input().split()
    count.append((int(number), int(m)))
while len(count) > 0:
    marsh = []
    a = count[0][0] // 10 * 10
    b = count[0][1] // 10 * 10
    for i in range(0, len(count)):
        x = count[i][0] // 10 * 10
        y = count[i][1] // 10 * 10
        if y == b and x == a:
            marsh.append(count[i])
    itog.append(marsh)
    count = list(filter(lambda c: c not in marsh, count))
kol = [len(itog[i]) for i in range(len(itog))]
kol_max = max(kol)
print(kol_max)

# Дни рождения
mes = {'янв': [], 'фев': [], 'мар': [], 'апр': [], 'май': [], 'июн': [],
       'июл': [], 'авг': [], 'сен': [], 'окт': [], 'ноя': [], 'дек': []}

for i in range(int(input())):
    name_number_mes = input().split()
    n = name_number_mes[0]
    m = name_number_mes[2]
    mes[m].append(n)
    mes[m].sort()
for i in range(int(input())):
    print(*mes.get(input(), ''))

# Домашняя работа
# Транслитерация
translit = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'tc', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ъ': '', 'ь': '', 'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia'
}
text = input()
out_text = ''
for char in text:
    if char.lower() in translit:
        if char.isupper():
            out_text += translit[char.lower()].capitalize()
        else:
            out_text += translit[char]
    else:
        out_text += char
print(out_text)

# Телефонная книга
number1 = int(input())
phone_book = {}
for i in range(number1):
    phone, name = input().split()
    if name not in phone_book:
        phone_book[name] = phone
    else:
        phone_book[name] += ' ' + phone

number2 = int(input())
for i in range(number2):
    query = input().strip()
    if query in phone_book:
        print(phone_book[query])
    else:
        print("Нет в телефонной книге")

# Дни рождения - 2
sp = dict()
number = int(input())
for i in range(number):
    name = input().split()
    if name[2] in sp:
        sp[name[2]].append([name[0], name[1]])
    else:
        sp[name[2]] = [[name[0], name[1]]]
number1 = int(input())
sp2 = [input() for k in range(number1)]
for word in sp2:
    if word in sp:
        sp2 = sorted(sp[word], key=lambda x: (int(x[1]), x[0]))
        d = ''
        for x in sp2:
            d += ' '.join(x) + ' '
        print(d.rstrip())
    if word not in sp:
        print()

# Дополнительные задачи
# Права доступа
main = dict()
for k in range(int(input())):
    vopr = input()
    main[vopr] = main.get(vopr)
for k in range(int(input())):
    new = ''
    dostup = False
    for i in input().split('/'):
        if i:
            new = new + '/' + i
        if new in main:
            dostup = True
    if not dostup:
        print('NO')
    else:
        print('YES')

# Характеристики двоичных чисел
number = input().split()
sp = []
for snum in number:
    number = int(snum)
    binss = bin(number)[2:]
    digits = len(binss)
    units = binss.count('1')
    zeros = binss.count('0')
    sp2 = {'digits': digits, 'units': units, 'zeros': zeros}
    sp.append(sp2)
print(sp)

# Репосты
number = int(input())
post = input().split(' опубликовал пост, количество просмотров: ')
puplar = {post[0]: [int(post[-1]), 'zef1n']}
for i in range(number - 1):
    post = input()
    reposter, post = post.split(' отрепостил пост у ')
    avtor, views = post.split(', количество просмотров: ')
    puplar[reposter] = [int(views), avtor]
    while avtor != 'zef1n':
        puplar[avtor][0] += int(views)
        avtor = puplar[avtor][1]
for kol in puplar.values():
    print(kol[0])

# Частотный анализ – 1
sp = []
number = int(input())
for i in range(number):
    lin = input().split()
    sp.extend(lin)
sp = [word.strip('.,!?:;') for word in sp]
sp = [word.lower() for word in sp]
sp_kol = {}
for word in sp:
    if word in sp_kol:
        sp_kol[word] += 1
    else:
        sp_kol[word] = 1
sorted_words = sorted(sp_kol.items(), key=lambda x: (-x[1], x[0]))
for word, count in sorted_words:
    print(word.capitalize())

# Радиоактивная порода
text = input().split()
i = 0
h = {text[i]: int(text[i + 1]) for i in range(0, len(text), 2)}
sp = [i for i in zip(input().split(), map(float, input().split()))]
number = float(input())
while sum([t[1] * 0.5 ** (i // h[t[0]]) for t in sp]) > number:
    i += 1
print(i)
print(*[t[1] * 0.5 ** (i // h[t[0]]) for t in sp])

# Предсказание погоды с памятью
pogoda_now = input()
a = float(input())
b = float(input())
kol = int(input())
if pogoda_now == 'ясно':
    pasm = 0
    yyasen = 1
else:
    yyasen = 0
    pasm = 1
for i in range(kol):
    yyasen, pasm = (max(yyasen * a, pasm * (1 - b)),
                    max(pasm * b, yyasen * (1 - a)))
if pasm > yyasen:
    print('пасмурно')
    print(pasm)
elif yyasen > pasm:
    print('ясно')
    print(yyasen)
else:
    print('равновероятно')
    print(pasm)
