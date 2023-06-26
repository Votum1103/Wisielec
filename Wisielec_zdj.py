from PyQt5 import QtCore, QtGui, QtWidgets


def zdj(self, Dialog):
    self.szub1_label = QtWidgets.QLabel(Dialog)
    self.szub2_label = QtWidgets.QLabel(Dialog)
    self.szub3_label = QtWidgets.QLabel(Dialog)
    self.szub4_label = QtWidgets.QLabel(Dialog)
    self.szub5_label = QtWidgets.QLabel(Dialog)
    self.szub6_label = QtWidgets.QLabel(Dialog)
    self.szub7_label = QtWidgets.QLabel(Dialog)
    self.szub8_label = QtWidgets.QLabel(Dialog)
    self.szub9_label = QtWidgets.QLabel(Dialog)
    zdj_names = [[self.szub1_label, "Zdjęcia szubienicy/szub1.png"],
                 [self.szub2_label, "Zdjęcia szubienicy/szub2.png"],
                 [self.szub3_label, "Zdjęcia szubienicy/szub3.png"],
                 [self.szub4_label, "Zdjęcia szubienicy/szub4.png"],
                 [self.szub5_label, "Zdjęcia szubienicy/szub5.png"],
                 [self.szub6_label, "Zdjęcia szubienicy/szub6.png"],
                 [self.szub7_label, "Zdjęcia szubienicy/szub7.png"],
                 [self.szub8_label, "Zdjęcia szubienicy/szub8.png"],
                 [self.szub9_label, "Zdjęcia szubienicy/szub9.png"]]
    for list in zdj_names:
        list[0].setGeometry(QtCore.QRect(30, 110, 241, 261))
        list[0].setStyleSheet("background-color:transparent;")
        list[0].setPixmap(QtGui.QPixmap(list[1]))
        list[0].setVisible(False)
