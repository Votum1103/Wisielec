from PyQt5 import QtWidgets
from apka_1 import Ui_dialog_game
from Wisielec import Ui_Dialog


class FirstWindow(QtWidgets.QDialog, Ui_dialog_game):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_singleplayer.clicked.connect(
            self.openSecondWindowFromSingle)
        self.pushButton_multiplayer.clicked.connect(
            self.openSecondWindowFromMulti)

    def openSecondWindowFromSingle(self):
        self.hide()
        self.secondWindow = SecondWindow()
        self.secondWindow.show()

    def openSecondWindowFromMulti(self):
        self.hide()
        self.secondWindow = SecondWindow()
        self.secondWindow.show()


class SecondWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    firstWindow = FirstWindow()
    firstWindow.show()
    sys.exit(app.exec_())
