# Kлассная работа
# Minecraft
class BaseObject:

    def __init__(self, x: int, y: int, z: int):
        self.x, self.y, self.z = x, y, z

    def get_coordinates(self) -> (int, int, int):
        return self.x, self.y, self.z


class Block(BaseObject):

    def shatter(self):
        self.x, self.y, self.z = None, None, None


class Entity(BaseObject):
    def move(self, x: int, y: int, z: int):
        self.x, self.y, self.z = x, y, z


class Thing(BaseObject):
    pass


# Таксономия живой природы
class MAY:
    pass


class Acellularia(MAY):
    pass


class Cellularia(MAY):
    pass


class Prokaryota(Cellularia):
    pass


class Eukaryota(Cellularia):
    pass


class Plantae(Eukaryota):
    pass


class Fungi(Eukaryota):
    pass


class Unicellularia(Eukaryota):
    pass


class Animalia(Eukaryota):
    pass


# Пользователи Яндекс.Лицея
class User:
    def solve(self, n):
        pass


class Student(User):
    pass


class Teacher(User):
    def check_solution(self, user, n):
        pass


class Admin(User):
    def edit(self, n):
        pass


class SuperAdmin(Admin):
    def grant(self, user):
        pass

# Домашняя работа
# Социальная сеть
# Классификация животных
# Дополнительные задачи
# Иерархия транспортных средств
# Геометрические фигуры – 2
