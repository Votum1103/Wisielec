# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wisielec.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from retranslateUI import retranslateUi
from push_button_styles import push_button_style
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(677, 574)
        Dialog.setStyleSheet("background-color: white")
        self.question_label = QtWidgets.QLabel(Dialog)
        self.question_label.setGeometry(QtCore.QRect(370, 180, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.question_label.setFont(font)
        self.question_label.setStyleSheet("QLabel {\n"
"    color: #565A5B;\n"
"    border: 1px solid black;\n"
"    font-size: 14px;\n"
"    border-radius: 10px;\n"
"    background-color: #C5DEEB;\n"
"    padding: 3px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #A5E2FF\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    color: #0B5AE1;\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #D7B5F9\n"
"        );\n"
"    }")
        self.question_label.setScaledContents(False)
        self.question_label.setWordWrap(False)
        self.question_label.setObjectName("question_label")
        self.yes_pushButton = QtWidgets.QPushButton(Dialog)
        self.yes_pushButton.setGeometry(QtCore.QRect(370, 250, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.yes_pushButton.setFont(font)
        self.yes_pushButton.setStyleSheet("QPushButton {\n"
"    color: #565A5B;\n"
"    border: 1px solid black;\n"
"    font-size: 14px;\n"
"    border-radius: 10px;\n"
"    background-color: #C5DEEB;\n"
"    padding: 3px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #A5E2FF\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    color: #0B5AE1;\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #D7B5F9\n"
"        );\n"
"    }background-color:silver;")
        self.yes_pushButton.setObjectName("yes_pushButton")
        self.no_pushButton = QtWidgets.QPushButton(Dialog)
        self.no_pushButton.setGeometry(QtCore.QRect(510, 250, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.no_pushButton.setFont(font)
        self.no_pushButton.setStyleSheet("QPushButton {\n"
"    color: #565A5B;\n"
"    border: 1px solid black;\n"
"    font-size: 14px;\n"
"    border-radius: 10px;\n"
"    background-color: #C5DEEB;\n"
"    padding: 3px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #A5E2FF\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    color: #0B5AE1;\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #D7B5F9\n"
"        );\n"
"    }")
        self.no_pushButton.setObjectName("no_pushButton")
        self.wisielec_label = QtWidgets.QLabel(Dialog)
        self.wisielec_label.setGeometry(QtCore.QRect(70, 20, 551, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.wisielec_label.setFont(font)
        self.wisielec_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wisielec_label.setStyleSheet("background-color:transparent;")
        self.wisielec_label.setObjectName("wisielec_label")
        
        self.szub1_label = QtWidgets.QLabel(Dialog)
        self.szub1_label.setGeometry(QtCore.QRect(0, 70, 381, 500))
        self.szub1_label.setStyleSheet("background-color:transparent;")
        self.szub1_label.setText("")
        self.szub1_label.setPixmap(QtGui.QPixmap("Zdjęcia szubienicy/szub1.png"))
        self.szub1_label.setScaledContents(True)
        self.szub1_label.setObjectName("szub1_label")
        self.szub2_label = QtWidgets.QLabel(Dialog)
        self.szub2_label.setGeometry(QtCore.QRect(0, 70, 381, 500))
        self.szub2_label.setStyleSheet("background-color:transparent;")
        self.szub2_label.setText("")
        self.szub2_label.setPixmap(QtGui.QPixmap("../../../Downloads/szub2.png.png"))
        self.szub2_label.setObjectName("szub2_label")
        self.szub4_label = QtWidgets.QLabel(Dialog)
        self.szub4_label.setGeometry(QtCore.QRect(0, 70, 381, 500))
        self.szub4_label.setStyleSheet("background-color:transparent;")
        self.szub4_label.setText("")
        self.szub4_label.setObjectName("szub4_label")
        self.szub3_label = QtWidgets.QLabel(Dialog)
        self.szub3_label.setGeometry(QtCore.QRect(0, 70, 381, 500))
        self.szub3_label.setStyleSheet("background-color:transparent;")
        self.szub3_label.setText("")
        self.szub3_label.setPixmap(QtGui.QPixmap("../../../Downloads/szub3.png.png"))
        self.szub3_label.setScaledContents(True)
        self.szub3_label.setObjectName("szub3_label")
        self.szub5_label = QtWidgets.QLabel(Dialog)
        self.szub5_label.setGeometry(QtCore.QRect(0, 70, 381, 500))
        self.szub5_label.setStyleSheet("background-color:transparent;")
        self.szub5_label.setText("")
        self.szub5_label.setPixmap(QtGui.QPixmap("../../../Downloads/szub5.png.png"))
        self.szub5_label.setObjectName("szub5_label")
        self.szub6_label = QtWidgets.QLabel(Dialog)
        self.szub6_label.setGeometry(QtCore.QRect(0, 70, 381, 500))
        self.szub6_label.setStyleSheet("background-color:transparent;")
        self.szub6_label.setText("")
        self.szub6_label.setPixmap(QtGui.QPixmap("../../../Downloads/szub6.png.png"))
        self.szub6_label.setScaledContents(True)
        self.szub6_label.setObjectName("szub6_label")
        self.szub7_label = QtWidgets.QLabel(Dialog)
        self.szub7_label.setGeometry(QtCore.QRect(0, 70, 381, 500))
        self.szub7_label.setStyleSheet("background-color:transparent;")
        self.szub7_label.setText("")
        self.szub7_label.setPixmap(QtGui.QPixmap("../../../Downloads/szub7.png.png"))
        self.szub7_label.setObjectName("szub7_label")
        self.szub8_label = QtWidgets.QLabel(Dialog)
        self.szub8_label.setGeometry(QtCore.QRect(0, 70, 381, 500))
        self.szub8_label.setStyleSheet("background-color:transparent;")
        self.szub8_label.setText("")
        self.szub8_label.setPixmap(QtGui.QPixmap("../../../Downloads/szub8.png.png"))
        self.szub8_label.setObjectName("szub8_label")
        self.szub9_label = QtWidgets.QLabel(Dialog)
        self.szub9_label.setGeometry(QtCore.QRect(0, 70, 381, 500))
        self.szub9_label.setStyleSheet("background-color:transparent;")
        self.szub9_label.setText("")
        self.szub9_label.setPixmap(QtGui.QPixmap("../../../Downloads/szub9.png"))
        self.szub9_label.setObjectName("szub9_label")
        self.finalword_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.finalword_lineEdit.setGeometry(QtCore.QRect(370, 250, 231, 31))
        self.finalword_lineEdit.setStyleSheet("QLineEdit {\n"
"    color: black;\n"
"    border: 1px solid black;\n"
"    font-size: 14px;\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    padding: 3px;\n"
"    }")
        self.finalword_lineEdit.setObjectName("finalword_lineEdit")
        self.keyword_label = QtWidgets.QLabel(Dialog)
        self.keyword_label.setGeometry(QtCore.QRect(70, 370, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyword_label.setFont(font)
        self.keyword_label.setStyleSheet("background-color:transparent;")
        self.keyword_label.setText("")
        self.keyword_label.setAlignment(QtCore.Qt.AlignCenter)
        self.keyword_label.setObjectName("keyword_label")
        self.finalword_lineEdit.raise_()
        self.question_label.raise_()
        self.yes_pushButton.raise_()
        self.wisielec_label.raise_()
        self.keyword_label.raise_()
        self.no_pushButton.raise_()

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        push_button_style(self, Dialog)
        retranslateUi(self, Dialog)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
