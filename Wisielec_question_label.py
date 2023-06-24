from PyQt5 import QtCore, QtGui, QtWidgets


def question_label(self, Dialog):
    font = QtGui.QFont()
    font.setFamily("Helvetica")
    font.setPointSize(-1)
    self.groupBox_question = QtWidgets.QGroupBox(Dialog)
    self.groupBox_question.setGeometry(QtCore.QRect(340, 130, 301, 181))
    font = QtGui.QFont()
    font.setFamily("Helvetica")
    font.setPointSize(18)
    self.groupBox_question.setFont(font)
    self.groupBox_question.setStyleSheet("color: white;")
    self.groupBox_question.setObjectName("groupBox_instruction")
    self.groupBox_question.setVisible(True)
    self.groupBox_question.raise_()
    self.question_label = QtWidgets.QTextBrowser(self.groupBox_question)
    self.question_label.setGeometry(
        QtCore.QRect(20, 40, 251, 21))
    self.question_label.setObjectName(
        "question_label")
    self.question_label.setParent(self.groupBox_question)
