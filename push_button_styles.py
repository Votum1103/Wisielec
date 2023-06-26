from PyQt5 import QtCore, QtWidgets


def push_button_style(self, Dialog):
    self.a_pushButton = QtWidgets.QPushButton(Dialog)
    self.aa_pushButton = QtWidgets.QPushButton(Dialog)
    self.b_pushButton = QtWidgets.QPushButton(Dialog)
    self.c_pushButton = QtWidgets.QPushButton(Dialog)
    self.cc_pushButton = QtWidgets.QPushButton(Dialog)
    self.d_pushButton = QtWidgets.QPushButton(Dialog)
    self.e_pushButton = QtWidgets.QPushButton(Dialog)
    self.ee_pushButton = QtWidgets.QPushButton(Dialog)
    self.f_pushButton = QtWidgets.QPushButton(Dialog)
    self.g_pushButton = QtWidgets.QPushButton(Dialog)
    self.h_pushButton = QtWidgets.QPushButton(Dialog)
    self.i_pushButton = QtWidgets.QPushButton(Dialog)
    self.j_pushButton = QtWidgets.QPushButton(Dialog)
    self.k_pushButton = QtWidgets.QPushButton(Dialog)
    self.l_pushButton = QtWidgets.QPushButton(Dialog)
    self.ll_pushButton = QtWidgets.QPushButton(Dialog)
    self.m_pushButton = QtWidgets.QPushButton(Dialog)
    self.n_pushButton = QtWidgets.QPushButton(Dialog)
    self.nn_pushButton = QtWidgets.QPushButton(Dialog)
    self.o_pushButton = QtWidgets.QPushButton(Dialog)
    self.oo_pushButton = QtWidgets.QPushButton(Dialog)
    self.p_pushButton = QtWidgets.QPushButton(Dialog)
    self.q_pushButton = QtWidgets.QPushButton(Dialog)
    self.r_pushButton = QtWidgets.QPushButton(Dialog)
    self.s_pushButton = QtWidgets.QPushButton(Dialog)
    self.ss_pushButton = QtWidgets.QPushButton(Dialog)
    self.t_pushButton = QtWidgets.QPushButton(Dialog)
    self.u_pushButton = QtWidgets.QPushButton(Dialog)
    self.w_pushButton = QtWidgets.QPushButton(Dialog)
    self.x_pushButton = QtWidgets.QPushButton(Dialog)
    self.y_pushButton = QtWidgets.QPushButton(Dialog)
    self.z_pushButton = QtWidgets.QPushButton(Dialog)
    self.zz_pushButton = QtWidgets.QPushButton(Dialog)
    self.zzz_pushButton = QtWidgets.QPushButton(Dialog)
    self.button_names = [[self.a_pushButton, "a", "a"],
                         [self.aa_pushButton, "aa", "ą"],
                         [self.b_pushButton, "b", "b"],
                         [self.c_pushButton, "c", "c"],
                         [self.cc_pushButton, "cc", "ć"],
                         [self.d_pushButton, "d", "d"],
                         [self.e_pushButton, "e", "e"],
                         [self.ee_pushButton, "ee", "ę"],
                         [self.f_pushButton, "f", "f"],
                         [self.g_pushButton, "g", "g"],
                         [self.h_pushButton, "h", "h"],
                         [self.i_pushButton, "i", "i"],
                         [self.j_pushButton, "j", "j"],
                         [self.k_pushButton, "k", "k"],
                         [self.l_pushButton, "l", "l"],
                         [self.ll_pushButton, "ll", "ł"],
                         [self.m_pushButton, "m", "m"],
                         [self.n_pushButton, "n", "n"],
                         [self.nn_pushButton, "nn", "ń"],
                         [self.o_pushButton, "o", "o"],
                         [self.oo_pushButton, "oo", "ó"],
                         [self.p_pushButton, "p", "p"],
                         [self.q_pushButton, "q", "q"],
                         [self.r_pushButton, "r", "r"],
                         [self.s_pushButton, "s", "s"],
                         [self.ss_pushButton, "ss", "ś"],
                         [self.t_pushButton, "t", "t"],
                         [self.u_pushButton, "u", "u"],
                         [self.w_pushButton, "w", "w"],
                         [self.x_pushButton, "x", "x"],
                         [self.y_pushButton, "y", "y"],
                         [self.z_pushButton, "z", "z"],
                         [self.zz_pushButton, "zz", "ż"],
                         [self.zzz_pushButton, "zzz", "ź"]]
    for index, list in enumerate(self.button_names):
        if index < 17:
            list[0].setGeometry(QtCore.QRect(90 + 30 * index, 450, 21, 28))
        elif index >= 17:
            list[0].setGeometry(QtCore.QRect(
                90 + 30 * (index-17), 490, 21, 28))
        list[0].setStyleSheet("QPushButton {\n"
                              "     border-radius: 10px;\n"
                              "     background-color: grey;\n"
                              "     color: white;\n"
                              "     font-size: 16px;\n"
                              "}\n"
                              "\n"
                              "QPushButton:hover {\n"
                              "     background-color: #C0C0C0;\n"
                              "     color: yellow\n"
                              "}\n"
                              "QPushButton:pressed {\n"
                              "     background-color: #A9A9A9;\n"
                              "}")
        list[0].setObjectName(f"{list[1]}_pushButton")
        list[0].clicked.connect(lambda _, l=list[2]: self.addToWord(l))
        list[0].clicked.connect(lambda _, button= list[0]: button.setVisible(False))
