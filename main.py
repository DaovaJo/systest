import os
import re
import sys
import time
from calendar import c

import openpyxl
from openpyxl import workbook
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox, QProgressBar, QVBoxLayout, QWidget)

from fnc.func import Functional
from newds import Ui_Form
# from UIdesing_py.finaly import Ui_Form
# from UIdesing_py.progress import Progers

# app = QApplication(sys.argv)

class Root(QWidget):
    def __init__(self):
        super(Root, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.funcsh = Functional()
        
        self.ui.check_nag.clicked.connect(self.funcsh.open_correct_file)
        self.ui.change_teach.clicked.connect(self.open_editor)
        
    
    def open_editor(self):
        window = Functional()
        window.show()
        
        




if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = Root()
    window.show()

    sys.exit(app.exec())