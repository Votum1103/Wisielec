from PyQt5 import QtCore, QtGui, QtWidgets


def yes_no_pushbutton(self, Dialog):
    self.yes_pushButton = QtWidgets.QPushButton(Dialog)
    self.yes_pushButton.setGeometry(QtCore.QRect(370, 250, 93, 28))
    font = QtGui.QFont()
    font.setPointSize(-1)
    font.setBold(True)
    font.setWeight(75)
    self.yes_pushButton.setFont(font)
    self.yes_pushButton.setStyleSheet("QPushButton {\n"
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
    self.yes_pushButton.setObjectName("yes_pushButton")
    self.no_pushButton = QtWidgets.QPushButton(Dialog)
    self.no_pushButton.setGeometry(QtCore.QRect(510, 250, 93, 28))
    self.no_pushButton.setFont(font)
    self.no_pushButton.setStyleSheet("QPushButton {\n"
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
    self.no_pushButton.setObjectName("no_pushButton")
