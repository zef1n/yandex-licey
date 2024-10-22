# Kлассная работа
# Фокус со словами
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QPushButton
#
#
# class WordTrick(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.first_value = QLineEdit(self)
#         self.second_value = QLineEdit(self)
#         self.trick_button = QPushButton('->', self)
#         self.trick_button.clicked.connect(self.switch_text)
#
#         layout = QHBoxLayout()
#         layout.addWidget(self.first_value)
#         layout.addWidget(self.trick_button)
#         layout.addWidget(self.second_value)
#
#         self.setLayout(layout)
#         self.setWindowTitle('Фокус со словами')
#         self.is_forward = True
#
#     def switch_text(self):
#         if self.is_forward:
#             self.second_value.setText(self.first_value.text())
#             self.first_value.clear()
#             self.trick_button.setText('<-')
#         else:
#             self.first_value.setText(self.second_value.text())
#             self.second_value.clear()
#             self.trick_button.setText('->')
#
#         self.is_forward = not self.is_forward
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = WordTrick()
#     window.show()
#     sys.exit(app.exec())

# Вычисление выражений
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout
#
#
# class Evaluator(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.UI()
#
#     def UI(self):
#         self.setWindowTitle('Вычисление выражений')
#         self.setGeometry(300, 300, 400, 100)
#
#         self.first_value = QLineEdit(self)
#         self.second_value = QLineEdit(self)
#         self.second_value.setReadOnly(True)
#
#         self.trick_button = QPushButton('->', self)
#         self.trick_button.clicked.connect(self.evaluate_expression)
#
#         hbox = QHBoxLayout()
#         hbox.addWidget(self.first_value)
#         hbox.addWidget(self.trick_button)
#         hbox.addWidget(self.second_value)
#
#         self.setLayout(hbox)
#
#     def evaluate_expression(self):
#         expression = self.first_value.text()
#         try:
#             result = eval(expression)
#             self.second_value.setText(str(result))
#         except Exception:
#             self.second_value.setText("Ошибка")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Evaluator()
#     window.show()
#     sys.exit(app.exec())
# Миникалькулятор
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLCDNumber, QLabel
#
#
# class MiniCalculator(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Мини-калькулятор')
#         self.setGeometry(300, 300, 400, 200)
#
#         self.number_1, self.number_2 = QLineEdit(), QLineEdit()
#         self.result_sum, self.result_sub, self.result_mul, self.result_div = \
#             QLCDNumber(), QLCDNumber(), QLCDNumber(), QLCDNumber()
#         self.calculate_button = QPushButton('->')
#         self.calculate_button.clicked.connect(self.calculate)
#
#         input_layout = QVBoxLayout()
#         input_layout.addWidget(QLabel("Первое число (целое):"))
#         input_layout.addWidget(self.number_1)
#         input_layout.addWidget(QLabel("Второе число (целое):"))
#         input_layout.addWidget(self.number_2)
#         input_layout.addWidget(self.calculate_button)
#
#         result_layout = QVBoxLayout()
#         for label, result in zip(['Сумма', 'Разность', 'Произведение', 'Частное'],
#                                  [self.result_sum, self.result_sub, self.result_mul, self.result_div]):
#             hbox = QHBoxLayout()
#             hbox.addWidget(QLabel(label))
#             hbox.addWidget(result)
#             result_layout.addLayout(hbox)
#
#         layout = QHBoxLayout()
#         layout.addLayout(input_layout)
#         layout.addLayout(result_layout)
#         self.setLayout(layout)
#
#     def format_result(self, value):
#         return f"{value:.3f}" if value % 1 != 0 else str(int(value))
#
#     def calculate(self):
#         try:
#             num1, num2 = float(self.number_1.text()), float(self.number_2.text())
#             self.result_sum.display(self.format_result(num1 + num2))
#             self.result_sub.display(self.format_result(num1 - num2))
#             self.result_mul.display(self.format_result(num1 * num2))
#             self.result_div.display(self.format_result(num1 / num2) if num2 != 0 else 'Error')
#         except ValueError:
#             for result in [self.result_sum, self.result_sub, self.result_mul, self.result_div]:
#                 result.display('Error')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MiniCalculator()
#     window.show()
#     sys.exit(app.exec())
# Прятки для виджетов
# import sys
# from PyQt6.QtWidgets import (
#     QApplication, QWidget, QLineEdit, QCheckBox, QVBoxLayout, QHBoxLayout
# )
#
#
# class WidgetsHideNSeek(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.edit1 = QLineEdit(self)
#         self.edit2 = QLineEdit(self)
#         self.edit3 = QLineEdit(self)
#         self.edit4 = QLineEdit(self)
#
#         self.checkbox1 = QCheckBox('edit1', self)
#         self.checkbox2 = QCheckBox('edit2', self)
#         self.checkbox3 = QCheckBox('edit3', self)
#         self.checkbox4 = QCheckBox('edit4', self)
#
#         self.checkbox1.stateChanged.connect(self.toggle_widget_visibility)
#         self.checkbox2.stateChanged.connect(self.toggle_widget_visibility)
#         self.checkbox3.stateChanged.connect(self.toggle_widget_visibility)
#         self.checkbox4.stateChanged.connect(self.toggle_widget_visibility)
#
#         checkbox_layout = QVBoxLayout()
#         checkbox_layout.addWidget(self.checkbox1)
#         checkbox_layout.addWidget(self.checkbox2)
#         checkbox_layout.addWidget(self.checkbox3)
#         checkbox_layout.addWidget(self.checkbox4)
#
#         edit_layout = QVBoxLayout()
#         edit_layout.addWidget(self.edit1)
#         edit_layout.addWidget(self.edit2)
#         edit_layout.addWidget(self.edit3)
#         edit_layout.addWidget(self.edit4)
#
#         main_layout = QHBoxLayout()
#         main_layout.addLayout(checkbox_layout)
#         main_layout.addLayout(edit_layout)
#
#         self.setLayout(main_layout)
#         self.setWindowTitle("Прятки для виджетов")
#
#     def toggle_widget_visibility(self):
#         checkbox = self.sender()
#
#         if checkbox == self.checkbox1:
#             self.edit1.setVisible(not self.checkbox1.isChecked())
#         elif checkbox == self.checkbox2:
#             self.edit2.setVisible(not self.checkbox2.isChecked())
#         elif checkbox == self.checkbox3:
#             self.edit3.setVisible(not self.checkbox3.isChecked())
#         elif checkbox == self.checkbox4:
#             self.edit4.setVisible(not self.checkbox4.isChecked())
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = WidgetsHideNSeek()
#     window.show()
#     sys.exit(app.exec())

# Домашняя работа
# Арифмометр
# from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
#
#
# class Arifmometr(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.first_value = QLineEdit("0", self)
#         self.second_value = QLineEdit("0", self)
#         self.result = QLineEdit("0", self)
#         self.result.setReadOnly(True)
#
#         self.add_button = QPushButton("+", self)
#         self.substract_button = QPushButton("-", self)
#         self.multiply_button = QPushButton("*", self)
#
#         self.add_button.clicked.connect(self.calculate)
#         self.substract_button.clicked.connect(self.calculate)
#         self.multiply_button.clicked.connect(self.calculate)
#
#         button_layout = QHBoxLayout()
#         button_layout.addWidget(self.add_button)
#         button_layout.addWidget(self.substract_button)
#         button_layout.addWidget(self.multiply_button)
#
#         input_layout = QHBoxLayout()
#         input_layout.addWidget(self.first_value)
#         input_layout.addLayout(button_layout)
#         input_layout.addWidget(self.second_value)
#
#         main_layout = QVBoxLayout()
#         main_layout.addLayout(input_layout)
#         main_layout.addWidget(self.result)
#
#         self.setLayout(main_layout)
#         self.setWindowTitle("Арифмометр")
#
#     def calculate(self):
#         try:
#             num1 = int(self.first_value.text())
#             num2 = int(self.second_value.text())
#         except ValueError:
#             self.result.setText("Ошибка")
#             return
#
#         operation = self.sender()
#         if operation == self.add_button:
#             res = num1 + num2
#         elif operation == self.substract_button:
#             res = num1 - num2
#         elif operation == self.multiply_button:
#             res = num1 * num2
#         self.result.setText(str(res))
#
#
# if __name__ == '__main__':
#     app = QApplication([])
#     window = Arifmometr()
#     window.show()
#     app.exec()
# Азбука Морзе 2
# from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
#
#
# class MorseCode(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.result = QLineEdit(self)
#         self.morse_code_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
#                                 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
#                                 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
#                                 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...',
#                                 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
#                                 'y': '-.--', 'z': '--..'}
#         self.alphabet_buttons = {}
#         main_layout = QVBoxLayout()
#         main_layout.addWidget(self.result)
#         row_layout = QHBoxLayout()
#         for index, letter in enumerate(self.morse_code_dict):
#             button = QPushButton(letter.upper(), self)
#             button.clicked.connect(self.add_morse_code)
#             self.alphabet_buttons[letter] = button
#             row_layout.addWidget(button)
#             if (index + 1) % 6 == 0:
#                 main_layout.addLayout(row_layout)
#                 row_layout = QHBoxLayout()
#         if row_layout.count() > 0:
#             main_layout.addLayout(row_layout)
#         self.setLayout(main_layout)
#         self.setWindowTitle("Азбука Морзе 2")
#
#     def add_morse_code(self):
#         button = self.sender()
#         letter = button.text().lower()
#         morse_code = self.morse_code_dict[letter]
#         current_text = self.result.text()
#         new_text = current_text + morse_code  # Убираем пробел между символами
#         self.result.setText(new_text)
#
#
# if __name__ == '__main__':
#     app = QApplication([])
#     window = MorseCode()
#     window.show()
#     app.exec()
# Крестики нолики QT edition
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.current_player = 'X'
        self.create_widgets()
        self.create_layout()
        self.setWindowTitle("Крестики-нолики")

    def create_widgets(self):
        self.button_grid = [[self.create_game_button() for _ in range(3)] for _ in range(3)]

        self.x_radio = QRadioButton("Первый игрок X")
        self.o_radio = QRadioButton("Первый игрок O")
        self.x_radio.setChecked(True)

        self.result_label = QLabel('')
        self.new_game_button = QPushButton('Новая игра')

        self.new_game_button.clicked.connect(self.new_game)
        self.x_radio.toggled.connect(self.new_game)
        self.o_radio.toggled.connect(self.new_game)

    def create_layout(self):
        main_layout = QVBoxLayout()

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.x_radio)
        radio_layout.addWidget(self.o_radio)
        main_layout.addLayout(radio_layout)

        for row in self.button_grid:
            row_layout = QHBoxLayout()
            for button in row:
                row_layout.addWidget(button)
            main_layout.addLayout(row_layout)

        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.new_game_button)

        self.setLayout(main_layout)

    def create_game_button(self):
        button = QPushButton('')
        button.setFixedSize(100, 100)
        button.clicked.connect(self.handle_turn)
        return button

    def handle_turn(self):
        button = self.sender()
        if button.text() or self.result_label.text():
            return
        button.setText(self.current_player)
        if self.check_winner():
            self.result_label.setText(f'Победил {self.current_player}!')
            self.disable_buttons()
        elif self.check_draw():
            self.result_label.setText('Ничья!')
            self.disable_buttons()
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for row in self.button_grid:
            if row[0].text() == row[1].text() == row[2].text() != '':
                return True
        for col in range(3):
            if self.button_grid[0][col].text() == self.button_grid[1][col].text() == self.button_grid[2][
                col].text() != '':
                return True
        if self.button_grid[0][0].text() == self.button_grid[1][1].text() == self.button_grid[2][2].text() != '':
            return True
        if self.button_grid[0][2].text() == self.button_grid[1][1].text() == self.button_grid[2][0].text() != '':
            return True
        return False

    def check_draw(self):
        return all(button.text() for row in self.button_grid for button in row)

    def disable_buttons(self):
        for row in self.button_grid:
            for button in row:
                button.setEnabled(False)

    def new_game(self):
        self.current_player = 'X' if self.x_radio.isChecked() else 'O'
        self.result_label.setText('')
        for row in self.button_grid:
            for button in row:
                button.setText('')
                button.setEnabled(True)


if __name__ == '__main__':
    app = QApplication([])
    window = TicTacToe()
    window.show()
    app.exec()
# Заказ в Макдональдсе
# Дополнительные задачи
# Калькулятор
# Ним наносит ответный удар
# Заказ в Макдональдсе — 2
