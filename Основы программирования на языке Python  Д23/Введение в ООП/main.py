# Kлассная работа
# Маленький колокольчик
class LittleBell:
    def sound(self):
        print('ding')


# Кнопка
class Button:
    k = 0

    def click(self):
        self.k += 1

    def click_count(self):
        return self.k

    def reset(self):
        self.k = 0


# Весы
class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, a):
        self.right += a

    def add_left(self, b):
        self.left += b

    def result(self):
        if self.right > self.left:
            return 'R'
        elif self.right < self.left:
            return 'L'
        return '='


# Разбивка по чётности
class OddEvenSeparator:
    def __init__(self):
        self.numbers_odd = []
        self.numbers_even = []

    def add_number(self, number):
        if number % 2 == 0:
            self.numbers_even.append(number)
        else:
            self.numbers_odd.append(number)

    def even(self):
        return self.numbers_even

    def odd(self):
        return self.numbers_odd


# Домашняя работа
# Большой колокольчик
class BigBell:
    def __init__(self):
        self.count = 0

    def sound(self):
        if self.count == 0:
            print('ding')
            self.count += 1
        else:
            print('dong')
            self.count -= 1


# Самые короткие и самые длинные слова
class MinMaxWordFinder:
    def __init__(self):
        self.words = []
        self.short = 0
        self.longest = 0

    def add_sentence(self, word):

        self.words += word.split()
        if self.words:
            self.short = len(min(self.words, key=len))
            self.longest = len(max(self.words, key=len))

    def shortest_words(self):
        if self.short:
            return sorted(list(filter(lambda x: len(x) == self.short, self.words)))
        else:
            return ' '

    def longest_words(self):
        if self.longest:
            return sorted(set(filter(lambda x: len(x) == self.longest, self.words)))
        else:
            return ' '

# Ограничивающий прямоугольник

# Дополнительные задачи
# Морской бой
# Класс крестики-нолики
