# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(491, 431)
        Form.setStyleSheet(u"QWidget{\n"
"	background-color: #121212;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: #78b0e9;\n"
"	border-radius: 20px;\n"
"	font-weight: 700;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #3c5874;\n"
"}\n"
"\n"
"QGridLayout{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QTextEdit{\n"
"	font-size:16px;\n"
"	color: #fff;\n"
"	opacity: 80%;\n"
"   padding: 10% 10%;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #fff;\n"
"}")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 320, 311, 51))
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 130, 401, 183))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(399, 61))
        self.textEdit.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(399, 61))

        self.gridLayout.addWidget(self.textEdit_2, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

