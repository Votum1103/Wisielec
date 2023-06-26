from PyQt5 import QtWidgets
from Single import Ui_Dialog_single
from apka_1 import Ui_dialog_game
from Wisielec import Ui_Dialog_multi
from Single import Ui_Dialog_single


class FirstWindow(QtWidgets.QDialog, Ui_dialog_game):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_singleplayer.clicked.connect(
            self.openThirdWindowFromSingle)
        self.pushButton_multiplayer.clicked.connect(
            self.openSecondWindowFromMulti)

    def openThirdWindowFromSingle(self):
        self.hide()
        self.singleWindow = ThirdWindow()
        self.singleWindow.show()

    def openSecondWindowFromMulti(self):
        self.hide()
        self.multiWindow = SecondWindow()
        self.multiWindow.show()


class SecondWindow(QtWidgets.QDialog, Ui_Dialog_multi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ThirdWindow(QtWidgets.QDialog, Ui_Dialog_single):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    firstWindow = FirstWindow()
    firstWindow.show()
    sys.exit(app.exec_())
