# Conectar com o banco
import mysql.connector as my
def conectarBanco():
    conexao = my.connect(
        host = 'database-1.czqmw2yyk7x8.sa-east-1.rds.amazonaws.com',
        user = 'admin',
        password = '281220Le#',
        database = 'testeaws'
    )
    print('Conexão bem-sucedida!!')
    return conexao

conectarBanco()

def cadastrarTeste(nome,email):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    sql = f"insert into teste (nome, email) values ('{nome}','{email}')"
    cursor.execute(sql)
    conexao.commit()
    conexao.close()
    return 'Usuário cadastrado'

print(cadastrarTeste('Dionizio','dionisioassis80@gmail.com'))
