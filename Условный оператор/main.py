# Kлассная работа
# Вспомнить всё
letter = input()
if letter == 'print':
    print(letter, '? Конечно, помню, ведь мы проходили это на прошлом занятии!')

# Только Питон!
letter = input()
if letter == 'Python':
    print('ДА')
else:
    print('НЕТ')

# Ёлочка, гори!
one = input()
two = input()
three = input()
if one == 'раз' and two == 'два' and three == 'три':
    print('ГОРИ')
else:
    print('НЕ ГОРИ')

# Ёлочка-2
one = input()
two = input()
three = input()
if one == 'раз' and two == 'два' and three == 'три':
    print('ГОРИ')
elif one == '1' and two == '2' and three == '3':
    print('ГОРИ')
else:
    print('НЕ ГОРИ')

# Ёлочка-3
one = input()
two = input()
three = input()
if (one == 'раз' or one == 'один') and (two == 'два') and (three == 'три'):
    print('ГОРИ')
elif one == '1' and two == '2' and three == '3':
    print('ГОРИ')
else:
    print('НЕ ГОРИ')

# Личностный тест
one_question = input('Любите ли вы котиков?: ')
if one_question == 'да':
    print('Отлично! Котики самые добрые животные!')
elif one_question == 'нет':
    print('Плохо! Ведь котики самые добрые животные!')
else:
    print("Ответ может состоять только из 'да' или 'нет'")
two_question = input('Умеете ли вы программировать?: ')
if two_question == 'да':
    print('Круто! Ждем в нашей команде "Яндекс Лицей"!')
elif two_question == 'нет':
    print('Ничего страшного! Приходи к нам в "Яндекс Лицей" и всё узнаешь!')
else:
    print("Ответ может состоять только из 'да' или 'нет'")

# Эхо-2
lettet = input()
print(lettet*4)

# Мяу
text = input()
if 'кот' in text:
    print('МЯУ')
else:
    print('ГАВ')

# Домашнаяя работа
# Вежливый тренажёр
name = input('Назовите себя, пожалуйста!\n')
text = input('Введите текст.\n')
text_repeat = input('Повторите текст.\n')
if text == text_repeat:
    print(f'{name}, введено верно!')
else:
    print(f'{name}, пока не получилось, попробуйте снова!')

# Регистрация почты
login = input()
email = input()
if '@' in login:
    print('Некорректный логин')
elif '@' not in email:
    print('Некорректный адрес')
else:
    print('OK')

# Лабиринт
print('Лабиринт')
print('Введите одно из слов в кавычках для выбора.')
question = input('Выберите куда вы хотите пойти "налево", "направо", "прямо"\n')


if question == 'налево':
    print('Вы пошли налево. Через время вы дошли до двух дверей. Вы выберете "левую" или "правую"?')
    choice = input('Введите одно из слов в кавычках для выбора: ')
    if choice == 'левую':
        print('Вы открыли левую дверь. Вы успешно сбежали из лабиринта :)')
    elif choice == 'правую':
        print('Вы открыли правую дверь. Но за ней вас ждал вампир и убил вас! :(')
    else:
        print('Ответ должен быть только из слов, которые указаны в кавычках')

elif question == 'направо':
    print('Вы пошли направо. Через время вы дошли до двух дверей. Вы выберете "левую" или "правую"?')
    choice = input('Введите одно из слов в кавычках для выбора: ')
    if choice == 'левую':
        print('Вы смело открыли левую дверь. Но за ней вас ждал годзида, который разорвал вас пополам! :(')
    elif choice == 'правую':
        print('Вы смело открыли правую дверь. Но за ней вас ждал зомби, который прокусил вам шею! :(')
    else:
        print('Ответ должен быть только из слов, которые указаны в кавычках')

elif question == 'прямо':
    print('Вы пошли прямо. Через время вы дошли до двух дверей. Вы выберете "левую" или "правую"?')
    choice = input('Введите одно из слов в кавычках для выбора: ')
    if choice == 'левую':
        print('Вы открыли левую дверь. Но за ней вас ждал бандит! Он вас поймал! :)')
    elif choice == 'правую':
        print('Вы смело открыли правую дверь. Но за ней вас ждала страшная жаба, которая проглотила вас целиком! :( ')
    else:
        print('Ответ должен быть только из слов, которые указаны в кавычках')
else:
    print('Ответ должен быть только из слов, которые указаны в кавычках')

# Дополнительные задачи
# Эхо-0
print(input())

# Дзен
yes = input()
no = input()
if 'да' or 'нет' in yes:
    print('ВЕРНО')
elif 'да' and 'нет' in no:
    print('ВЕРНО')
else:
    print('НЕВЕРНО')

# Да или нет?!
a = input()
b = input()
if (a == 'да' or a == 'нет') and (b == 'да' or b == 'нет'):
    print('ВЕРНО')
else:
    print('НЕВЕРНО')

# Личностный тест 2
seasons = 'Зима', 'Весна', 'Лето', 'Осень'
one_question = input(f'Какие ваши любимые времена года? Выберите из предложенных вариантов: {seasons}\n')
if one_question == 'Зима':
    print('Вы любитель снежков, веселья и мороза!')
elif one_question == 'Весна':
    print('Вы любитель цветущих растений!')
elif one_question == 'Лето':
    print('Вы любитель гулять, отдыхать и купаться')
elif one_question == 'Осень':
    print('Вы любитель пасмурной погоды и грязи? С вами точно всё хорошо?')
else:
    print('Укажите вариант ответа, который указан в кавычках!')
animals = 'Кот', 'Собака', 'Попугай', 'Черепаха'
two_question = input(f'Каких животных из списка вы любите? Выберите из предложенных вариантов: {animals}\n')
if two_question == 'Кот':
    print('Отлично! Коты могут вылечить вас в любой момент!')
elif two_question == 'Собака':
    print('Отлично! Собаки могут выручить вас в любой момент!')
elif two_question == 'Попугай':
    print('Отлично! Попугаи могут расмешить вас в любой момент!')
elif two_question == 'Черепаха':
    print('Отлично! За черепахами интересно наблюдать!')
else:
    print('Укажите вариант ответа, который указан в кавычках!')

# Короткая светская беседа
one_question = input('Какое у вас настроение?\n')
if (not 'не' in one_question and 'хорош' in one_question) or ('прекрасн' in one_question):
    print('Прекрасно! У меня тоже хорошее! :)')
elif ('плох' in one_question) or ('ужасн' in one_question) or ('не хорош' in one_question):
    print('Ничего страшного! Скоро все наладиться! :)')
else:
    print('Извините, я вас не понял. :(')
