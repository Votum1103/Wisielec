from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from retranslateUI import retranslateUi
from push_button_styles import push_button_style
from Wisielec_question_pushbutton import question_pushButton
from Wisielec_wisielec_label import wisielec_label
from Wisielec_keyword_label import keyword_label
from Wisielec_groupbox_input_word import groupbox_input_word
from Wisielec_groupbox_guess_word import groupbox_guess_word
from Wisielec_zdj import zdj
from Wisielec_Music import play_music_in_game
from Single_text import single_text


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
        single_text(self, Dialog)
        groupbox_guess_word(self, Dialog)
        self.photo_index = 0
        play_music_in_game(self, Dialog)

    def hide_input_groupbox(self):
        self.groupBox_input_word.setVisible(False)

    def assignVariable(self):
        self.given_word = self.linedit_given_word.text()
        self.word = "_ " * len(self.given_word)
        for index, char in enumerate(self.given_word):
            if char == " ":
                index_space = index * 2
                self.word = self.word[:index_space] + \
                    " " + self.word[index_space + 1:]
            elif char == "-":
                index_space = index * 2
                self.word = self.word[:index_space] + \
                    "-" + self.word[index_space + 1:]
        self.keyword_label.setText(self.word)

    def addToWord(self, letter):
        for index, char in enumerate(self.given_word):
            if char == letter.lower() or char == letter.capitalize():
                index_space = index * 2
                self.word = self.word[:index_space] + \
                    letter.capitalize() + self.word[index_space + 1:]
                self.keyword_label.setText(self.word)

    def show_groupbox(self):
        self.groupBox_guess_word.show()

    def try_to_guess(self):
        self.guess_word = self.linedit_guess_word.text()
        if self.given_word.upper() == self.guess_word.upper():
            self.keyword_label.setText(self.guess_word.upper())
            self.groupBox_guess_word.hide()
        else:
            self.timer.start(800)
            self.linedit_guess_word.hide()
            self.label_wrong_word.show()

    def hide_label(self):
        self.label_wrong_word.hide()
        self.linedit_guess_word.show()
        self.groupBox_guess_word.hide()

    def show_wisielec(self, letter):
        photos = [self.szub1_label,
                  self.szub2_label,
                  self.szub3_label,
                  self.szub4_label,
                  self.szub5_label,
                  self.szub6_label,
                  self.szub7_label,
                  self.szub8_label,
                  self.szub9_label]

        if self.photo_index == 0 and letter.lower() not in self.given_word:
            photos[self.photo_index].setVisible(True)
            self.photo_index += 1
        elif letter.lower() not in self.given_word:
            photos[self.photo_index-1].setVisible(False)
            photos[self.photo_index].setVisible(True)
            self.photo_index += 1

    def play_music_after_getting_letter(self):
        self.player1 = QMediaPlayer()
        url = QUrl.fromLocalFile("When_you_get_letter.wav")
        content = QMediaContent(url)
        self.player1.setMedia(content)
        self.player1.setVolume(30)
        self.player1.play()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_multi()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
