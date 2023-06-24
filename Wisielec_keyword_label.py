from PyQt5 import QtCore, QtGui, QtWidgets


def keyword_label(self, Dialog):
    self.keyword_label = QtWidgets.QLabel(Dialog)
    self.keyword_label.setGeometry(QtCore.QRect(70, 370, 551, 41))
    font = QtGui.QFont()
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    self.keyword_label.setFont(font)
    self.keyword_label.setStyleSheet("background-color:transparent;")
    self.keyword_label.setAlignment(QtCore.Qt.AlignCenter)
    self.keyword_label.setObjectName("keyword_label")
