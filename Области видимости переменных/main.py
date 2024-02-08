# Классная работа
# Длина окружности и площадь круга
def circle_length(radius):
    return 2 * 3.14159 * radius


def circle_area(radius):
    return 3.14159 * radius ** 2


def main():
    radius = float(input())
    print(circle_length(radius), circle_area(radius))


# Корни квадратного уравнения
def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def larger_root(p, q):
    disc = discriminant(1, p, q)
    one = (-p + disc ** 0.5) / 2
    two = (-p - disc ** 0.5) / 2
    return max(one, two)


def smaller_root(p, q):
    disc = discriminant(1, p, q)
    one = (-p + disc ** 0.5) / 2
    two = (-p - disc ** 0.5) / 2
    return min(one, two)


def main():
    p = float(input())
    q = float(input())

    dicscrim = discriminant(1, p, q)
    print(dicscrim)

    smaller = smaller_root(p, q)
    larger = larger_root(p, q)
    print(*(smaller, larger))


# Заикание
last_m = ""


def print_without_duplicates(message):
    global last_m
    if message != last_m:
        print(message)
    last_m = message


# Длинный чек
items: [str, int] = []
con: int = 1


def add_item(name: str, cost: int):
    items.append((name, cost))


def print_receipt():
    total: int = 0
    global con
    if not items:
        return
    print(f"Чек {con}. Всего предметов: {len(items)}")
    for name, cost in items:
        total += cost
        print(f"{name} - {cost}")
    print(f"Итого: {total}")
    print('-----')
    con += 1
    items.clear()


# Я вас знаю
# def polite_input(question):
#     if not hasattr(polite_input, "name"):
#         polite_input.name = input("Как вас зовут?")
#     return input(f"{polite_input.name}, {question}")
#
#
# def solution():
#     print("Я - самая вежливая программа на свете")
#     polite_input("укажите возраст")
#     polite_input("укажите номер школы")
#     polite_input("укажите полный номер класса")
#     polite_input("укажите что-нибудь ещё")
#     print("Самая вежливая программа завершила свою работу")
#
#
# solution()

# Вечеринка
friends_D = {}


def add_friends(name_of_person, list_of_friends):
    global friends_D
    if name_of_person in friends_D:
        friends_D[name_of_person].extend(list_of_friends)
    else:
        friends_D[name_of_person] = list_of_friends


def are_friends(name_of_person1, name_of_person2):
    global friends_D
    return name_of_person2 in friends_D.get(name_of_person1, [])


def print_friends(name_of_person):
    global friends_D
    friends = friends_D.get(name_of_person, [])
    friends.sort()
    print(" ".join(friends))


# Азбука Морзе
MorseCode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
             'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
             'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
             'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
             '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', 'А': '.-', 'Б': '-...', 'В': '.--',
             'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-',
             'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
             'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--',
             'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-',
             '.': '.-.-.-', ',': ' --..--', '?': '.. - -..', "'": '.----.', '!': ' -.-.--',
             '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
             '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
             '@': '.--.-.', '¿': '..-.-', '¡': '--...-',
             }


def encode_to_morse(text):
    morzcode = ''
    for sim in text.upper():
        if sim == ' ':
            morzcode += ' '
        elif sim in MorseCode:
            morzcode += MorseCode[sim] + ' '
        else:
            morzcode += sim
    return morzcode.strip()


def decode_from_morse(code):
    morz = {value: key for key, value in MorseCode.items()}
    morz_list = code.split(' ')
    decoder = ''
    for morz_sim in morz_list:
        if morz_sim == '':
            decoder += ' '
        elif morz_sim in morz:
            decoder += morz[morz_sim]
        else:
            decoder += morz_sim
    return decoder


def main():
    while True:
        ch = input("Хотите закодировать (1) или раскодировать (2) текст? Введите 1 или 2: ")
        if ch == '1':
            txt_encode = input("Введите текст для кодирования: ")
            encoder = encode_to_morse(txt_encode)
            print(f"Код Морзе: {encoder}")
        elif ch == '2':
            morz_decoder = input("Введите код Морзе для декодирования: ")
            decoder_txt = decode_from_morse(morz_decoder)
            print(f"Раскодированный текст: {decoder_txt}")
        else:
            print("Пожалуйста, выберите 1 или 2.")


# Домашняя работа
# НРЗБРЧВ
# def translate(text):
#     global translated_text
#     translated_words = []
#
#     for word in text.split():
#         translated_word = ''.join([char for char in word if char.lower() not in 'аеёиоуыэюя'])
#         translated_words.append(translated_word)
#
#     translated_text = ' '.join(translated_words)
#
#

# translated_text = None
# translate(
#     "Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать.")
#

# print(translated_text)

# Здоровое питание

food = {
    'жирное': ["растительное масло", 'гамбургер'],
    'сладкое': ['печенье', 'чай', 'мёд', 'сахар', 'торт', 'пончики', ],
    'мучное': ["печенье"],
    'диетическое': ['творог', 'фрукты', 'каша', 'зелень', 'овощи', 'рис', 'фрукты'],
}


def diet(eat):
    foods_catg = {'жирное': 0, 'сладкое': 0, 'мучное': 0, 'диетическое': 0}

    for k in eat.split(', '):
        for ct, ks in food.items():
            if k in ks:
                foods_catg[ct] += 1

    dfc = foods_catg['диетическое']
    ndfc = len(eat.split(', ')) - dfc

    if ndfc > dfc:
        return 'Не ешь столько, По!'
    else:
        return 'Так держать, Воин Дракона!'


# Бюрократия
tek_sotrudnik = None
rabochie = []


def setup_profile(name, vacation_dates):
    global tek_sotrudnik
    tek_sotrudnik = {"name": name, "vacation_dates": vacation_dates, "deputy": None}
    rabochie.append(tek_sotrudnik)


def print_application_for_leave():
    print(f"Заявление на отпуск в период {tek_sotrudnik['vacation_dates']}. {tek_sotrudnik['name']}")


def print_holiday_money_claim(amount):
    print(f"Прошу выплатить {amount} отпускных денег. {tek_sotrudnik['name']}")


def print_attorney_letter(to_whom):
    print(
        f"На время отпуска в период {tek_sotrudnik['vacation_dates']} моим заместителем назначается {to_whom}. "
        f"{tek_sotrudnik['name']}")


# Пример использования:
setup_profile("Иван Петров", "1 июня – 20 июня")
print_application_for_leave()
print_application_for_leave()
print_holiday_money_claim("15 тысяч пиастров")
print_attorney_letter("Василий Васильев")

# Дополнительные задачи
# Несвежие анекдоты

# Айболит

# Счастливый пассажир

# Делайте ваши ставки

# Статистика по клиентам

# Римские примеры

# Айболит 2.0
