# Form implementation generated from reading ui file 'sobre2.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Sobre(object):
    def setupUi(self, Sobre):
        Sobre.setObjectName("Sobre")
        Sobre.resize(477, 600)
        Sobre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=Sobre)
        self.centralwidget.setObjectName("centralwidget")
        self.botao_fechar2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.botao_fechar2.setGeometry(QtCore.QRect(150, 530, 75, 23))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(10)
        self.botao_fechar2.setFont(font)
        self.botao_fechar2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(108, 168, 218);")
        self.botao_fechar2.setObjectName("botao_fechar2")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 171, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_mariana = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(10)
        self.label_mariana.setFont(font)
        self.label_mariana.setObjectName("label_mariana")
        self.verticalLayout.addWidget(self.label_mariana)
        self.label_mariana1 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_mariana1.setText("")
        self.label_mariana1.setPixmap(QtGui.QPixmap("imagens/menina (1).png"))
        self.label_mariana1.setObjectName("label_mariana1")
        self.verticalLayout.addWidget(self.label_mariana1)
        self.label_livia = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(10)
        self.label_livia.setFont(font)
        self.label_livia.setObjectName("label_livia")
        self.verticalLayout.addWidget(self.label_livia)
        self.label_livia1 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_livia1.setText("")
        self.label_livia1.setPixmap(QtGui.QPixmap("imagens/mulher (1).png"))
        self.label_livia1.setObjectName("label_livia1")
        self.verticalLayout.addWidget(self.label_livia1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(200, 40, 181, 451))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_sonaly = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(10)
        self.label_sonaly.setFont(font)
        self.label_sonaly.setObjectName("label_sonaly")
        self.verticalLayout_2.addWidget(self.label_sonaly)
        self.label_sonaly1 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_sonaly1.setText("")
        self.label_sonaly1.setPixmap(QtGui.QPixmap("imagens/menina.png"))
        self.label_sonaly1.setObjectName("label_sonaly1")
        self.verticalLayout_2.addWidget(self.label_sonaly1)
        self.label_eduarda = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(10)
        self.label_eduarda.setFont(font)
        self.label_eduarda.setObjectName("label_eduarda")
        self.verticalLayout_2.addWidget(self.label_eduarda)
        self.label_eduarda1 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_eduarda1.setText("")
        self.label_eduarda1.setPixmap(QtGui.QPixmap("imagens/mulher.png"))
        self.label_eduarda1.setObjectName("label_eduarda1")
        self.verticalLayout_2.addWidget(self.label_eduarda1)
        self.label_turma = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_turma.setGeometry(QtCore.QRect(20, 20, 281, 16))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_turma.setFont(font)
        self.label_turma.setObjectName("label_turma")
        Sobre.setCentralWidget(self.centralwidget)

        self.retranslateUi(Sobre)
        QtCore.QMetaObject.connectSlotsByName(Sobre)

        self.botao_fechar2.clicked.connect(self.fecharSobre)

    def retranslateUi(self, Sobre):
        _translate = QtCore.QCoreApplication.translate
        Sobre.setWindowTitle(_translate("Sobre", "Sobre"))
        self.botao_fechar2.setText(_translate("Sobre", "FECHAR"))
        self.label_mariana.setText(_translate("Sobre", "NOME: Mariana Suyane"))
        self.label_livia.setText(_translate("Sobre", "NOME: LÍvia Layane"))
        self.label_sonaly.setText(_translate("Sobre", "NOME:Sonaly Reinaldo"))
        self.label_eduarda.setText(_translate("Sobre", "NOME: Maria Eduarda Andre"))
        self.label_turma.setText(_translate("Sobre", "Turma: Tecnico Subsequente em informática"))

    def fecharSobre(self):

        Sobre.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sobre = QtWidgets.QMainWindow()
    ui = Ui_Sobre()
    ui.setupUi(Sobre)
    Sobre.show()
    sys.exit(app.exec())
