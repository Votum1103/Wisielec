from PyQt5 import QtCore


def retranslateUi(self, dialog_game):
    _translate = QtCore.QCoreApplication.translate
    dialog_game.setWindowTitle(_translate("dialog_game", "Dialog"))
    self.pushButton_singleplayer.setText(
        _translate("dialog_game", "SINGLEPLAYER"))
    self.pushButton_multiplayer.setText(
        _translate("dialog_game", "MULTIPLAYER"))
    self.pushButton_instruction.setText(
        _translate("dialog_game", "INSTRUKCJA"))
    self.Wisielec_napis.setText(_translate("dialog_game", "WISIELEC"))
    self.groupBox_instruction.setTitle(
        _translate("dialog_game", "Instrukcja"))
    self.textBrowser_instruction_text.setHtml(_translate("dialog_game", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">1.  W grze multiplayer gracz pierwszy podaje słowo i oprzekazuje urządzenie graczowi drugiemu,  który zgaduje słowo wpisane przez gracza pierwszego. </span></p>\n"
                                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">2.  W grze singleplayer gracz zgaduje wymyślone przez komputer słowo. </span></p>\n"
                                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">3.  Niedopuszczalne jest definiowanie słów z myślnikami czy znakami białymi.   </span></p>\n"
                                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">4.  Słowa zgadujemy,  wpisując po jednej literze alfabetu polskiego. </span></p>\n"
                                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">5.  Jeśli domyślasz się,  jakie będzie słowo zanim zgadniesz wszystkie litery, możesz podjąć próbę odgadnięcia go,  wciskając przycisk &quot;tak&quot; w polu &quot;Czy chcesz odgadnąć hasło&quot;,  a następnie wpisując słowo.  W razie nieudanej próby zostanie odjęte 5 pkt. </span></p></body></html>"))
    self.pushButton_instruction_wroc.setText(
        _translate("dialog_game", "WRÓĆ"))
