import mysql.connector
print('drive ok')
conexao = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="estante",
)
print('conexao ok')
cursor = conexao.cursor()
titulo = input("Qual o título do livro?")
autor = input("Quem é o autor do livro?")
cursor.execute(
   #" INSERT INTO livros VALUES(null,%s,%s)",

#f" INSERT INTO livros VALUES(null,'{titulo}','{autor}')",

f''' INSERT INTO livros VALUES(null,'{titulo}','{autor}')'''

)
conexao.commit()
print('inserido com sucesso')

#encerrar a conexao com o servidor
cursor.close()
conexao.close()
print('Conexao encerrada.')
