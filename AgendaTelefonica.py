# -------------------Tupla -> Iterável, indexada, imutável

# itens = (1)
# print(type(itens))
#
# carrinho = ('Mouse','Fone', 'Teclado','Monitor', 'Monitor', 'Mouse' )
# print(type(carrinho))
# print(carrinho[1])
#
# # niveis = ('Fácil', 'Normal','Difícil')
#
# # carrinho[1] = "Teclado mecanico" #error: imutável
# # print(carrinho)
#
# # #------------------------ Funções
# # #Como obter o índice na tupla?
# index = carrinho.index('Mouse')
# print(index)
#
# # #Como saber quantas vezes o item aparece na tupla?
# count = carrinho.count('Mouse')
# print(count)


# # Cada venda realizada em uma loja, o nome do funcionário era adicionado
# # manualmente em uma tupla em python, ao final do dia a tupla ficou assim
# # vendas = ('Jorge', 'Amanda', 'Miguel', 'Miguel', 'Jorge', 'Miguel', 'Fernado', 'Amanda')
# # Quantas vendas o Miguel realizou?
# # Qual o índice do Fernando?

# vendas = ('Jorge', 'Amanda', 'Miguel', 'Miguel', 'Jorge', 'Miguel', 'Fernando', 'Amanda')
# count = vendas.count('Miguel')
# print(f'Miguel realizou {vendas.count("Miguel")} vendas')  #aspas simples não funciona
# # print(f'Miguel realizou {count} vendas \n')
# # print(vendas.count('Miguel'))
#
# index = vendas.index('Fernando')
# print(f'Fernando realizou a {index}ª venda do dia')


# -------------------Dicionário -> chave:valor
#
# dividas = {
#     "Miguel": 1500,
#     "Lara": 2600,
#     "Jubliscleudo":54156
# }
# print(dividas)
#
# # Acessando o valor de um item
# print(dividas['Miguel'])
#
# dividas['Miguel'] -= 1000
# print(dividas)
#
# # # como adicionar novo item no dicionário
#
# dividas['Leo'] = 300
# print(dividas)
#
# nome = input('digite o nome do cliente: ')
# dividas[nome] = int(input('Digite o valor da dívida: '))
# print(dividas)

# # leia o nome de 3 produtos e adicione-os no dicionário

# mercado ={}
#
# for i in range(3):
#     produto = input('Digite o produto desejado: ')
#     preco = float(input('Digite o valor do produto: '))
#
#     mercado[produto]=preco
#
# print(mercado)

# # Como remover um item do dicionário?
# dividas = {
#     "Miguel": 1500,
#     "Lara": 2600,
#     "Jubliscleudo":54156
# }
# del dividas['Miguel']
# print(dividas)


# # Crie um dicionário com 3 chaves (nome, profissão e idade)

# dicionario = {
#     "nome":"Daniel",
#     "profissao": "Analista de PCP",
#     "idade": 28,
# }

# dividas = {
#     "Miguel": 1500,
#     "Lara": 2600,
#     "Jubliscleudo":54156
# }
# print(dividas)
# #---------- Como percorrer um dicionário?

# for k in dividas:
#     print(dividas[k])
###########################################################
# print(dividas.values())
#
# for valor in dividas.values():
#     print(valor)
###########################################################

# print(dividas.items())
# for item in dividas.items():
#     print(item)
###########################################################

# print(dividas.keys())
# for k in dividas.keys():
#     print(k)


# #-------------------------------------##

# # Agenda telefônica

agenda = {}

while True:
    print('-- Agenda Telefônica --')
    print('1 - Adicionar contato')
    print('2 - Editar telefone')
    print('3 - Remover contato')
    print('4 - Buscar contato')
    print('5 - Listar todos')
    # print('7 - Editar nome') #tentar
    print('9 - Sair' )
    opcao = int(input('Selecione uma das opções: '))

    if opcao == 1:
        nome = input("Digite o nome do Contato: ")
        if nome not in agenda:
            telefone = int(input("Digite o núemro de telefone: "))
            agenda[nome] = telefone
            print(f"{nome} foi adicionado!\n")
            print(agenda)
        else:
            print(f"O contato {nome} já existe!\n")

    #Editar telefone
    elif opcao ==2:
        nome = input('Digite o nome do contato: ')
        if nome in agenda:
            agenda[nome]=int(input(f"Digite o novo telefone de {nome}: "))
            print(f"O contato {nome} foi atualizado com sucesso com o núemro {agenda[nome]}. \n")
        else:
            print(f"O contato {nome} não consta na lista, tente adiciona-lo!\n")

    # Remover contato
    elif opcao ==3:
        nome = input('Digite o nome do contato: ')
        if nome in agenda:
            del agenda[nome]
            print(f"O contato {nome} foi removido com sucesso! \n")
        else:
            print(f"O contato {nome} não consta na lista!\n")

    # Buscar contato
    elif opcao == 4:
        nome = input('Digite o nome do contato: ')
        if nome in agenda:
            print(f"{agenda[nome]} é o número de {nome}\n")
        else:
            print(f"O contato {nome} não consta na lista!\n")

    # Listar todos
    elif opcao == 5:
        for key in agenda:
            print(f'Nome: {key} - Telefone: {agenda[key]}\n')

    elif opcao == 6:
        print('Até breve...')
        break

    else:
        print("Digite uma opção válida!\n")

