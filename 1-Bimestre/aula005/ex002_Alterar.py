#### CONECTAR AO BANCO ##############

import mysql.connector
conexao = mysql.connector.connect(
    host="localhost", user="root",
    password ="", database="lojacarros"
)

cursor = conexao.cursor()
print('ok')
#### LISTAR OS REGISTROS DA TABELA ############
cursor.execute("SELECT * FROM carros")
for linha in cursor:
    print(linha)

#### SOLICITAR A DIGITAÇÃO/CONFIRMAÇÃO############
cod = input("Qual código deseja alterar?")

cursor.execute(
    "SELECT * FROM CARROS WHERE codigo = " + cod
)

### CONVERTE A CONSULTA EM UMA LISTA #############
dados = cursor.fetchall()

if len(dados) == 0:
    print("Código não encontrado")
else:
    print("código:",dados[0][0])
    print("fabricante:", dados[0][1])
    print("modelo:", dados[0][2])
    print("preco:", dados[0][3])
    coluna = input("Qual coluna deseja alterar")

    if coluna in ('codigo','fabricante','modelo','preco'):
        valor = input("Qual o novo valor?")


        cursor.execute(
            f'''UPDATE carros SET {coluna} = '{valor}' 
            WHERE codigo = {cod}
            '''
            )
        conexao.commit()
        print("Alterado com sucesso")
    else:
        print('Coluna Desconhecida')