from calendar import c
import sys
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QProgressBar
from UIdesing_py.progress import Progers
from UIdesing_py.finaly import Ui_Form


import os

import openpyxl
from openpyxl import workbook

import re

app = QApplication(sys.argv)

class Root(QWidget):
    def __init__(self):
        super(Root, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.check_nag.clicked.connect(self.open_correct_file)
    # открыть скорректированный файл
    def open_correct_file(self):
        if self.key_control == True:
            self.ui2.settings.setEnabled(True)
            file = os.startfile('try.xlsx') #офигенная вещь , запускает файл
        else:
            # self.ui2.settings.setEnabled(False)

            msg = QMessageBox()
            msg.setText("""Данные в нагрузку не внесены, пожалуста загрузите данные
            """)
            msg.exec()
            pass

    def help(self):
        pass

    def bar(self):
        # self.open_file()
        self.window = Progers()
        self.window.show()
        
        

    
    def rep_btn(self):
        # self.ui = Ui_MainWindow2()
        self.ui2.setupUi(self)
        
        self.key_window = False

        window = Root()
        window.show()

        
        self.ui2.settings.setEnabled(True)

        # self.ui2.menu_2.triggered.connect(self.open_file)
        self.ui2.settings.clicked.connect(self.open_correct_file)
        self.ui2.action_5.triggered.connect(self.bar)







if __name__ == "__main__":

    # app = QApplication(sys.argv)

    window = Root()
    window.show()

    sys.exit(app.exec())