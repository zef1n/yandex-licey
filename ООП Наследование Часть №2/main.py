# Kлассная работа

# Сумматоры
class Summator:
    def sum(self, n):
        c = 0
        for i in range(n + 1):
            c += self.transform(int(i))
        return c

    def transform(self, n):
        return n


class SquareSummator(Summator):
    def __init__(self):
        pass

    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def __init__(self):
        pass

    def transform(self, n):
        return n ** 3


# Сайт поиска вакансий
# Треугольники
class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(Triangle, a, b, c):
        super().__init__(a, b, c)
        Triangle.a = a
        Triangle.b = a
        Triangle.c = a

    def perimeter(self):
        return Triangle.perimeter(self)
# Домашняя работа
# Сумматоры – 2
# Алфавит классов
# Дополнительные задачи
# Заготовка для игры
# mapPainter
# Правильные многоугольники
