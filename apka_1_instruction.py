from PyQt5 import QtCore, QtGui, QtWidgets


def connected_with_instruction(self, dialog_game):
    self.pushButton_instruction = QtWidgets.QPushButton(dialog_game)
    self.pushButton_instruction.setGeometry(
        QtCore.QRect(480, 500, 151, 41))
    font = QtGui.QFont()
    font.setFamily("Helvetica")
    font.setPointSize(-1)
    self.pushButton_instruction.setFont(font)
    self.pushButton_instruction.setStyleSheet("QPushButton {\n"
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
    self.pushButton_instruction.setObjectName("pushButton_instruction")
    self.groupBox_instruction = QtWidgets.QGroupBox(dialog_game)
    self.groupBox_instruction.setGeometry(QtCore.QRect(20, 190, 611, 371))
    font = QtGui.QFont()
    font.setFamily("Helvetica")
    font.setPointSize(18)
    self.groupBox_instruction.setFont(font)
    self.groupBox_instruction.setStyleSheet("color: white;")
    self.groupBox_instruction.setObjectName("groupBox_instruction")
    self.groupBox_instruction.setVisible(False)
    self.textBrowser_instruction_text = QtWidgets.QTextBrowser(
        self.groupBox_instruction)
    self.textBrowser_instruction_text.setGeometry(
        QtCore.QRect(20, 50, 581, 211))
    self.textBrowser_instruction_text.setObjectName(
        "textBrowser_instruction_text")
    self.pushButton_instruction_wroc = QtWidgets.QPushButton(
        self.groupBox_instruction)
    self.pushButton_instruction_wroc.setGeometry(
        QtCore.QRect(460, 310, 151, 41))
    self.pushButton_instruction_wroc.setStyleSheet("QPushButton {\n"
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
    self.pushButton_instruction_wroc.setObjectName(
        "pushButton_instruction_wroc")
    self.pushButton_instruction.clicked.connect(self.print_instruction)
    self.pushButton_instruction_wroc.clicked.connect(self.hide_instruction)
