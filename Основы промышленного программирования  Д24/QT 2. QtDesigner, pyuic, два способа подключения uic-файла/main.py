# Kлассная работа
# Красивый калькулятор
from PyQt6 import QtWidgets, uic
import sys
import math


class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)

        self.btn0.clicked.connect(lambda: self.input_digit('0'))
        self.btn1.clicked.connect(lambda: self.input_digit('1'))
        self.btn2.clicked.connect(lambda: self.input_digit('2'))
        self.btn3.clicked.connect(lambda: self.input_digit('3'))
        self.btn4.clicked.connect(lambda: self.input_digit('4'))
        self.btn5.clicked.connect(lambda: self.input_digit('5'))
        self.btn6.clicked.connect(lambda: self.input_digit('6'))
        self.btn7.clicked.connect(lambda: self.input_digit('7'))
        self.btn8.clicked.connect(lambda: self.input_digit('8'))
        self.btn9.clicked.connect(lambda: self.input_digit('9'))

        self.current_value = ''
        self.operator = ''
        self.operand1 = None
        self.waiting_for_operand2 = False
        self.btn_dot.clicked.connect(self.input_dot)

        self.btn_plus.clicked.connect(lambda: self.set_operator('+'))
        self.btn_minus.clicked.connect(lambda: self.set_operator('-'))
        self.btn_mult.clicked.connect(lambda: self.set_operator('*'))
        self.btn_div.clicked.connect(lambda: self.set_operator('/'))
        self.btn_pow.clicked.connect(lambda: self.set_operator('^'))

        self.btn_sqrt.clicked.connect(self.calculate_sqrt)
        self.btn_fact.clicked.connect(self.calculate_fact)

        self.btn_eq.clicked.connect(self.calculate_result)
        self.btn_clear.clicked.connect(self.clear_all)

    def input_digit(self, digit):
        if self.waiting_for_operand2:
            self.current_value = digit
            self.waiting_for_operand2 = False
        else:
            self.current_value += digit
        self.update_display()

    def input_dot(self):
        if '.' not in self.current_value:
            if self.current_value == '':
                self.current_value = '0.'
            else:
                self.current_value += '.'
            self.update_display()

    def set_operator(self, op):
        if self.current_value == '':
            return
        if self.operand1 is not None and not self.waiting_for_operand2:
            self.calculate_result()
        else:
            try:
                self.operand1 = float(self.current_value)
            except ValueError:
                self.show_error("че написал то?")
                return
        self.operator = op
        self.waiting_for_operand2 = True

    def calculate_result(self):
        if self.operator == '':
            return
        try:
            operand2 = float(self.current_value)
        except ValueError:
            self.show_error("че написал то?")
            return

        try:
            if self.operator == '+':
                result = self.operand1 + operand2
            elif self.operator == '-':
                result = self.operand1 - operand2
            elif self.operator == '*':
                result = self.operand1 * operand2
            elif self.operator == '/':
                if operand2 == 0:
                    self.show_error("не дели на ноль!!!")
                    return
                result = self.operand1 / operand2
            elif self.operator == '^':
                result = self.operand1 ** operand2
            else:
                self.show_error("че сделал?")
                return
            self.current_value = str(result)
            self.update_display()
            self.operator = ''
            self.operand1 = result
            self.waiting_for_operand2 = True
        except Exception as e:
            self.show_error(str(e))

    def calculate_sqrt(self):
        try:
            value = float(self.current_value)
            if value < 0:
                self.show_error("корень из отрицательного числа, ну ты вообще")
                return
            result = math.sqrt(value)
            self.current_value = str(result)
            self.update_display()
        except ValueError:
            self.show_error("че написал то?")

    def calculate_fact(self):
        try:
            value = float(self.current_value)
            if value < 0 or not value.is_integer():
                self.show_error("факториал определил для отрицательных чисел,")
                return
            result = math.factorial(int(value))
            self.current_value = str(result)
            self.update_display()
        except (ValueError, OverflowError):
            self.show_error("слишком большое число")

    def clear_all(self):
        self.current_value = ''
        self.operator = ''
        self.operand1 = None
        self.waiting_for_operand2 = False
        self.update_display()

    def update_display(self):
        self.table.display(self.current_value)

    def show_error(self, message):
        error_dialog = QtWidgets.QErrorMessage(self)
        error_dialog.showMessage(message)


#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     window = Calculator()
#     window.show()
#     sys.exit(app.exec())
# Текстовый флаг
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QPushButton, QButtonGroup, QVBoxLayout, \
    QGridLayout
from PyQt6.QtCore import Qt


class FlagMaker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Текстовый флаг')
        self.setFixedSize(400, 300)

        # Создаем группы кнопок
        self.color_group_1 = QButtonGroup(self)
        self.color_group_2 = QButtonGroup(self)
        self.color_group_3 = QButtonGroup(self)
        colors = ['Синий', 'Красный', 'Зелёный']

        layout = QVBoxLayout()
        grid = QGridLayout()

        # Добавляем метки для столбцов
        label1 = QLabel('Цвет №1')
        label2 = QLabel('Цвет №2')
        label3 = QLabel('Цвет №3')
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 0, 2)

        for i, group in enumerate([self.color_group_1, self.color_group_2, self.color_group_3]):
            for j, color in enumerate(colors):
                radio = QRadioButton(color)
                group.addButton(radio)
                grid.addWidget(radio, j + 1, i)

        layout.addLayout(grid)
        self.make_flag = QPushButton('Сделать флаг')
        self.make_flag.clicked.connect(self.make_flag_clicked)
        layout.addWidget(self.make_flag)

        self.result = QLabel('')
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result)

        self.setLayout(layout)

    def make_flag_clicked(self):
        selected = []
        for group in [self.color_group_1, self.color_group_2, self.color_group_3]:
            button = group.checkedButton()
            if button:
                selected.append(button.text())
        if len(selected) == 0:
            result_text = 'Цвета не выбраны'
        elif len(selected) == 1:
            result_text = f'Цвет: {selected[0]}'
        else:
            result_text = "Цвета: " + ', '.join(selected[:-1]) + " и " + selected[-1]
        self.result.setText(result_text)


#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = FlagMaker()
#     window.show()
#     sys.exit(app.exec())

# Минипланировщик
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QCalendarWidget, QTimeEdit, \
    QPushButton, QListWidget, QLabel
from PyQt6.QtCore import QDateTime


class SimplePlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Минипланировщик")
        self.events = []

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()

        self.calendarWidget = QCalendarWidget()
        left_layout.addWidget(self.calendarWidget)

        event_name_label = QLabel("Название события")
        self.lineEdit = QLineEdit()
        left_layout.addWidget(event_name_label)
        left_layout.addWidget(self.lineEdit)

        time_label = QLabel("Время")
        self.timeEdit = QTimeEdit()
        left_layout.addWidget(time_label)
        left_layout.addWidget(self.timeEdit)

        self.addEventBtn = QPushButton("Добавить")
        left_layout.addWidget(self.addEventBtn)

        self.eventList = QListWidget()

        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.eventList)

        self.setLayout(main_layout)

        self.addEventBtn.clicked.connect(self.add_event)

    def add_event(self):
        event_name = self.lineEdit.text().strip()
        date = self.calendarWidget.selectedDate()
        time = self.timeEdit.time()
        datetime = QDateTime(date, time)
        self.events.append((datetime, event_name))
        self.events.sort(key=lambda x: x[0])
        self.eventList.clear()
        for event_datetime, event_name in self.events:
            datetime_str = event_datetime.toString("yyyy-MM-dd HH:mm:ss")
            item_text = f"{datetime_str} - {event_name}"
            self.eventList.addItem(item_text)
            self.lineEdit.clear()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = SimplePlanner()
#     window.show()
#     sys.exit(app.exec())
# Домашняя работа
# Записная книжка
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget, QLabel
)
from PyQt6.QtCore import Qt


class MyNotes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Записная книжка")
        self.setFixedSize(400, 300)

        main_layout = QVBoxLayout()

        input_layout = QHBoxLayout()

        name_label = QLabel("Имя:")
        self.contactName = QLineEdit()
        self.contactName.setPlaceholderText("Введите имя")
        input_layout.addWidget(name_label)
        input_layout.addWidget(self.contactName)

        phone_label = QLabel("Телефон:")
        self.contactNumber = QLineEdit()
        self.contactNumber.setPlaceholderText("Введите номер телефона")
        input_layout.addWidget(phone_label)
        input_layout.addWidget(self.contactNumber)

        main_layout.addLayout(input_layout)

        self.addContactBtn = QPushButton("Добавить")
        self.addContactBtn.clicked.connect(self.add_contact)
        main_layout.addWidget(self.addContactBtn)

        self.contactList = QListWidget()
        main_layout.addWidget(self.contactList)

        self.setLayout(main_layout)

    def add_contact(self):
        name = self.contactName.text().strip()
        number = self.contactNumber.text().strip()

        if name and number:
            contact = f"{name} {number}"
            self.contactList.addItem(contact)
            self.contactName.clear()
            self.contactNumber.clear()
        else:

            pass


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyNotes()
#     window.show()
#     sys.exit(app.exec())

# Widget Art
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt6.QtCore import Qt


class WidgetArt(QWidget):
    def __init__(self, mat):
        super().__init__()
        self.setWindowTitle("Widget Art")
        self.widgetArt = QGridLayout()
        self.setLayout(self.widgetArt)

        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                btn = QPushButton("*" if cell == 1 else "")
                btn.setFixedSize(40, 40)
                btn.setEnabled(False)
                self.widgetArt.addWidget(btn, i, j)


if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    ]
    app = QApplication(sys.argv)
    art = WidgetArt(matrix)
    art.show()
    sys.exit(app.exec())

# Псевдоним. Возвращение
# Дополнительные задачи
# Антиплагиат v0.0001
