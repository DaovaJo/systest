# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu2.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(56)
        sizePolicy.setVerticalStretch(26)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 550))
        MainWindow.setMaximumSize(QSize(800, 650))
        font = QFont()
        font.setFamilies([u"Rockwell"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: #ff0000;\n"
"	color: #fff\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #f0c662;\n"
"	color: #000000\n"
"}\n"
"\n"
"")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(370, 150, 431, 391))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../../Downloads/\u041b\u043e\u0433\u043e (1).jpg"))

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(190, 40, 421, 131))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 0, 419, 129))
        self.label_2.setPixmap(QPixmap(u"../../Downloads/\u043b\u043e\u0433\u043e \u043d\u0430 \u043c\u0443\u0438\u0432.png"))
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 250, 346, 191))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.pushButton.setFont(font1)

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setFont(font1)

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuafqks = QMenu(self.menubar)
        self.menuafqks.setObjectName(u"menuafqks")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuafqks.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menuafqks.addAction(self.action)
        self.menuafqks.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0444\u0435\u0434\u0440\u0430 \u041c\u0438\u0415\u041d\u0414", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0444\u0435\u0434\u0440\u0430 \u0418\u0421", None))
        self.label.setText("")
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0444\u0435\u0434\u0440\u0430 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0444\u0435\u0434\u0440\u0430 \u041c\u0438\u0415\u041d\u0414", None))
        self.menuafqks.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b\u044b", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0444\u0435\u0434\u0440\u044b", None))
    # retranslateUi

