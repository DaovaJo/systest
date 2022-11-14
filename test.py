import sys
import time
from tokenize import Double
import os
import openpyxl 
import re
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QProgressBar, QPushButton
from PySide6 import QtCore, QtWidgets, QtGui
from tryui import Ui_MainWindow3


class Progers(QtWidgets.QMainWindow):
    def __init__(self):
        super(Progers, self).__init__()

        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)

        self.key_control = False
        self.a = 1
        self.f = 1
        self.teacher = "Простомолотов Андрей Сергеевич"
        self.d = 11
        self.c = 0
        self.cc = list()
        number = None

        self.ui.pushButton.clicked.connect(self.run)
        # print(self.run())

        #Данная функция занимается переносом знчений в нашу форму для нагрузки
    def replacing(self, l0,  Data, Time, Class, Subjects, Group, More, Event, Teach, Dep, Id):
        
        D = 'D' + str(self.d); P = 'P' + str(self.d); Q = 'Q' + str(self.d); R = 'R' + str(self.d); J = 'J' + str(self.d); N = 'N' + str(self.d)

        S = 'S' + str(self.d)
        T = 'T' + str(self.d)
        U = 'U' + str(self.d)
        AJ = 'AJ' + str(self.d)
        AI = 'AI' + str(self.d)

        
        book = openpyxl.open('try.xlsx')
        sheet = book.active

# Данные из выписки 
        sheet[D] = Data
        sheet[P] = Subjects
        sheet[Q] = Group
        sheet[R] = More
# Данные для формул 
        cl_J = 'J' + str(sheet[J].row)
        cl_N = 'N' + str(sheet[N].row)

        fr_lect = str('=IF(J14="Лекции";N14;"")')

        
        sheet[S] = fr_lect

      

        print(f'=IF({cl_J}="Лекции";{cl_N};"")')
    

# Формулы для счета нагрузки
        # sheet[S] = '=ЕСЛИ({sheet[J]}="Лекции";{sheet[N]};"")'
        # sheet[T] = ('=ЕСЛИ(ИЛИ({J}="СПЗ";;{J}="Семинары ИПЗ";);{N};"")')
        # sheet[U] = '=ЕСЛИ({J}="Консультации";{N};"")'
        # sheet[AJ] = '=СУММ({S}:{AI})'

        # sheet['S'] = "ЕСЛИ(S='Лекции';S;'')"




        book.save('try.xlsx')
        book.close()
        self.d = self.d + 1

    def run(self):
            
                folder = QFileDialog.getExistingDirectory(self)
                f = os.listdir(folder) #получаем нужную папку
                print(folder, f)
                counter = 1

                for i in f:
                    global c
                    global lst
                    
                    

                    time.sleep(0.1)
                    self.ui.progressBar.setValue(round((f.index(i)+100/len(f)-f.index(i)) * counter))
                    print(len(f))
                    print(round((f.index(i)+100/len(f)-f.index(i)) * counter))
                    
                    counter = counter + 1
                    file = folder + "/" + i
                    file_name = os.path.abspath(file) #поправляем путь, делаем его адеватным
                    print(file_name)

                    book = openpyxl.open(file_name, read_only = True)
                    sheet = book.active
                        
                    cells = sheet['A11':'M500']
                    for Data, n, nl, Time, Class, Subjects, none, Group, More, Event, Teach, Dep, Id in cells:
                        cc = list()
                        # print(Data)
                            
                        if Teach.value == self.teacher: #and Departmant.value == 'Кафедра информационных систем':
                            Data = Data.value  
                            Time = Time.value
                            Class = Class.value
                            Subjects = Subjects.value
                            Group = Group.value
                            More = More.value
                            Event = Event.value
                            Teach = Teach.value
                            Dep = Dep.value
                            Id = Id.value
                                    # print(Group)
                            # self.search_group(Group)
                                    # print(num)
                            print(Data, Time, Class, Subjects, Group, More, Event, Teach, Dep, Id)
                            self.replacing(10, Data, Time, Class, Subjects, Group, More, Event, Teach, Dep, Id)
                        else:
                            continue
                        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    demo = Progers()
    demo.show()

    


    sys.exit(app.exec())
