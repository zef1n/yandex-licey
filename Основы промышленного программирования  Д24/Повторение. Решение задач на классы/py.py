# Kлассная работа
# Ноты
class Note:
    def __init__(self, height):
        self.height = height

    def play(self):
        print(self.height)


# Но-оты
class Note:
    def __init__(self, height, duration=False):
        self.height = height
        self.duration = duration

    def __str__(self):
        if self.duration:
            if self.height == "соль":
                return "со-оль"
            yandex = {
                "до": "-о",
                "ре": "-э",
                "ми": "-и",
                "фа": "-а",
                "ля": "-а",
                "си": "-и"
            }
            return self.height + yandex.get(self.height, "")
        else:
            return self.height


# Больше нот, хороших и разных
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    def __init__(self, height, is_long=False):
        self.height = height
        self.is_long = is_long

    def __str__(self):
        if self.is_long:
            if self.height == "соль":
                return "со-оль"
            suffixes = {
                "до": "-о",
                "ре": "-э",
                "ми": "-и",
                "фа": "-а",
                "ля": "-а",
                "си": "-и"
            }
            return self.height + suffixes.get(self.height, "")
        else:
            return self.height


class LoudNote(Note):
    def __str__(self):
        return super().__str__().upper()


class DefaultNote(Note):
    def __init__(self, height="до", is_long=False):
        super().__init__(height, is_long)


class NoteWithOctave(Note):
    def __init__(self, height, octave, is_long=False):
        super().__init__(height, is_long)
        self.octave = octave

    def __str__(self):
        return f"{super().__str__()} ({self.octave})"


# Продолжайте создавать удивительные вещи!

# Домашняя работа
# Точка обыкновенная
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y


# Именованная точка
class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"

    def __invert__(self):
        return Point(self.name, self.y, self.x)


# Осторожно окрашенные
class Point:
    __easter_egg = 'Сегодня ты делаешь код...'

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"

    def __invert__(self):
        return Point(self.name, self.y, self.x)


class ColoredPoint(Point):
    def __init__(self, name, x, y, color=(0, 0, 0)):
        super().__init__(name, x, y)
        self.color = color

    def get_color(self):
        return self.color

    def __invert__(self):
        inverted_color = tuple(255 - c for c in self.color)
        return ColoredPoint(self.name, self.y, self.x, inverted_color)

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"


# Дополнительные задачи
# Колокольня
class LittleBell:
    # Если твой код работает, значит это хороший код
    def sound(self):
        print("ding")


class BigBell:
    def __init__(self):
        self.ding_next = True

    def sound(self):
        if self.ding_next:
            print("ding")
            self.ding_next = False
        else:
            print("dong")
            self.ding_next = True


class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print("...")


# О колоколах подробнее
class Bell:
    def __init__(self, *pos_args, **named_args):
        self.positional_args = pos_args
        self.named_args = named_args

    def print_info(self):
        info_parts = []
        if self.named_args:
            sorted_named = sorted(self.named_args.items())
            named_info = ', '.join(f"{key}: {value}" for key, value in sorted_named)
            info_parts.append(named_info)
        if self.positional_args:
            positional_info = ', '.join(self.positional_args)
            info_parts.append(positional_info)
        if info_parts:
            print('; '.join(info_parts))
        else:
            print("-")


class LittleBell(Bell):
    def sound(self):
        print("ding")


class BigBell(Bell):
    def __init__(self, *pos_args, **named_args):
        super().__init__(*pos_args, **named_args)
        self.ding_next = True

    def sound(self):
        if self.ding_next:
            print("ding")
            self.ding_next = False
        else:
            print("dong")
            self.ding_next = True


class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print("...")
