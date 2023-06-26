from PyQt5 import QtCore, QtWidgets, QtGui
from retranslateUI import retranslateUi
from push_button_styles import push_button_style
from Wisielec_question_pushbutton import question_pushButton
from Wisielec_wisielec_label import wisielec_label
from Wisielec_keyword_label import keyword_label
from Wisielec_groupbox_input_word import groupbox_input_word
from Wisielec_groupbox_guess_word import groupbox_guess_word
from Wisielec_zdj import zdj


class Ui_Dialog_multi(object):
    def setupUi(self, Dialog):
        self.multi = True
        Dialog.setObjectName("Dialog")
        Dialog.resize(677, 574)
        Dialog.setStyleSheet("background-color: white")
        question_pushButton(self, Dialog)
        wisielec_label(self, Dialog)
        keyword_label(self, Dialog)
        zdj(self, Dialog)
        push_button_style(self, Dialog)
        groupbox_input_word(self, Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        retranslateUi(self, Dialog)

    def hide_input_groupbox(self):
        self.groupBox_input_word.setVisible(False)

    def assignVariable(self):
        self.given_word = self.linedit_given_word.text()
        self.word = "_ " * len(self.given_word)
        self.keyword_label.setText(self.word)

    def addToWord(self, letter):
        for index, char in enumerate(self.given_word):
            if char == letter.lower() or char == letter.capitalize():
                index_space = index * 2
                self.word = self.word[:index_space] + \
                    letter.capitalize() + self.word[index_space + 1:]
                self.keyword_label.setText(self.word)

    def show_groupbox(self):
        groupbox_guess_word(self, Dialog)

    def try_to_guess(self):
        self.guess_word = self.linedit_guess_word.text()
        if self.given_word.upper() == self.guess_word.upper():
            self.keyword_label.setText(self.guess_word.upper())
            self.groupBox_guess_word.setVisible(False)
        else:
            self.groupBox_guess_word.setVisible(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_multi()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
