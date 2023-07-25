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

self.pushButton_login.clicked.connect(self.trocarPaginaLogin)
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


def abrirPaginaCadastrar(self):
    from cadastro import Ui_MainWindow
    # cria uma tela vazia
    self.tela = QtWidgets.QMainWindow()

    # criar um objeto da tela que deseja exibir
    self.cadastro = Ui_MainWindow()

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
        preco = QTableWidgetItem(str(linha[2]))
        marca = QTableWidgetItem(linha[3])

        self.tabela.setItem(cont, 0, codigo)
        self.tabela.setItem(cont, 1, nome)
        self.tabela.setItem(cont, 2, preco)
        self.tabela.setItem(cont, 3, marca)
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













