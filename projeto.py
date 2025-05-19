# Gabriel - Cadastrar - Calcular a média das idade
def cadastrar (nome, idade, cidade, listaclientes):
    cliente = {
        'nome': nome,
        'idade': idade,
        'cidade': cidade
    }
    listaclientes.append(cliente)
    
    return listaclientes



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

listagem(clientes)
cadastrar('Caio',25,'Quixadá',clientes)
listagem(clientes)
calcular_media_idade(clientes)




# while True - com as opções









