from PyQt5 import QtCore, QtWidgets
from Single_text import single_text
from push_button_styles import push_button_style
from Wisielec_question_label import question_pushButton
from Wisielec_yes_no_pushbutton import yes_no_pushbutton
from Wisielec_wisielec_label import wisielec_label
from Wisielec_keyword_label import keyword_label
from Wisielec_zdj import zdj
import random


class Ui_Dialog_single(object):
    def setupUi(self, Dialog_single):
        self.multi = False
        Dialog_single.setObjectName("Dialog")
        Dialog_single.resize(677, 574)
        Dialog_single.setStyleSheet("background-color: white")
        question_pushButton(self, Dialog_single)
        wisielec_label(self, Dialog_single)
        keyword_label(self, Dialog_single)
        zdj(self, Dialog_single)
        push_button_style(self, Dialog_single)
        QtCore.QMetaObject.connectSlotsByName(Dialog_single)
        single_text(self, Dialog_single)

    def assignVariableSingle(self):
        plik = "dane.txt"
        plik = open(plik, "r", encoding='utf8')
        words_from_file = plik.read().split(",")
        self.given_word = "".join(random.sample(
            words_from_file, 1)).strip().lower()
        self.word = "_ " * len(self.given_word)
        self.keyword_label.setText(self.word)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_single = QtWidgets.QDialog()
    ui = Ui_Dialog_single()
    ui.setupUi(Dialog_single)
    Dialog_single.show()
    ui.assignVariableSingle()
    sys.exit(app.exec_())
