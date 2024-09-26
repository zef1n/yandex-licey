# Kлассная работа
# Интервалы и транспонирование
from functools import total_ordering
from typing import Any

PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
N = 7


@total_ordering
class Note:
    def __init__(self, name: str, long: bool = False) -> None:
        if long and name in LONG_PITCHES:
            self.index = LONG_PITCHES.index(name)
            self.long = True
            self.name = PITCHES[self.index]
        elif name in PITCHES:
            self.index = PITCHES.index(name)
            self.long = long
            self.name = name
        else:
            raise ValueError(f"Нота '{name}' не найдена в списках.")

    def __lshift__(self, shift: int) -> 'Note':
        new_index = (self.index - shift) % N
        if self.long:
            return Note(LONG_PITCHES[new_index], True)
        return Note(PITCHES[new_index])

    def __rshift__(self, shift: int) -> 'Note':
        new_index = (self.index + shift) % N
        if self.long:
            return Note(LONG_PITCHES[new_index], True)
        return Note(PITCHES[new_index])

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Note):
            return False
        return self.index == other.index

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Note):
            return False
        return self.index < other.index

    def __str__(self) -> str:
        return LONG_PITCHES[self.index] if self.long else PITCHES[self.index]

    def get_interval(self, other: 'Note') -> str:
        interval = (other.index - self.index) % N
        return INTERVALS[interval]


# Подбор мелодии
from functools import total_ordering
from typing import Any

PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
N = 7


@total_ordering
class Note:
    def __init__(self, name: str, long: bool = False) -> None:
        if long and name in LONG_PITCHES:
            self.index = LONG_PITCHES.index(name)
            self.long = True
            self.name = PITCHES[self.index]
        elif name in PITCHES:
            self.index = PITCHES.index(name)
            self.long = long
            self.name = name
        else:
            raise ValueError(f"Нота '{name}' не найдена в списках.")

    def __lshift__(self, shift: int) -> 'Note':
        new_index = (self.index - shift) % N
        if self.long:
            return Note(LONG_PITCHES[new_index], True)
        return Note(PITCHES[new_index])

    def __rshift__(self, shift: int) -> 'Note':
        new_index = (self.index + shift) % N
        if self.long:
            return Note(LONG_PITCHES[new_index], True)
        return Note(PITCHES[new_index])

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Note):
            return False
        return self.index == other.index

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Note):
            return False
        return self.index < other.index

    def __str__(self) -> str:
        return LONG_PITCHES[self.index] if self.long else PITCHES[self.index]

    def get_interval(self, other: 'Note') -> str:
        interval = (other.index - self.index) % N
        return INTERVALS[interval]


class Melody:
    def __init__(self, notes: list[Note] = None) -> None:
        self.notes = notes if notes else []

    def __str__(self) -> str:
        if not self.notes:
            return ""
        result = ", ".join([str(note) for note in self.notes])
        return result[0].upper() + result[1:]

    def append(self, note: Note) -> None:
        self.notes.append(note)

    def replace_last(self, note: Note) -> None:
        if self.notes:
            self.notes[-1] = note

    def remove_last(self) -> None:
        if self.notes:
            self.notes.pop()

    def clear(self) -> None:
        self.notes = []

    def __len__(self) -> int:
        return len(self.notes)

    def __rshift__(self, shift: int) -> 'Melody':
        new_melody = []
        for note in self.notes:
            new_note_index = note.index + shift
            if new_note_index >= N:
                return Melody(self.notes)
            new_melody.append(note >> shift)
        return Melody(new_melody)

    def __lshift__(self, shift: int) -> 'Melody':
        new_melody = []
        for note in self.notes:
            new_note_index = note.index - shift
            if new_note_index < 0:
                return Melody(self.notes)
            new_melody.append(note << shift)
        return Melody(new_melody)


fa1 = Note("фа", True)
fa2 = Note("фа")
print(fa1 == fa2)
print(fa1 > fa2)
print(fa1 < fa2)
print(fa1 <= fa2)

la = Note("ля", True)
print(fa1 < la)
# Кинотеатры
# Домашняя работа
# С занесением в список
# Равенство и порядок
# Для галочки
# Дополнительные задачи
# С занесением во множества и словари
# Колокольни с ограничениями
# Кинотеатры с отчётами и рекламой
