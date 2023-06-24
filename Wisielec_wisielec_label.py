from PyQt5 import QtCore, QtGui, QtWidgets


def wisielec_label(self, Dialog):
    self.wisielec_label = QtWidgets.QLabel(Dialog)
    self.wisielec_label.setGeometry(QtCore.QRect(70, 20, 551, 61))
    font = QtGui.QFont()
    font.setPointSize(22)
    font.setBold(True)
    font.setWeight(75)
    self.wisielec_label.setFont(font)
    self.wisielec_label.setStyleSheet("background-color:transparent;")
    self.wisielec_label.setObjectName("wisielec_label")
