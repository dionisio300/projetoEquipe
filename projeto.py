# Gabriel - Cadastrar
def cadastrar (nome, idade, cidade, listaclientes):
    cliente = {
        'nome': nome,
        'idade': idade,
        'cidade': cidade
    }
    listaclientes.append(cliente)
    
    return listaclientes


    






# Alexya - Listar

def listagem (clientes):
    for dicionario in clientes:
        print (f'Nome:{dicionario['nome']}, Idade: {dicionario['idade']} e Cidade: {dicionario['cidade']}. \n')
        


clientes = [
    {"nome":'Maria', "idade":28,"cidade":'Fortaleza'},
    {"nome":'Ana', "idade":25,"cidade":'Caucaia'},
    {"nome":'João', "idade":28,"cidade":'Euzebio'}
]


#Fazer um menu de opções 1 - cadastrar cliente, 2 - listar os clientes 3 - sair 

listagem(clientes)
cadastrar('Caio',25,'Quixadá',clientes)
listagem(clientes)

# while True - com as opções
