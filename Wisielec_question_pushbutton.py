from PyQt5 import QtCore, QtGui, QtWidgets


def question_pushButton(self, Dialog):
    self.question_pushButton = QtWidgets.QPushButton(Dialog)
    self.question_pushButton.setGeometry(QtCore.QRect(380, 240, 231, 41))
    font = QtGui.QFont()
    font.setPointSize(-1)
    font.setBold(True)
    font.setWeight(75)
    self.question_pushButton.setFont(font)
    self.question_pushButton.setStyleSheet("QPushButton {\n"
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
                                           "    }background-color:silver;")
    self.question_pushButton.setObjectName("question_pushButton")
    self.question_pushButton.clicked.connect(self.show_groupbox)
