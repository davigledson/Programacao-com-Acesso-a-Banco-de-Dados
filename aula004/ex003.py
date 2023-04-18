import mysql.connector

conexao = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="deposito"
)
# criar o cursor
cursor = conexao.cursor()
print('ok')
# solicita a digitação do item a localizar
item = input("Qual item deseja localizar?")
# executar a consulta

cursor.execute(f'''SELECT * FROM itens WHERE descricao LIKE "%{item}%"; ''')

# ixibir os dados do cursor
dados = cursor.fetchall()

for linha in dados:
    print("Código:  ", linha[0])
    print("descrição:  ", linha[1])
    print('posição:  ', linha[2])
    print('----' * 10)

# processa todos os registros do cursor

# retorna qts de itens afetados no último comando
print(len(dados), "itens encontrados.")

#fecha a conexao
cursor.close()
conexao.close()