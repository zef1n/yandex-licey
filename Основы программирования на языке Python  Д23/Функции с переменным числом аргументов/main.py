# Kлассная работа
# Чеширский указатель
# text = input().split()
# sp = []
# start, end = text[0].lower(), text[-1].lower()
# for i in text[1:-1]:
#     if start <= i.lower() <= end:
#         sp.append(i)
# print(*sp)


# Накопление
def accumulation(*data):
    res = [0]
    for i in data:
        res.append(res[-1] + i)
    return res


# Матрица
def matrix(n=1, m=0, a=0):
    if n == 1 and not m:
        m = 1
    elif n != 1 and not m:
        m = n
    return [[a for _ in range(m)] for _ in range(n)]


# Бариста
ingredient = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0],
              'Маккиато': [2, 1, 0], 'Кофе по-венски': [1, 0, 2],
              'Латте Маккиато': [1, 2, 1], 'Кон Панна': [1, 0, 1]}


def choose_coffee(*args):
    for i in args:
        if ingredient[i][0] <= ingredients[0] and ingredient[i][1] <= ingredients[1] and ingredient[i][2] <= \
                ingredients[2]:
            ingredients[0] -= ingredient[i][0]
            ingredients[1] -= ingredient[i][1]
            ingredients[2] -= ingredient[i][2]
            return i
    return 'К сожалению, не можем предложить Вам напиток'


ingredients = [1, 2, 3]



# Спамогенератор
def spam(email, name, date, place='Магнитогорске'):
    print(f'To: {email}\n'
          f'Здраствуйте, {name}!\n'
          f'Были бы рады видеть вас на встрече начинающих программистов в {place},\n'
          f'которая пройдет {date}.')


# Домашняя работа
# Частичные суммы
def partial_sums(*args):
    sp = [0]
    for i in range(len(args)):
        sp.append(sp[i] + args[i])
    return sp


# Занято
def sequence_occupied(**kwargs):
    max_length = 0
    max_row = 0

    for row, seats in kwargs.items():
        current_length = 0
        max_current_length = 0
        for seat in seats:
            if seat == 1:
                current_length += 1
                if current_length > max_current_length:
                    max_current_length = current_length
            else:
                current_length = 0
        if max_current_length > max_length:
            max_length = max_current_length
            max_row = int(row)

    return max_length, max_row




places = [[1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 1, 0, 0, 0]]
data = {'2': [3, 2], '1': [4], '3': [4]}
print(sequence_occupied(**data))
print(places)
# Цезарь

# Дополнительные задачи
# Дартс

# Заменитель

# Уравнения степени не выше второй — часть 2

# Уравнения степени не выше второй — часть 3

# Наиболее вероятное будущее
