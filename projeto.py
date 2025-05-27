# Crie uma função para atualizar o nome - Alexya


# Crie uma função para atualizar a idade - Gabriel
def atualizar_idade (id, idade):
    conexao = conectarBanco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'update clientes set idade= %s where id = %s'
    cursor.execute(sql,(idade, id))
    conexao.commit()
    conexao.close()
    return 'Idade atualizada'





# Crie uma função para atualizar a cidade - Dionizio


# crie uma função para incrementar o total de compras de uma pessoa - Gabriel
def incrementar_compras (id, totalCompras):
    conexao = conectarBanco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'select * from clientes where id = %s'
    cursor.execute(sql,(id,))
    resultados = cursor.fetchone()
    total = resultados["totalCompras"]
    print(total + totalCompras)
    return 'Compra atualizada'


# Calcular a média de compra dos clientes - Alexya


# Gabriel - Cadastrar - Calcular a média das idade
def cadastrar (nome, idade, cidade, totalCompras):
    conexao = conectarBanco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'insert into clientes (nome, idade, cidade, totalCompras) values (%s,%s,%s,%s)'
    cursor.execute(sql,(nome,idade,cidade,totalCompras))
    conexao.commit()
    return 'Dados Cadastrados'



def calcular_media_idade(clientes):
    soma_idades = 0
    total_clientes = 0

    for cliente in clientes:
        soma_idades += cliente["idade"]
        total_clientes += 1

    if total_clientes == 0:
        return 0  

    media = soma_idades / total_clientes
    return media




    






# Alexya - Listar - Criar função para deletar clientes

def listagem (clientes):
    for dicionario in clientes:
        print (f'Nome:{dicionario['nome']}, Idade: {dicionario['idade']} e Cidade: {dicionario['cidade']}. \n')
        


clientes = [
    {"nome":'Maria', "idade":28,"cidade":'Fortaleza'},
    {"nome":'Ana', "idade":25,"cidade":'Caucaia'},
    {"nome":'João', "idade":28,"cidade":'Euzebio'}
]


#Fazer um menu de opções 1 - cadastrar cliente, 2 - listar os clientes 3 - sair 



# Conectar com o banco
import mysql.connector as my
def conectarBanco():
    conexao = my.connect(
        host = '18.228.154.71',
        user = 'gabriel',
        password = '1234',
        database = 'clientes_db'
    )
    print('Conexão bem-sucedida!!')
    return conexao


# while True - com as opções - Dionizio
incrementar_compras(3,100)
while True:
    opcoes = input(f'1- Cadastrar\n 2- Listar Clientes\n 3- Sair\n 4- Media Idades\n')
    if opcoes == '3':
        print('Saindo...')
        break
    if opcoes == '1':
        nome = input('Digite o nome da pessoa: ')
        idade = int(input('Digite a idade da pessoa: '))
        cidade = input('Digite a cidade da pessoa: ')
        totalCompras = float(input('Digite o total de compras: '))

        print(cadastrar(nome,idade,cidade,totalCompras))
        
    if opcoes == '2':
        listagem(clientes)
    if opcoes == '4':
        media_idade = calcular_media_idade(clientes)
        print(f'A media de idade é: {media_idade}')