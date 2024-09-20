# import sys
#
#
# def find_shortest_words(line):
#     words = line.split()
#     min_length = len(min(words, key=len))
#     sh_w = [word for word in words if len(word) == min_length]
#     return sh_w
#
#
# lines = sys.stdin.readlines()
#
# result = set()
# for line in lines:
#     sh_w_print = find_shortest_words(line)
#     result.update(sh_w_print)
# print("! ".join(result))

#######################################################################################################################
# def future(*args, plan="Earth"):
#     result = {}
#     for arg in args:
#         diff_count = len(set(arg.lower()) - set(plan.lower()))
#         if diff_count in result:
#             result[diff_count].append(arg)
#         else:
#             result[diff_count] = [arg]
#     for key in result:
#         result[key].sort(reverse=True)
#     return result
#
#
# # Пример использования
# lines = [
#     'can', 'Breathe', 'experience',
#     'gravity', 'inconveniences', 'jellyfish',
#     'plankton', 'vegetation'
# ]
# print(future(*lines))

#######################################################################################################################
from PIL import Image
def humans(image_path, *coordinates, part=4):
    # Открываем изображение
    img = Image.open(image_path)

    # Отражаем изображение по вертикали
    img = img.transpose(Image.FLIP_LEFT_RIGHT)

    # Инициализируем пустой список для хранения вырезанных квадратов
    cropped_squares = []

    # Обходим переданные координаты
    for coord in coordinates:
        x, y = coord
        # Вырезаем квадрат 400x400, центрированный по заданным координатам
        square = img.crop((x - 200, y - 200, x + 200, y + 200))
        cropped_squares.append(square)

    # Создаем новое изображение, объединяя вырезанные квадраты
    result_width = 400 * len(coordinates)
    result_height = 400
    result_img = Image.new('RGB', (result_width, result_height))

    for i, square in enumerate(cropped_squares):
        result_img.paste(square, (i * 400, 0))

    # Модифицируем интенсивности пикселей
    pixels = result_img.load()
    for x in range(result_width):
        for y in range(result_height):
            r, g, b = pixels[x, y]
            r = (r + part) % 256
            g = (g + part) % 256
            b = (b + part) % 256
            pixels[x, y] = (r, g, b)

    return result_img


humans(
    'aliens.png',
    (0, 224), (600, 224),
    (0, 624), (600, 624),
    part=4
).save('result.png')


#######################################################################################################################
class World:
    def __init__(self, *args, planet="New"):
        self.strings = list(args)
        self.planet = planet

    def __add__(self, other):
        new_strings = set(self.strings) ^ set(other.strings)
        new_strings = sorted(new_strings)
        new_planet = self.planet[0] + other.planet[1:]
        return World(*new_strings, planet=new_planet)

    def __mul__(self, other):
        additional_strings = [s for s in other.strings if s not in self.strings]
        self.strings.extend(additional_strings)
        return self

    def __call__(self):
        return sum(len(s) for s in self.strings)

    def __str__(self):
        return f"World(planet: {self.planet}, suggest: {', '.join(self.strings)})"

# # Пример использования
# wl1 = World("string1", "string2", planet="Earth")
# wl2 = World("string2", "string3", planet="Mars")
#
# things1 = ['car', 'computer', 'ballet', 'armagnac', 'sandwich']
# things2 = ['car', 'fountain', 'vacuum cleaner', 'Kant', 'ballet']
# wl1 = World(*things1)
# wl2 = World(*things2, planet='Febula')
# wl = wl1 + wl2
# print(wl1, wl2, wl, sep='\n')
#######################################################################################################################
