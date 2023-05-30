import mysql.connector

conexao = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="deposito"
)
# criar o cursor
cursor = conexao.cursor()
print('ok')

while True:
    # solicita a digitação do item a localizar
    resp = input("deseja cadastrar?:")
    if resp == "n":
        break
    descricao = input('descrição:')
    posicao = input('posição :')

    # executar a consulta
    cursor.execute(f'''INSERT INTO itens VALUES(null, "{descricao}", "{posicao}"); ''')

    # ixibir os dados do cursor


    print("Inserido com sucesso")



