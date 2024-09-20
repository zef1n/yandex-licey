# Kлассная работа
# Калорийность
class FoodInfo(object):

    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def get_proteins(self):
        return self.proteins

    def get_fats(self):
        return self.fats

    def get_carbohydrates(self):
        return self.carbohydrates

    def get_kcalories(self):
        return 4 * self.proteins + 9 * self.fats + 4 * self.carbohydrates

    def __add__(self, value):
        return FoodInfo(self.proteins + value.proteins, self.fats + value.fats,
                        self.carbohydrates + value.carbohydrates)


food1 = FoodInfo(100, 100, 100)
food2 = FoodInfo(50, 60, 70)
food3 = food1 + food2
print(food1.get_proteins(), food1.get_fats(),
      food1.get_carbohydrates(), food1.get_kcalories())
print(food2.get_proteins(), food2.get_fats(),
      food2.get_carbohydrates(), food2.get_kcalories())
print(food3.get_proteins(), food3.get_fats(),
      food3.get_carbohydrates(), food3.get_kcalories())


# Список в обратном порядке
class ReversedList:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, index):
        return self.lst[-1 - index]


# Квадратичная функция
class SquareFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c
# Домашняя работа
# Вычитание дат
# Точки на плоскости
# Разреженный массив
# Дополнительные задачи
# Сложение многочленов
# Очередь и все-все-все
