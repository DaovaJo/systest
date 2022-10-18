# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finaly.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1240, 824)
        Form.setMinimumSize(QSize(1240, 824))
        Form.setMaximumSize(QSize(1240, 824))
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setStyleSheet(u"QWidget {\n"
"    background: #171A18;\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 10vh;\n"
"	font-family: 'Amatica SC';\n"
"	font-style: normal;\n"
"	font-weight: 700;\n"
"	\n"
"	color: #04E500;\n"
"}\n"
"\n"
"QPushButton{\n"
"	cursor: Pointing Hand;\n"
"	width: 520px;\n"
"	height: 72px;\n"
"\n"
"	border-radius: 20px;\n"
"    border: 2px solid #AEAFAE; /* \u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0440\u0430\u043c\u043a\u0438 */\n"
"   \n"
"	font-family: 'Irish Grover';\n"
"	font-style: normal;\n"
"	font-weight: 400;\n"
"	font-size: 18px; \n"
"	color: #fff;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #00E349, stop:1 #00E3D1);\n"
"	border: transparent;\n"
"	color: #171A18;\n"
"}")
        self.IMG_1 = QLabel(Form)
        self.IMG_1.setObjectName(u"IMG_1")
        self.IMG_1.setGeometry(QRect(1070, 10, 161, 141))
        self.IMG_1.setPixmap(QPixmap(u"../../Downloads/obj.png"))
        self.IMG_2 = QLabel(Form)
        self.IMG_2.setObjectName(u"IMG_2")
        self.IMG_2.setGeometry(QRect(30, 660, 161, 141))
        self.IMG_2.setPixmap(QPixmap(u"../../Downloads/2obj.png"))
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(230, 80, 781, 80))
        self.INTRO = QHBoxLayout(self.horizontalLayoutWidget)
        self.INTRO.setObjectName(u"INTRO")
        self.INTRO.setContentsMargins(0, 0, 0, 0)
        self.PROGRAMM = QLabel(self.horizontalLayoutWidget)
        self.PROGRAMM.setObjectName(u"PROGRAMM")
        font = QFont()
        font.setFamilies([u"Amatica SC"])
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        self.PROGRAMM.setFont(font)
        self.PROGRAMM.setStyleSheet(u"<!DOCTYPE html>\n"
"<html>\n"
"<head>\n"
"  <meta charset=\"utf-8\" />\n"
"  <style>\n"
"   .colortext {\n"
"     color: #FFF; /* \u041a\u0440\u0430\u0441\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u044f */\n"
"   }\n"
"  </style>\n"
" </head>\n"
"\n"
" <body>\n"
"  <p>\u041f\u0420\u041e\u0413\u0420\u0410\u041c\u041c\u0410<span class=\"colortext\">\u0414\u041b\u042f \u0424\u041e\u0420\u041c\u0418\u0420\u041e\u0412\u0410\u041d\u0418\u042f</span>\u041d\u0410\u0413\u0420\u0423\u0417\u041a\u0418</p>\n"
" </body>\n"
"</html>")
        self.PROGRAMM.setAlignment(Qt.AlignCenter)

        self.INTRO.addWidget(self.PROGRAMM)

        self.FOR = QLabel(self.horizontalLayoutWidget)
        self.FOR.setObjectName(u"FOR")
        font1 = QFont()
        font1.setFamilies([u"Amatica SC"])
        font1.setPointSize(25)
        font1.setBold(False)
        font1.setItalic(False)
        self.FOR.setFont(font1)
        self.FOR.setStyleSheet(u"QLabel{\n"
"    font-size: 10vh;\n"
"	font-family: 'Amatica SC';\n"
"	font-style: normal;\n"
"	font-weight: 400;\n"
"	\n"
"	color: #FFF;\n"
"}")
        self.FOR.setAlignment(Qt.AlignCenter)

        self.INTRO.addWidget(self.FOR)

        self.NAG = QLabel(self.horizontalLayoutWidget)
        self.NAG.setObjectName(u"NAG")
        self.NAG.setFont(font)
        self.NAG.setStyleSheet(u"<!DOCTYPE html>\n"
"<html>\n"
"<head>\n"
"  <meta charset=\"utf-8\" />\n"
"  <style>\n"
"   .colortext {\n"
"     color: #FFF; /* \u041a\u0440\u0430\u0441\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u044f */\n"
"   }\n"
"  </style>\n"
" </head>\n"
"\n"
" <body>\n"
"  <p>\u041f\u0420\u041e\u0413\u0420\u0410\u041c\u041c\u0410<span class=\"colortext\">\u0414\u041b\u042f \u0424\u041e\u0420\u041c\u0418\u0420\u041e\u0412\u0410\u041d\u0418\u042f</span>\u041d\u0410\u0413\u0420\u0423\u0417\u041a\u0418</p>\n"
" </body>\n"
"</html>")
        self.NAG.setAlignment(Qt.AlignCenter)

        self.INTRO.addWidget(self.NAG)

        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(360, 180, 531, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.creat_nag = QPushButton(self.verticalLayoutWidget)
        self.creat_nag.setObjectName(u"creat_nag")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.creat_nag.sizePolicy().hasHeightForWidth())
        self.creat_nag.setSizePolicy(sizePolicy)
        self.creat_nag.setMinimumSize(QSize(320, 72))
        self.creat_nag.setMaximumSize(QSize(520, 72))
        self.creat_nag.setCursor(QCursor(Qt.PointingHandCursor))
        self.creat_nag.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.creat_nag)

        self.check_nag = QPushButton(self.verticalLayoutWidget)
        self.check_nag.setObjectName(u"check_nag")
        sizePolicy.setHeightForWidth(self.check_nag.sizePolicy().hasHeightForWidth())
        self.check_nag.setSizePolicy(sizePolicy)
        self.check_nag.setMinimumSize(QSize(520, 72))
        self.check_nag.setMaximumSize(QSize(320, 72))
        self.check_nag.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.check_nag)

        self.change_teach = QPushButton(self.verticalLayoutWidget)
        self.change_teach.setObjectName(u"change_teach")
        self.change_teach.setMinimumSize(QSize(520, 72))
        self.change_teach.setMaximumSize(QSize(520, 72))
        self.change_teach.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.change_teach)

        self.helper = QLabel(self.verticalLayoutWidget)
        self.helper.setObjectName(u"helper")
        sizePolicy.setHeightForWidth(self.helper.sizePolicy().hasHeightForWidth())
        self.helper.setSizePolicy(sizePolicy)
        self.helper.setMinimumSize(QSize(520, 18))
        self.helper.setMaximumSize(QSize(520, 18))
        self.helper.setCursor(QCursor(Qt.ArrowCursor))
        self.helper.setStyleSheet(u"QLabel{\n"
"color: #AEAFAE;\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"}\n"
"")
        self.helper.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.helper)

        self.helper_2 = QPushButton(self.verticalLayoutWidget)
        self.helper_2.setObjectName(u"helper_2")
        self.helper_2.setMinimumSize(QSize(520, 72))
        self.helper_2.setMaximumSize(QSize(520, 72))
        self.helper_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.helper_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.IMG_1.setText("")
        self.IMG_2.setText("")
        self.PROGRAMM.setText(QCoreApplication.translate("Form", u"\u041f\u0420\u041e\u0413\u0420\u0410\u041c\u041c\u0410 ", None))
        self.FOR.setText(QCoreApplication.translate("Form", u"\u0414\u041b\u042f \u0424\u041e\u0420\u041c\u0418\u0420\u041e\u0412\u0410\u041d\u0418\u042f", None))
        self.NAG.setText(QCoreApplication.translate("Form", u"\u041d\u0410\u0413\u0420\u0423\u0417\u041a\u0418", None))
        self.creat_nag.setText(QCoreApplication.translate("Form", u"\u0441\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u0430\u0433\u0440\u0443\u0437\u043a\u0443", None))
        self.check_nag.setText(QCoreApplication.translate("Form", u"\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043e\u0442\u0447\u0435\u0442\u0430", None))
        self.change_teach.setText(QCoreApplication.translate("Form", u"\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.helper.setText(QCoreApplication.translate("Form", u"\u0427\u0438\u0442\u0430\u0442\u044c \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044e \u043f\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u043c \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u0435\u043c", None))
        self.helper_2.setText(QCoreApplication.translate("Form", u"\u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
    # retranslateUi

