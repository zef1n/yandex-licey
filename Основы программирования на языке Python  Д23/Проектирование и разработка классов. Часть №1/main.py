# # Kлассная работа
# # Конь
# class Knight:
#     def __init__(self, row, col, color):
#         self.row = row
#         self.col = col
#         self.color = color
#
#     def can_move(self, row1, col1):
#         if ((self.col - col1) ** 2 + (self.row - row1) ** 2) == 5:
#             if 0 <= row1 < 8 and 0 <= col1 < 8:
#                 return True
#         return False
#
#     def set_position(self, row1, col1):
#         self.row = row1
#         self.col = col1
#
#     def get_color(self):
#         return self.color
#
#     def char(self):
#         return 'N'
#
#
# # Слон
# class Bishop:
#     def __init__(self, row, col, color):
#         self.row = row
#         self.col = col
#         self.color = color
#
#     def can_move(self, row1, col1):
#         if abs(self.row - row1) == abs(self.col - col1):
#             if 0 <= col1 <= 7 and 0 <= row1 <= 7:
#                 return True
#         return False
#
#     def set_position(self, row1, col1):
#         self.row = row1
#         self.col = col1
#
#     def get_color(self):
#         return self.color
#
#     def char(self):
#         return 'B'
#
#
# # Ферзь
# class Queen:
#     def __init__(self, row, col, color):
#         self.row = row
#         self.col = col
#         self.color = color
#
#     def can_move(self, row1, col1):
#         if 0 <= col1 <= 7 and 0 <= row1 <= 7:
#             if abs(self.row - row1) == abs(self.col - col1) or self.col - col1 == 0 or self.row - row1 == 0:
#                 return True
#             return False
#
#     def set_position(self, row1, col1):
#         self.row = row1
#         self.col = col1
#
#     def get_color(self):
#         return self.color
#
#     def char(self):
#         return 'Q'
#
#
# # Домашняя работа
# # Поля под боем
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
# def correct_coords(row, col):
#     return 0 <= row < 8 and 0 <= col < 8
#
#
# class Queen:
#     def __init__(self, row, col, color):
#         self.row = row
#         self.col = col
#         self.color = color
#
#     def set_position(self, row, col):
#         self.row = row
#         self.col = col
#
#     def char(self):
#         return 'Q'
#
#     def get_color(self):
#         return self.color
#
#     def can_move(self, row, col):
#         if not (0 <= row < 8 and 0 <= col < 8):
#             return False
#         if (abs(self.row - row) == abs(self.col - col)) or (abs(self.row - row) * abs(self.col - col) == 0):
#             return True
#         return False
#
#
# class Knight:
#     def __init__(self, row, col, color):
#         self.row = row
#         self.col = col
#         self.color = color
#
#     def set_position(self, row, col):
#         self.row = row
#         self.col = col
#
#     def char(self):
#         return 'N'
#
#     def get_color(self):
#         return self.color
#
#     def can_move(self, row, col):
#         if not (0 <= row < 8 and 0 <= col < 8):
#             return False
#         if abs(self.col - col) * abs(self.row - row) == 2 and self.row != row and self.col != col:
#             return True
#         return False
#
#
# class Pawn:
#     def __init__(self, row, col, color):
#         self.row = row
#         self.col = col
#         self.color = color
#
#     def set_position(self, row, col):
#         self.row = row
#         self.col = col
#
#     def char(self):
#         return 'P'
#
#     def get_color(self):
#         return self.color
#
#     def can_move(self, row, col):
#         if not (0 <= row < 8 and 0 <= col < 8):
#             return False
#         if self.col != col:
#             return False
#         if self.color == WHITE:
#             direction = 1
#             start_row = 1
#         if not ((not (0 <= row < 8 and 0 <= col < 8)) and (self.col != col) and (self.color == WHITE)):
#             direction = -1
#             start_row = 6
#         if self.row + direction == row:
#             return True
#         if self.row == start_row and self.row + 2 * direction == row:
#             return True
#         return False
#
#
# class Rook:
#     def __init__(self, row, col, color):
#         self.row = row
#         self.col = col
#         self.color = color
#
#     def set_position(self, row, col):
#         self.row = row
#         self.col = col
#
#     def char(self):
#         return 'R'
#
#     def get_color(self):
#         return self.color
#
#     def can_move(self, row, col):
#         if not (0 <= row < 8 and 0 <= col < 8):
#             return False
#
#         if self.row != row and self.col != col:
#             return False
#         return True
#
#
# class Bishop:
#     def __init__(self, row, col, color):
#         self.row = row
#         self.col = col
#         self.color = color
#
#     def set_position(self, row, col):
#         self.row = row
#         self.col = col
#
#     def char(self):
#         return 'B'
#
#     def get_color(self):
#         return self.color
#
#     def can_move(self, row, col):
#         if not (0 <= row < 8 and 0 <= col < 8):
#             return False
#         if abs(self.row - row) == abs(self.col - col):
#             return True
#         return False
#
#
# class Board:
#     def __init__(self):
#         self.field = []
#         for row in range(8):
#             self.field.append([None] * 8)
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
#         if not piece.can_move(row1, col1):
#             return False
#         self.field[row][col] = None
#         self.field[row1][col1] = piece
#         piece.set_position(row1, col1)
#         self.color = opponent(self.color)
#         return True
#
#     def is_under_attack(self, row, col, color):
#         for i in range(8):
#             for j in range(8):
#                 if self.field[i][j] is not None:
#                     piece = self.field[i][j]
#                     if piece.get_color() == color:
#                         if piece.can_move(row, col):
#                             return True
#         return False
#
#
# board = Board()
#
# board.field = [([None] * 8) for i in range(8)]
# board.field[0][0] = Rook(0, 0, WHITE)
# board.field[1][2] = Bishop(1, 2, WHITE)
# coords = ((0, 0), (1, 2))
#
# print('White:')
# for row in range(7, -1, -1):
#     for col in range(8):
#         if (row, col) in coords:
#             print('W', end='')
#         elif board.is_under_attack(row, col, WHITE):
#             print('x', end='')
#         else:
#             print('-', end='')
#     print()
# Почта
from sys import exit


class MailClient:
    def __init__(self, server, user):
        self.s = server
        self.u = user

    d = dict()

    def f(self):
        return self.d

    def list(self):
        self.d[self.s] = self.u


class Receive(MailClient):

    def __init__(self):
        super().f()

    def Mail(self):
        s = input('На какой сервер зайдем? ')
        if s in self.d.keys():
            if type(self.d[s]) == tuple:
                print(f'Получено письмо от пользователя {self.d[s][0]}: {self.d[s][1]}')
            else:
                print('В папке "Вся почта" пока пусто')
        else:
            print('К сожалению, такого сервера не существует ¯\_(ツ)_/¯')


class Send(MailClient):

    def __init__(self):
        super().f()

    def get_key(self, d, value):
        for k, v in d.items():
            if v == value:
                return k

    def send(self):
        un = input('Кому напишем? ')
        if un in self.d.values() and len(self.d[self.get_key(self.d, un)]) > 1:
            tom = input('Введи текст сообщения: ')
            for i in self.d.values():
                if i == un:
                    self.d[self.get_key(self.d, un)] = (i, tom)
            print(f'Сообщение успешно отправлено пользователю {un}!')
        else:
            print('Такого пользователя не существует ¯\_(ツ)_/¯')


def main():
    while True:
        print('Привет! Ты попал(а) на почтовый сервис AmEl!')
        serv = input('На какой сервер зайдем? ')
        name = input('Как тебя звать? ')
        print(f'{name[0].upper() + name[1:].lower()}, добро пожаловать!')
        m = MailClient(serv, name)
        m.list()
        way = input('Что хотим сделать? ')
        if way.lower().strip() == 'отправить сообщение' or way.lower().strip() == 'написать сообщение' \
                or way.lower().strip() == 'написать':
            s = Send()
            s.send()
        elif way.lower().strip() == 'просмотреть ящик' or way.lower().strip() == 'посмотреть сообщения' \
                or way.lower().strip() == 'прочитать сообщения' or way.lower().strip() == 'почитать' \
                or way.lower().strip() == 'посмотреть почту':
            r = Receive()
            r.Mail()
        else:
            print('Ой! Ошибочка вышла...')

        print('/-----------------------------------------\ ')
        s = '|"exit" - выйти                           |\n|"return" - вернуться на домашнюю страницу|'
        print(s)
        print('\-----------------------------------------/ ')
        a = input()
        if a == 'exit':
            exit()
        elif a == 'return':
            pass
        else:
            print('Ой! Ошибочка вышла...')
            exit()


main()
# Дополнительные задачи
# Все фигуры на доске
