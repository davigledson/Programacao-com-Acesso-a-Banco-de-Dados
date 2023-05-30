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
item= input("Qual item deseja localizar?")
#executar a consulta

cursor.execute(f'''SELECT * FROM itens WHERE descricao LIKE "%{item}%"; ''')

#ixibir os dados do cursor

for linha in cursor:
    print("Código:  ",linha[0])
    print("descrição:  ",linha[1])
    print('posição:  ', linha[2])
    print('----'*10)

#processa todos os registros do cursor
cursor.fetchall()
#retorna qts de itens afetados no último comando
print(cursor.rowcount,"encontrados.")