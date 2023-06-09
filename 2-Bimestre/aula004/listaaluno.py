# Form implementation generated from reading ui file 'listaaluno.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
#python -m PyQt6.uic.pyuic -o cadaluno.py -x cadaluno.ui comando para converte arquivo
import mysql.connector
conexao = mysql.connector.connect(
    host='localhost', user='root',
    password='', database='escola'
)
cursor = conexao.cursor()
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_listaAluno(object):
    def setupUi(self, MainWindow_listaAluno):
        MainWindow_listaAluno.setObjectName("MainWindow_listaAluno")
        MainWindow_listaAluno.resize(560, 380)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_listaAluno)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_listar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_listar.setObjectName("pushButton_listar")
        self.pushButton_listar.clicked.connect(self.listar)
        self.verticalLayout.addWidget(self.pushButton_listar)
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow_listaAluno.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_listaAluno)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_listaAluno)

    def retranslateUi(self, MainWindow_listaAluno):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_listaAluno.setWindowTitle(_translate("MainWindow_listaAluno", "Listagem de Alunos"))
        self.pushButton_listar.setText(_translate("MainWindow_listaAluno", "Listar"))

    def listar(self):
        sql = 'SELECT * FROM aluno'
        cursor.execute(sql)
        dados = cursor.fetchall()

        #print(dados)
        texto = ''
        for linha in dados:
            texto+=" Código:" +str( linha[0]) + '\n'
            texto += " Nome:" + linha[1] + '\n'
            texto += " Turma:" + linha[2] + '\n'
            texto += " Atleta:" + linha[3] + '\n'
            texto += " Bolsista:" + linha[4] + '\n'
            texto += " Obs:" + linha[5] + '\n'
            texto+= "="*20 + '\n'
            self.textEdit.setPlainText(texto)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_listaAluno = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_listaAluno()
    ui.setupUi(MainWindow_listaAluno)
    MainWindow_listaAluno.show()
    sys.exit(app.exec())
