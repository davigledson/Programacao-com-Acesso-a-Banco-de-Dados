#python -m PyQt6.uic.pyuic -o cadaluno.py -x cadaluno.ui comando para converte arquivo


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox


import mysql.connector
conexao = mysql.connector.connect(
    host='localhost', user='root',
    password='', database='lojaroupa'
)
cursor = conexao.cursor()
print('conectado ao DB')

self.pushButton_sobre.clicked.connect(self.trocarPaginaSobre)
self.pushButton_pesquisa.clicked.connect(self.trocarPaginaPesquisa)
self.pushButton_cadastrar_vestuario.clicked.connect(self.trocarPaginaVestuario)
self.pushButton_login.clicked.connect(self.trocarPaginaLogin)
self.pushButton_cadastrar_usuario.clicked.connect(self.abrirPaginaCadastrar)

self.botao_pesquisar.clicked.connect(self.pesquisar)
self.botao_entrar.clicked.connect(self.login)
self.botao_entrar_vestuario.clicked.connect(self.cadastrarRoupas)


def trocarPaginaPesquisa(self):
    if self.login() == True:
        self.StackedWidget_Paginas.setCurrentWidget(self.page_pesquisa)
    # else:
    # msg = QMessageBox()
    # msg.setWindowTitle('Aviso')
    # msg.setText('Faça login para acessar o sistema')
    # msg.exec()
    # return False
    print('pesquisa')


def trocarPaginaLogin(self):
    if self.login() == True:
        self.StackedWidget_Paginas.setCurrentWidget(self.page_login)

    print('login')


def trocarPaginaSobre(self):
    if self.login() == True:
        self.StackedWidget_Paginas.setCurrentWidget(self.page_sobre)

    print('sobre')


def trocarPaginaVestuario(self):
    if self.login() == True:
        self.StackedWidget_Paginas.setCurrentWidget(self.page_registrar_roupas)

    print('sobre')


def abrirPaginaCadastrar(self):
    if self.login() == True:
        from cadastro import Ui_telaCadastro
        # cria uma tela vazia
        self.tela = QtWidgets.QMainWindow()

        # criar um objeto da tela que deseja exibir
        self.cadastro = Ui_telaCadastro()

        # associar a tela vazia com o código da tela a exibir
        self.cadastro.setupUi(self.tela)

        # exibir a nova tela

        self.tela.show()


def pesquisar(self):
    nome = self.line_nome.text()
    sql = '''SELECT * FROM roupas WHERE NOME LIKE %s'''
    cursor.execute(sql, ("%" + nome + "%",))
    dados = cursor.fetchall()
    print(dados)

    self.tabela.setRowCount(len(dados))
    cont = 0  # contador de linhas
    for linha in dados:
        codigo = QTableWidgetItem(str(linha[0]))
        nome = QTableWidgetItem(linha[1])
        tipoVestimenta = QTableWidgetItem(linha[2])
        quantidade = QTableWidgetItem(str(linha[3]))
        preco = QTableWidgetItem(str(linha[4]))
        detalhes = QTableWidgetItem(linha[5])

        self.tabela.setItem(cont, 0, codigo)
        self.tabela.setItem(cont, 1, nome)
        self.tabela.setItem(cont, 2, tipoVestimenta)
        self.tabela.setItem(cont, 3, quantidade)
        self.tabela.setItem(cont, 4, preco)
        self.tabela.setItem(cont, 5, detalhes)
        cont += 1
    self.tabela.show()


def login(self):
    nome = self.line_usuario.text()
    senha = self.line_senha.text()
    sql = '''SELECT * FROM usuarios WHERE nome = %s AND senha = %s'''
    cursor.execute(sql, (nome, senha))
    dados = cursor.fetchall()
    # print(dados)

    if len(dados) == 0:  # não encontrou
        msg = QMessageBox()
        msg.setWindowTitle('Aviso')
        msg.setText('Acesso negado.')
        msg.exec()
        return False
    else:
        self.StackedWidget_Paginas.setCurrentWidget(self.page_pesquisa)
        self.label_nome_usuario.setText(nome)

        self.pushButton_login.setDisabled(True)
        return True


def cadastrarRoupas(self):
    descricao = self.line_descricao_roupa.text()

    tipoVestimenta = ""
    if self.radioButton_masculino.isChecked():
        tipoVestimenta = "Masculino"
    elif self.radioButton_feminino.isChecked():
        tipoVestimenta = "Feminino"
    elif self.radioButton_unisex.isChecked():
        tipoVestimenta = "Unisex"

    quantidade = self.spinBox_quantidade.text()
    preco = self.doubleSpinBox_preco.text()
    detalhes = self.textEdit_detalhes.toPlainText()

    print(descricao, tipoVestimenta, quantidade, preco, detalhes)









