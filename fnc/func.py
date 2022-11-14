# ФУНКЦИОНАЛ ПО
import sys
import time
from tokenize import Double
import os
import openpyxl 
import re
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QProgressBar, QGridLayout, QPushButton, QLineEdit, QLabel
# from change import Window
from langdetect import detect

class Functional(QWidget):
    def __init__(self):
        super().__init__()
        self.teacher = list()

        self.le_num1 = QLineEdit()
        self.pb_num1 = QPushButton('добавить преподавателя')
        self.pb_num1.clicked.connect(self.edit_teach)

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel('Введите ФИО преподавателя'))
        layout.addWidget(self.le_num1)
        layout.addWidget(self.pb_num1)
            
            

    def open_correct_file(self):
        try:
            file = os.startfile('try.xlsx') #офигенная вещь , запускает файл
        except:
            msg = QMessageBox()
            msg.setText("""Упс...проверьте наличие файла в проекте""")
            msg.exec()
    
    def change_teacher(self):
        teacher = list()

    def edit_teach(self):
        value = self.le_num1.text()
        print(value)
        # создаю список из введенных слов для проверки на наличии болие 2 слов а именно Имени и Фамилии
        chek_value = value.split(" ")
        print(chek_value)
        print(detect(value))
        # Проверка на количество слов ввода (P.S. Обязательно больше 1 слова, так как либо будет ФИО либо ФИ но никак не И, О, Ф и наоборот)
        if len(chek_value) < 2:
            # Выводим окно сообщения
            msg1 = QMessageBox()
            msg1.setText("""Введите полностью ФИО""")
            msg1.exec()
        # Проверка на язык ввода
        elif detect(value) != "ru":
            msg2 = QMessageBox()
            msg2.setText("""Введите ФИО на русском""")
            msg2.exec()
        else:
            self.teacher.append(value)
            print(self.teacher)




# if __name__ == '__main__':
    
#     app = QApplication([])

#     mw = Functional()
#     mw.show()

#     app.exec()
    
    
   