# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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

class Ui_MainWindow2(object):
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
" \n"
"QPushButton:disabled{\n"
"	background-color: #ff7f7f\n"
"}\n"
"")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 140, 761, 391))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../../Downloads/\u041b\u043e\u0433\u043e (1).jpg"))

        self.gridLayout.addWidget(self.label, 0, 1, 5, 1)

        self.nag = QPushButton(self.gridLayoutWidget)
        self.nag.setObjectName(u"nag")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nag.sizePolicy().hasHeightForWidth())
        self.nag.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setKerning(True)
        self.nag.setFont(font1)
        self.nag.setStyleSheet(u"")

        self.gridLayout.addWidget(self.nag, 2, 0, 1, 1)

        self.pps = QPushButton(self.gridLayoutWidget)
        self.pps.setObjectName(u"pps")
        sizePolicy1.setHeightForWidth(self.pps.sizePolicy().hasHeightForWidth())
        self.pps.setSizePolicy(sizePolicy1)
        self.pps.setFont(font1)
        self.pps.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pps, 0, 0, 1, 1)

        self.settings = QPushButton(self.gridLayoutWidget)
        self.settings.setObjectName(u"settings")
        sizePolicy1.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy1)
        self.settings.setFont(font1)
        self.settings.setStyleSheet(u"")

        self.gridLayout.addWidget(self.settings, 1, 0, 1, 1)

        self.help = QPushButton(self.gridLayoutWidget)
        self.help.setObjectName(u"help")
        sizePolicy1.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy1)
        self.help.setFont(font1)
        self.help.setStyleSheet(u"")

        self.gridLayout.addWidget(self.help, 3, 0, 1, 1)

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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuafqks = QMenu(self.menubar)
        self.menuafqks.setObjectName(u"menuafqks")
        self.menu_2 = QMenu(self.menuafqks)
        self.menu_2.setObjectName(u"menu_2")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuafqks.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menuafqks.addAction(self.menu_2.menuAction())
        self.menuafqks.addAction(self.action_2)
        self.menu_2.addAction(self.action_5)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0444\u0435\u0434\u0440\u0430 \u041c\u0438\u0415\u041d\u0414", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0444\u0435\u0434\u0440\u0430 \u0418\u0421", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.label.setText("")
        self.nag.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.pps.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e \u041f\u041f\u0421", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043d\u0430\u0433\u0440\u0443\u0437\u043a\u0443", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.label_2.setText("")
        self.menuafqks.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b\u044b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u043e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0444\u0435\u0434\u0440\u044b", None))
    # retranslateUi

