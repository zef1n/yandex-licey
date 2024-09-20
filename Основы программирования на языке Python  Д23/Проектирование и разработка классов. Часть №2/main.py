# # Kлассная работа
# # Ферзь – 2
# WHITE = 1
# BLACK = 2
#
#
# def opponent(color):
#     if color == WHITE:
#         return BLACK
#     else:
#         return WHITE
#
#
# def print_board(board):
#     print('     +----+----+----+----+----+----+----+----+')
#     for row in range(7, -1, -1):
#         print(' ', row, end='  ')
#         for col in range(8):
#             print('|', board.cell(row, col), end=' ')
#         print('|')
#         print('     +----+----+----+----+----+----+----+----+')
#     print(end='        ')
#     for col in range(8):
#         print(col, end='    ')
#     print()
#
#
# def main():
#     board = Board()
#     while True:
#         print_board(board)
#         print('Команды:')
#         print('    exit                               -- выход')
#         print('    move <row> <col> <row1> <row1>     -- ход из клетки (row, col)')
#         print('                                          в клетку (row1, col1)')
#
#         if board.current_player_color() == WHITE:
#             print('Ход белых:')
#         else:
#             print('Ход чёрных:')
#         command = input()
#         if command == 'exit':
#             break
#         move_type, row, col, row1, col1 = command.split()
#         row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
#         if board.move_piece(row, col, row1, col1):
#             print('Ход успешен')
#         else:
#             print('Координаты некорректы! Попробуйте другой ход!')
#
#
# def correct_coords(row, col):
#     return 0 <= row < 8 and 0 <= col < 8
#
#
# class Board:
#     def __init__(self):
#         self.color = WHITE
#         self.field = []
#         for row in range(8):
#             self.field.append([None] * 8)
#         self.field[0] = [
#             Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
#             King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
#         ]
#         self.field[1] = [
#             Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
#             Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
#         ]
#         self.field[6] = [
#             Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
#             Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
#         ]
#         self.field[7] = [
#             Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
#             King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
#         ]
#
#     def current_player_color(self):
#         return self.color
#
#     def cell(self, row, col):
#         piece = self.field[row][col]
#         if piece is None:
#             return '  '
#         color = piece.get_color()
#         c = 'w' if color == WHITE else 'b'
#         return c + piece.char()
#
#     def get_piece(self, row, col):
#         if correct_coords(row, col):
#             return self.field[row][col]
#         else:
#             return None
#
#     def move_piece(self, row, col, row1, col1):
#         if not correct_coords(row, col) or not correct_coords(row1, col1):
#             return False
#         if row == row1 and col == col1:
#             return False
#         piece = self.field[row][col]
#         if piece is None:
#             return False
#         if piece.get_color() != self.color:
#             return False
#         if self.field[row1][col1] is None:
#             if not piece.can_move(self, row, col, row1, col1):
#                 return False
#         elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
#             if not piece.can_attack(self, row, col, row1, col1):
#                 return False
#         else:
#             return False
#         self.field[row][col] = None
#         self.field[row1][col1] = piece
#         self.color = opponent(self.color)
#         return True
#
#
# class Bishop:
#     def __init__(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def char(self):
#         return 'B'
#
#     def can_move(self, board, row, col, row1, col1):
#         return None
#
#     def can_attack(self, board, row, col, row1, col1):
#         return self.can_move(self, board, row, col, row1, col1)
#
#
# class Pawn:
#     def __init__(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def char(self):
#         return 'P'
#
#     def can_move(self, board, row, col, row1, col1):
#         if col != col1:
#             return False
#
#         if self.color == WHITE:
#             direction = 1
#             start_row = 1
#         else:
#             direction = -1
#             start_row = 6
#
#         # ход на 1 клетку
#         if row + direction == row1:
#             return True
#
#         if (row == start_row
#                 and row + 2 * direction == row1
#                 and board.field[row + direction][col] is None):
#             return True
#
#         return False
#
#     def can_attack(self, board, row, col, row1, col1):
#         direction = 1 if (self.color == WHITE) else -1
#         return (row + direction == row1
#                 and (col + 1 == col1 or col - 1 == col1))
#
#
# class Rook:
#     def __init__(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def char(self):
#         return 'R'
#
#     def can_move(self, board, row, col, row1, col1):
#         if row != row1 and col != col1:
#             return False
#         step = 1 if (row1 >= row) else -1
#         for r in range(row + step, row1, step):
#
#             if not (board.get_piece(r, col) is None):
#                 return False
#
#         step = 1 if (col1 >= col) else -1
#         for c in range(col + step, col1, step):
#
#             if not (board.get_piece(row, c) is None):
#                 return False
#
#         return True
#
#     def can_attack(self, board, row, col, row1, col1):
#         return self.can_move(board, row, col, row1, col1)
#
#
# class Knight:
#
#     def __init__(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def char(self):
#         return 'N'
#
#     def can_move(self, board, row, col, row1, col1):
#         return None
#
#     def can_attack(self, board, row, col, row1, col1):
#         return self.can_move(self, board, row, col, row1, col1)
#
#
# class King:
#
#     def __init__(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def char(self):
#         return 'K'
#
#     def can_move(self, board, row, col, row1, col1):
#         return None
#
#     def can_attack(self, board, row, col, row1, col1):
#         return self.can_move(self, board, row, col, row1, col1)
#
#
# class Queen:
#
#     def __init__(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def char(self):
#         return 'Q'
#
#     def can_move(self, board, row, col, row1, col1):
#         if not correct_coords(row1, col1):
#             return False
#         piece1 = board.get_piece(row1, col1)
#         if not (piece1 is None) and piece1.get_color() == self.color:
#             return False
#         if row == row1 or col == col1:
#             step = 1 if (row1 >= row) else -1
#             for r in range(row + step, row1, step):
#                 if not (board.get_piece(r, col) is None):
#                     return False
#             step = 1 if (col1 >= col) else -1
#             for c in range(col + step, col1, step):
#                 if not (board.get_piece(row, c) is None):
#                     return False
#             return True
#         if row - col == row1 - col1:
#             step = 1 if (row1 >= row) else -1
#             for r in range(row + step, row1, step):
#                 c = col - row + r
#                 if not (board.get_piece(r, c) is None):
#                     return False
#             return True
#         if row + col == row1 + col1:
#             step = 1 if (row1 >= row) else -1
#             for r in range(row + step, row1, step):
#                 c = row + col - r
#                 if not (board.get_piece(r, c) is None):
#                     return False
#             return True
#         return False
#
#     def can_attack(self, board, row, col, row1, col1):
#         return self.can_move(self, board, row, col, row1, col1)
#

# Превращение пешки
class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(self, row, col, row1, col1):
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def is_under_attack(self, row, col, color):
        for i in range(8):
            for j in range(8):
                if self.field[i][j]:
                    if self.field[i][j].get_color() == color and self.field[i][j].can_move(row, col):
                        return True
        return False

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        pwn = Pawn
        if not isinstance(self.field[row][col], pwn):
            return False
        if self.field[row1][col1] is not None:
            if not self.field[row][col].can_attack(self, row, col, row1, col1):
                return False
        else:
            if not self.field[row][col].can_move(self, row, col, row1, col1):
                return False
        p = self.field[row][col]
        self.field[row][col] = None
        if char == 'Q':
            self.field[row1][col1] = Queen(p.get_color())
        elif char == 'R':
            self.field[row1][col1] = Rook(p.get_color())
        elif char == 'B':
            self.field[row1][col1] = Bishop(p.get_color())
        elif char == 'N':
            self.field[row1][col1] = Knight(p.get_color())
        self.color = opponent(self.color)
        return True


class Piece:
    def __init__(self, color):
        self.color = color

    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        if board.cell(row1, col1)[1] != ' ':
            if board.get_piece(row1, col1).get_color() == self.color:
                return False
        return True

    def set_position(self, row, col):
        self.row, self.col = row, col

    def get_color(self):
        return self.color

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Pawn(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if col != col1:
            return False

        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        if row + direction == row1:
            return True

        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True
        return False

    def char(self):
        return 'P'

    def can_attack(self, board, row, col, row1, col1):
        if board.cell(row1, col1)[1] == ' ':
            return False
        if board.get_piece(row1, col1).get_color() == self.color:
            return False
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))


class Rook(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False

        if row != row1 and col != col1:
            return False
        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            if not (board.get_piece(r, col) is None):
                return False
        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            if not (board.get_piece(row, c) is None):
                return False
        return True

    def char(self):
        return 'R'


class Queen(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False

        if abs(row1 - row) == abs(col1 - col):
            stepx = 1 if (col1 >= col) else -1
            stepy = 1 if (row1 >= row) else -1
            for i in range(1, abs(row1 - row)):
                if not (board.get_piece(row + i * stepy, col + i * stepx) is None):
                    return False
            return True
        if row == row1 or col == col1:
            step = 1 if (row1 >= row) else -1
            for r in range(row + step, row1, step):
                if not (board.get_piece(r, col) is None):
                    return False
            step = 1 if (col1 >= col) else -1
            for c in range(col + step, col1, step):
                if not (board.get_piece(row, c) is None):
                    return False
            return True
        return False

    def char(self):
        return 'Q'


class Knight(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if not ((abs(row1 - row) == 2 and abs(col1 - col) == 1) or
                (abs(row1 - row) == 1 and abs(col1 - col) == 2)):
            return False
        return True

    def char(self):
        return 'N'


class Bishop(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if not abs(row1 - row) == abs(col1 - col):
            return False

        stepx = 1 if (col1 >= col) else -1
        stepy = 1 if (row1 >= row) else -1

        for i in range(1, abs(row1 - row)):
            if not (board.get_piece(row + i * stepy, col + i * stepx) is None):
                return False
        return True

    def char(self):
        return 'B'


class King(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if abs(row - row1) > 1 or abs(col - col1) > 1:
            return False
        return True

    def char(self):
        return 'K'


WHITE = 1
BLACK = 2


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


# Таблицы значений функций
class GENII_YANDEX:
    def __call__(self, x):
        return x


class SQRT:
    def __call__(self, x):
        return x ** 0.5


con = {'x': GENII_YANDEX(), 'sqrt_fun': SQRT()}


class ILYA:
    def __init__(self, char_znak, arg1, arg2):
        self.char_znak = char_znak
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, arg):
        if self.arg1 in con:
            a = con[self.arg1](arg)
        else:
            a = int(self.arg1)
        b = con[self.arg2](arg)
        if self.char_znak == '+':
            return a + b
        if self.char_znak == '-':
            return a - b
        if self.char_znak == '*':
            return a * b
        if self.char_znak == '/':
            return a / b
        if self.char_znak == '//':
            return a // b


number = int(input())
for i in range(number):
    command = input().split()
    if command[0] == 'define':
        con[command[1]] = ILYA(command[3], command[2], command[4])
    if command[0] == 'calculate':
        sp = command[2:]
        sp = [int(z) for z in sp]
        ans = con[command[1]]
        for k in sp:
            print(ans(k), end=' ')
# Домашняя работа
# Рокировка
# Преобразования чисел
# Расписание конференции
# Дополнительные задачи
# Файловая система
# Шахматы
