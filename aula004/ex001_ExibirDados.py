#estabelecer a conexao

import mysql.connector

conexao = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="deposito"
)
#criar o cursor
cursor = conexao.cursor()
print('ok')
#solicita a digitação do item a localizar

#executar a consulta

cursor.execute("SELECT * FROM itens ")

#ixibir os dados do cursor

for linha in cursor:
    print("Código:  ",linha[0])
    print("descrição:  ",linha[1])
    print('posição:  ', linha[2])
    print('----'*10)