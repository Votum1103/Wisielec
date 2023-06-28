from pickle import FALSE
from PyQt5 import QtCore, QtWidgets, QtGui


def groupbox_guess_word(self, Dialog):
    self.groupBox_guess_word = QtWidgets.QGroupBox(Dialog)
    self.groupBox_guess_word.setGeometry(QtCore.QRect(360, 140, 291, 211))
    font = QtGui.QFont()
    font.setFamily("Helvetica")
    font.setPointSize(24)
    self.groupBox_guess_word.setFont(font)
    self.groupBox_guess_word.setStyleSheet("color: black;")
    self.groupBox_guess_word.setObjectName("groupBox_input_word")
    self.groupBox_guess_word.hide()
    self.label_guess_word = QtWidgets.QLabel(
        self.groupBox_guess_word)
    self.label_guess_word.setGeometry(
        QtCore.QRect(90, 30, 131, 31))
    self.label_guess_word.setObjectName(
        "label_guess_word")
    self.label_guess_word.setAlignment(QtCore.Qt.AlignCenter)
    self.pushButton_guess_word_zatwierdz = QtWidgets.QPushButton(
        self.groupBox_guess_word)
    self.pushButton_guess_word_zatwierdz.setGeometry(
        QtCore.QRect(160, 160, 113, 32))
    self.pushButton_guess_word_zatwierdz.setStyleSheet("QPushButton {\n"
                                                       "    color: #565A5B;\n"
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
    self.pushButton_guess_word_zatwierdz.setObjectName(
        "pushButton_guess_word_zatwierdz")
    self.linedit_guess_word = QtWidgets.QLineEdit(self.groupBox_guess_word)
    self.linedit_guess_word.setGeometry(QtCore.QRect(20, 80, 241, 41))
    self.linedit_guess_word.setObjectName(
        "linedit_guess_word")

    self.label_wrong_word = QtWidgets.QLabel(self.groupBox_guess_word)
    self.label_wrong_word.setGeometry(QtCore.QRect(90, 80, 131, 31))
    self.label_wrong_word.setAlignment(QtCore.Qt.AlignCenter)
    self.label_wrong_word.setObjectName(
        "label_wrong_word")
    self.label_wrong_word.hide()
    self.pushButton_guess_word_zatwierdz.clicked.connect(self.try_to_guess)
    _translate = QtCore.QCoreApplication.translate
    self.label_guess_word.setText(_translate("Dialog", "Wpisz hasło"))
    self.pushButton_guess_word_zatwierdz.setText(
        _translate("Dialog", "Zatwierdź"))
    self.label_wrong_word.setText(_translate("Dialog", "ŹLE"))
    self.timer = QtCore.QTimer(Dialog)
    self.timer.timeout.connect(self.hide_label)
    self.timer.setSingleShot(True)
