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
    button_names = [[self.a_pushButton, "a"],
                    [self.aa_pushButton, "aa"],
                    [self.b_pushButton, "b"],
                    [self.c_pushButton, "c"],
                    [self.cc_pushButton, "cc"],
                    [self.d_pushButton, "d"],
                    [self.e_pushButton, "e"],
                    [self.ee_pushButton, "ee"],
                    [self.f_pushButton, "f"],
                    [self.g_pushButton, "g"],
                    [self.h_pushButton, "h"],
                    [self.i_pushButton, "i"],
                    [self.j_pushButton, "j"],
                    [self.k_pushButton, "k"],
                    [self.l_pushButton, "l"],
                    [self.ll_pushButton, "ll"],
                    [self.m_pushButton, "m"],
                    [self.n_pushButton, "n"],
                    [self.nn_pushButton, "nn"],
                    [self.o_pushButton, "o"],
                    [self.oo_pushButton, "oo"],
                    [self.p_pushButton, "p"],
                    [self.q_pushButton, "q"],
                    [self.r_pushButton, "r"],
                    [self.s_pushButton, "s"],
                    [self.ss_pushButton, "ss"],
                    [self.t_pushButton, "t"],
                    [self.u_pushButton, "u"],
                    [self.w_pushButton, "w"],
                    [self.x_pushButton, "x"],
                    [self.y_pushButton, "y"],
                    [self.z_pushButton, "z"],
                    [self.zz_pushButton, "zz"],
                    [self.zzz_pushButton, "zzz"]]
    for index, list in enumerate(button_names):
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
