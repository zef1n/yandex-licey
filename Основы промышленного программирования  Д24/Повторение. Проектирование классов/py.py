# Kлассная работа
# Интервалы и транспонирование
from functools import total_ordering

N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


@total_ordering
class Note:
    def __init__(self, pitch: str, long: bool = False):
        self.pitch = pitch
        self.long = long

    def __eq__(self, other):
        if isinstance(other, Note):
            return self.pitch == other.pitch
        return False

    def __lt__(self, other):
        if isinstance(other, Note):
            return PITCHES.index(self.pitch) < PITCHES.index(other.pitch)
        return False

    def __repr__(self):
        return LONG_PITCHES[PITCHES.index(self.pitch)] if self.long else self.pitch

    def __rshift__(self, steps: int):
        index = PITCHES.index(self.pitch)
        new_index = (index + steps) % N
        return Note(PITCHES[new_index], self.long)

    def __lshift__(self, steps: int):
        index = PITCHES.index(self.pitch)
        new_index = (index - steps) % N
        return Note(PITCHES[new_index], self.long)

    def get_interval(self, other):
        index1 = PITCHES.index(self.pitch)
        index2 = PITCHES.index(other.pitch)
        forward = (index2 - index1) % N
        backward = (index1 - index2) % N
        min_diff = min(forward, backward)
        return INTERVALS[min_diff]


fa1 = Note("фа", True)
fa2 = Note("фа")
la = Note("ля", True)
print(la.get_interval(fa1))
print(fa1.get_interval(fa2))
print(fa1.get_interval(Note('си')))
# Кинотеатры
# Домашняя работа
# С занесением в список
# Равенство и порядок
# Для галочки
# Дополнительные задачи
# С занесением во множества и словари
# Колокольни с ограничениями
# Кинотеатры с отчётами и рекламой
