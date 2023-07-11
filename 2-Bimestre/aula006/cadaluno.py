# Form implementation generated from reading ui file 'cadaluno.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import mysql.connector
conexao = mysql.connector.connect(
    host='localhost', user='root',
    password='', database='escola'
)
cursor = conexao.cursor()
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import  QMessageBox







class Ui_CadAluno(object):
    def setupUi(self, CadAluno):
        CadAluno.setObjectName("CadAluno")
        CadAluno.resize(595, 600)
        self.centralwidget = QtWidgets.QWidget(parent=CadAluno)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label_nome = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_nome)
        self.lineEdit_nome = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_nome)
        self.label_curso = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_curso.setObjectName("label_curso")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_curso)
        self.comboBox_curso = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_curso.setObjectName("comboBox_curso")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox_curso)
        self.label_turno = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_turno.setObjectName("label_turno")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_turno)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_manha = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_manha.setChecked(True)
        self.radioButton_manha.setObjectName("radioButton_manha")
        self.horizontalLayout.addWidget(self.radioButton_manha)
        self.radioButton_tarde = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_tarde.setObjectName("radioButton_tarde")
        self.horizontalLayout.addWidget(self.radioButton_tarde)
        self.radioButton_noite = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_noite.setObjectName("radioButton_noite")
        self.horizontalLayout.addWidget(self.radioButton_noite)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout)
        self.label_extra = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_extra.setObjectName("label_extra")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_extra)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_atleta = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_atleta.setObjectName("checkBox_atleta")
        self.horizontalLayout_2.addWidget(self.checkBox_atleta)
        self.checkBox_bolsista = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_bolsista.setObjectName("checkBox_bolsista")
        self.horizontalLayout_2.addWidget(self.checkBox_bolsista)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)
        self.textEdit_obs = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_obs.setObjectName("textEdit_obs")
        self.textEdit_obs.setTabChangesFocus(True)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_obs)
        self.label_obs = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_obs.setObjectName("label_obs")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_obs)
        self.pushButton_salva = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_salva.setObjectName("pushButton_salva")

        self.pushButton_salva.clicked.connect(self.salvar)

        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pushButton_salva)
        CadAluno.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=CadAluno)
        self.statusbar.setObjectName("statusbar")
        CadAluno.setStatusBar(self.statusbar)

        self.retranslateUi(CadAluno)
        QtCore.QMetaObject.connectSlotsByName(CadAluno)

    def retranslateUi(self, CadAluno):
        _translate = QtCore.QCoreApplication.translate
        CadAluno.setWindowTitle(_translate("CadAluno", "Cadastro de Aluno"))
        self.label_nome.setText(_translate("CadAluno", "Nome:"))
        self.label_curso.setText(_translate("CadAluno", "Curso:"))
        self.comboBox_curso.setItemText(0, _translate("CadAluno", "Informatica"))
        self.comboBox_curso.setItemText(1, _translate("CadAluno", "edificaçoes"))
        self.comboBox_curso.setItemText(2, _translate("CadAluno", "eletrica"))
        self.comboBox_curso.setItemText(3, _translate("CadAluno", "mecanica"))
        self.label_turno.setText(_translate("CadAluno", "turno:"))
        self.radioButton_manha.setText(_translate("CadAluno", "Manhã"))
        self.radioButton_tarde.setText(_translate("CadAluno", "Tarde"))
        self.radioButton_noite.setText(_translate("CadAluno", "Noite"))
        self.label_extra.setText(_translate("CadAluno", "Extra:"))
        self.checkBox_atleta.setText(_translate("CadAluno", "Atleta"))
        self.checkBox_bolsista.setText(_translate("CadAluno", "Bolsista"))
        self.label_obs.setText(_translate("CadAluno", "Obs.:"))
        self.pushButton_salva.setText(_translate("CadAluno", "Salvar"))

    def salvar(self):
        nome = self.lineEdit_nome.text()
        curso= self.comboBox_curso.currentText()
        turno = ""
        if self.radioButton_manha.isChecked():
            turno ="Manhã"
        elif self.radioButton_tarde.isChecked():
            turno ="Tarde"
        elif self.radioButton_noite.isChecked():
            turno ="Noite"

        atleta = 'Não'
        if self.checkBox_atleta.isChecked():
            atleta = 'Sim'

        bolsista = 'não'
        if self.checkBox_bolsista.isChecked():
            bolsista = 'sim'

        obs = self.textEdit_obs.toPlainText()
        print(nome,curso,turno,atleta,bolsista,obs)

        sql = "INSERT INTO ALUNO VALUES(null,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (nome,curso,turno,atleta,bolsista,obs))
        conexao.commit()
        #print('INSERIDO COM SUCESSO')

        msg = QMessageBox()
        msg.setWindowTitle('AVISO')
        msg.setText('inserido com sucesso')
        msg.exec()

        #limpar os campos
        self.lineEdit_nome.setText('')
        self.comboBox_curso.setCurrentIndex(0)
        self.radioButton_manha.setChecked(True)
        self.radioButton_noite.setChecked(False) #opcional
        self.radioButton_tarde.setChecked(False) #opcional
        self.checkBox_atleta.setChecked(False)
        self.checkBox_bolsista.setChecked(False)
        self.textEdit_obs.setPlainText("")

        self.lineEdit_nome.setFocus() #faz com o que o campo já esteja pronto para digitar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CadAluno = QtWidgets.QMainWindow()
    ui = Ui_CadAluno()
    ui.setupUi(CadAluno)
    CadAluno.show()
    sys.exit(app.exec())

#python -m PyQt6.uic.pyuic -o cadaluno.py -x cadaluno.ui comando para converte arquivo