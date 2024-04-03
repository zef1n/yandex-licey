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

# Домашняя работа
# Статистика
# Таблица
# Прямоугольники
# Дополнительные задачи
# Таблица с изменяемым размером
# СМС-рассылка
