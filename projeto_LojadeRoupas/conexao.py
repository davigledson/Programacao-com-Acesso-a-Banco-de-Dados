
import mysql.connector
conexao = mysql.connector.connect(
    host='localhost', user='root',
    password='', database='lojaroupa'
)
cursor = conexao.cursor()
print('conectado ao DB')
