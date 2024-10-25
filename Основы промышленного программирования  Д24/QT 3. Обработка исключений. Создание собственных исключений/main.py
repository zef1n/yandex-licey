# Kлассная работа
# Номера телефонов 1
formatted_number = ''.join(input().split())

if '--' in formatted_number:
    print("error")
    exit()

if formatted_number.count('(') != formatted_number.count(')'):
    print("error")
    exit()

if not formatted_number.startswith('8'):
    if not formatted_number.startswith('+7'):
        print("error")
        exit()

if formatted_number[0] == '-' or formatted_number[-1] == '-':
    print("error")
    exit()

if '((' in formatted_number or '))' in formatted_number:
    print("error")
    exit()

for symbol in formatted_number:
    if symbol.isalpha():
        print("error")
        exit()

if '(' in formatted_number and ')' in formatted_number:
    if formatted_number.index('(') > formatted_number.index(')'):
        print("error")
        exit()

formatted_number = formatted_number.replace('(', '').replace(')', '').replace('-', '')

if formatted_number[0] == '8':
    if len(formatted_number) == 11:
        print('+7' + formatted_number[1:])
    else:
        print("error")
else:
    if len(formatted_number) == 12:
        print(formatted_number)
    else:
        print("error")

# Номера телефонов. Часть 2
try:
    number = ''.join(input().split())

    if '--' in number:
        raise ValueError("Недопустимый двойной дефис")

    if number.count('(') != number.count(')'):
        raise SyntaxError("Несоответствие количества открывающих и закрывающих скобок")

    if not (number.startswith('8') or number.startswith('+7')):
        raise ValueError("Номер должен начинаться с '8' или '+7'")

    if number[0] == '-' or number[-1] == '-':
        raise SyntaxError("Недопустимые дефисы в начале или конце номера")

    if '((' in number or '))' in number:
        raise SyntaxError("Недопустимая последовательность скобок")

    if any(char.isalpha() for char in number):
        raise ValueError("Номер не должен содержать буквы")

    if '(' in number and ')' in number and number.index('(') > number.index(')'):
        raise SyntaxError("Неверный порядок скобок")

    number = number.replace('(', '').replace(')', '').replace('-', '')

    if number.startswith('8'):
        if len(number) == 11:
            print('+7' + number[1:])
        else:
            raise ValueError("Некорректная длина номера")
    elif len(number) == 12:
        print(number)
    else:
        raise ValueError("Некорректная длина номера")

except (ValueError, SyntaxError) as e:
    print("error")

# Номера телефонов. Возвращение
try:
    phone = ''.join(input().split())
    if '--' in phone:
        raise ValueError("неверный формат")
    if phone.count('(') != phone.count(')'):
        raise ValueError("неверный формат")
    if not phone.startswith('8') and not phone.startswith('+7'):
        raise ValueError("неверный формат")
    if phone[0] == '-' or phone[-1] == '-':
        raise ValueError("неверный формат")
    if '((' in phone or '))' in phone:
        raise ValueError("неверный формат")
    if any(c.isalpha() for c in phone):
        raise ValueError("неверный формат")
    if '(' in phone and ')' in phone and phone.index('(') > phone.index(')'):
        raise ValueError("неверный формат")

    phone = phone.replace('(', '').replace(')', '').replace('-', '')

    if phone.startswith('8'):
        if len(phone) == 11:
            print('+7' + phone[1:])
        else:
            raise IndexError("неверное количество цифр")
    elif len(phone) == 12:
        print(phone)
    else:
        raise IndexError("неверное количество цифр")

except ValueError as e:
    print(e)
except IndexError as e:
    print(e)

# Пароли. Часть 1
eng = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю',
       'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
letters = set(''.join(eng))
letters_up = set(''.join(eng).upper())
numberu = set('1234567890')


def check_password(password):
    cor = set(password)
    if not (cor & letters and cor & letters_up and cor & numberu and len(password) > 8):
        return 'error'
    for c in range(len(password) - 2):
        password_ = password[c:c + 3].lower()
        for i in eng:
            if password_ in i:
                return 'error'
    return 'ok'


print(check_password(input()))


# Пароли. Часть 2
class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


lettersi = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю',
            'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
numberu = set('1234567890')


def has_sequence(password, keyboards):
    password_lower = password.lower()
    for line in keyboards:
        for i in range(len(line) - 2):
            seq = line[i:i + 3]
            if seq in password_lower:
                return True
    return False


def check_password(password):
    if len(password) < 9:
        raise LengthError()

    if not any(char.isdigit() for char in password):
        raise DigitError()

    if password.islower() or password.isupper() or all(char.isdigit() for char in password):
        raise LetterError()
    if has_sequence(password, lettersi):
        raise SequenceError()

    return "ok"


# Домашняя работа
# Телефоны наносят ответный удар
try:
    phone_number = ''.join(input().split())
    if '--' in phone_number:
        raise ValueError
    if phone_number.count('(') != phone_number.count(')'):
        raise ValueError
    if not phone_number[0] == '8' and not phone_number[:2] == '+7':
        raise ValueError
    if phone_number.endswith('-') or phone_number.startswith('-'):
        raise ValueError
    if '))' in phone_number or '((' in phone_number:
        raise ValueError
    for i in phone_number:
        if i.isalpha():
            raise ValueError
    if '(' in phone_number and ')' in phone_number:
        if phone_number.index('(') > phone_number.index(')'):
            raise ValueError

    phone_number = ''.join(phone_number.split('('))
    phone_number = ''.join(phone_number.split(')'))
    phone_number = ''.join(phone_number.split('-'))
    if phone_number[0] == '8':
        if len(phone_number) == 11:
            phone_number = '+7' + phone_number[1:]
        else:
            raise IndexError
    elif len(phone_number) != 12:
        raise IndexError
    operator_code = phone_number[2:5]
    mts_codes = list(range(910, 920)) + list(range(980, 990))
    megafon_codes = list(range(920, 940))
    beeline_codes = list(range(902, 907)) + list(range(960, 970))

    if not (int(operator_code) in mts_codes or int(operator_code) in megafon_codes or int(
            operator_code) in beeline_codes):
        print("не определяется оператор сотовой связи")
    else:
        print(phone_number)
except ValueError:
    print("неверный формат")
except IndexError:
    print("неверное количество цифр")
