# Kлассная работа
# Выборки
class Selector:
    def __init__(self, values):
        self.values = values
        self.list_evens = list()
        self.list_odds = list()
        for i in values:
            if i % 2 == 0:
                self.list_evens.append(i)
            else:
                self.list_odds.append(i)

    def get_evens(self):
        return self.list_evens

    def get_odds(self):
        return self.list_odds


# Вывод предложений
class LeftParagraph:
    def __init__(self, number):
        self.number = number
        self.list_words = list()

    def add_word(self, word):
        self.list_words.append(word)

    def end(self):
        t = ''
        for word in self.list_words:
            if not t:
                t += word
            elif len(t) + len(word) + 1 <= self.number:
                t += ' ' + word
            else:
                print(t)
                t = word
        print(t)
        self.list_words.clear()


class RightParagraph:
    def __init__(self, number):
        self.number = number
        self.list_words = list()

    def add_word(self, word):
        self.list_words.append(word)

    def end(self):
        t = ''
        for word in self.list_words:
            if not t:
                t += word
            elif len(t) + len(word) + 1 <= self.number:
                t += ' ' + word
            else:
                t = ' ' * (self.number - len(t)) + t
                print(t)
                t = word
        t = ' ' * (self.number - len(t)) + t
        print(t)
        self.list_words.clear()


# Форматы дат
class AmericanDate:

    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def get_year(self):
        self.y = str(self.y)
        return self.y

    def get_month(self):
        self.m = str(self.m)
        return self.m

    def get_day(self):
        self.d = str(self.d)
        return self.d

    def set_year(self, ny):
        self.y = ny
        return self.y

    def set_month(self, nm):
        self.m = str(nm)
        return str(self.m)

    def set_day(self, nd):
        self.d = str(nd)
        return self.d

    def format(self):
        if len(self.get_day()) > 1 and len(self.get_month()) > 1:
            return f'{self.get_month()}.{self.get_day()}.{self.get_year()}'
        if len(self.get_day()) == 1 and len(self.get_month()) == 1:
            return f'0{self.get_month()}.0{self.get_day()}.{self.get_year()}'
        if len(self.get_day()) > 1 and len(self.get_month()) == 1:
            return f'0{self.get_month()}.{self.get_day()}.{self.get_year()}'
        if len(self.get_day()) == 1 and len(self.get_month()) > 1:
            return f'{self.get_month()}.0{self.get_day()}.{self.get_year()}'


class EuropeanDate:

    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def get_year(self):
        self.y = str(self.y)
        return self.y

    def get_month(self):
        self.m = str(self.m)
        return self.m

    def get_day(self):
        self.d = str(self.d)
        return self.d

    def set_year(self, ny):
        self.y = ny
        return self.y

    def set_month(self, nm):
        self.m = str(nm)
        return str(self.m)

    def set_day(self, nd):
        self.d = str(nd)
        return self.d

    def format(self):
        if len(self.get_day()) > 1 and len(self.get_month()) > 1:
            return f'{self.get_day()}.{self.get_month()}.{self.get_year()}'
        if len(self.get_day()) == 1 and len(self.get_month()) == 1:
            return f'0{self.get_day()}.0{self.get_month()}.{self.get_year()}'
        if len(self.get_day()) > 1 and len(self.get_month()) == 1:
            return f'{self.get_day()}.0{self.get_month()}.{self.get_year()}'
        if len(self.get_day()) == 1 and len(self.get_month()) > 1:
            return f'0{self.get_day()}.{self.get_month()}.{self.get_year()}'




american = AmericanDate(2000, 4, 10)
european = EuropeanDate(2000, 4, 10)
print(american.format())
print(european.format())
# Домашняя работа
# Статистика
# Таблица
# Прямоугольники
# Дополнительные задачи
# Таблица с изменяемым размером
# СМС-рассылка
