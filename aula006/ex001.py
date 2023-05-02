############ CONECTAR AO BANCO DE DADOS  #################

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost', user  ='root',
    password='', database = 'livraria'
)

cursor = conexao.cursor()
#print('ok')

## FUNCAO CADASTRO ####

def cadastro():
    print('=== CADASTRO DE LIVRO ===')
    titulo = input('titulo do livro:')
    autor = input("autor do livro:")
    preco = input("Preço do livro:")
    cmd = "INSERT INTO livros VALUES (null, %s, %s,%s)"
    cursor.execute(cmd,(titulo,autor,preco))
    conexao.commit()
    print("inserido com sucesso!")
def listar():
    print('=== LISTAGEM DE LIVROS ===')
    cursor.execute('SELECT * FROM livros')
    for linha in cursor:
        print("Código:", linha[0])
        print("Título:", linha[1])
        print("Autor:", linha[2])
        print("Preço:", linha[3])


######  MENU PRINCIPAL  ##########

while True:
    print(" ==== MENU DO SISTEMA ====")
    print('1. Cadastrar')
    print('2. Listar')
    print('5. Sair')

    opcao = input("opção:")

    if opcao == "1":
       cadastro()

    if opcao == "2":
       listar()

    elif opcao == '5':
        print('Até a próxima!')
        break
