# Gabriel - Cadastrar
def cadastrar (nome, idade, cidade, listaclientes):
    cliente = {
        'nome': nome,
        'idade': idade,
        'cidade': cidade
    }
    listaclientes.push(cliente)
    return listaclientes
    






# Alexya - Listar

def listagem (clientes):
    for dicionario in clientes:
        print (f'Nome:{clientes['nome']}, Idade: {clientes['idade']} e Cidade: {clientes['cidade']}. \n')
        


clientes = [
    {"nome":'Maria', "idade":28,"cidade":'Fortaleza'},
    {"nome":'Ana', "idade":25,"cidade":'Caucaia'},
    {"nome":'João', "idade":28,"cidade":'Euzebio'}
]

#Fazer um menu de opções 1 - cadastrar cliente, 2 - listar os clientes 3 - sair 


# while True - com as opções
