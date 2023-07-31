#Inicia das variaveis Globais
lista_colaborador = [] # Lista vazia para armazenar os colaboradores
codigo_colaborador = 0 # Variável para atribuir códigos únicos aos colaboradores
#Fim das variaveis Globais

# Função para cadastrar um novo colaborador
def cadastrar_colaborador(id):
    print('----------------------------------Menu Cadastrar Colaborador---------------------------')
    print('\nEscolha a opcao desejada: \n')
    print('Codigo do Colaborador: {}'.format(id))
    nome = input('Digite seu nome: ')
    setor = input('Digite seu Setor: ')
    valor = float(input(('Digite seu pagamento R$: ')))
    print('')
    dicionario_colaborador = {  'Codigo' : id,
                                'Nome'   : nome,
                                'Setor'  : setor,
                                'Salario'  : valor,}
    lista_colaborador.append(dicionario_colaborador.copy())

# Função para consultar os colaboradores
def Consultar_colaborador():
    print('-----------------------------------Menu Consultar Colaborador---------------------------')
    while True:
        print('\nEscolha a opcao desejada: \n')
        print('1 - Consultar Todos os Colaborador')
        print('2 - Consultar Colaborador por ID')
        print('3 - Consultar Colaborador(es) por setor')
        print('4 - retornar')
        opcao_consultar = input('>>')

        if opcao_consultar == '1':
            print('Voce escolheu a opcao Consultador todos os Colaboradores')
            for nome in lista_colaborador: # Nome vai varrer toda a lista de Colaboradores
                print('---------------------------------')
                for key,value in nome.items(): # Varrer todos os conjuntos chaves e valor do dicionario Colaborador
                    print('{}: {}'.format(key, value))
                print('---------------------------------')
        elif opcao_consultar == '2':
            print('Voce escolheu a opcao Consultador Colaborador por ID')
            ID_desejado = int((input('Digite o ID do colaborador: ')))
            for nome in lista_colaborador:
              if nome ['Codigo'] == ID_desejado: # Verifica se o código do colaborador é igual ao ID digitado
                print('---------------------------------')
                for key,value in nome.items(): # Varrer todos os conjuntos chaves e valor do dicionario Colaborador
                    print('{}: {}'.format(key, value))
                print('---------------------------------')


        elif opcao_consultar == '3':
            print('Voce escolheu a opcao Consultador todos os Colaboradores por setor')
            nome_setor = (input('Digite o setor desejado: '))
            for nome in lista_colaborador:
              if nome ['Setor'] == nome_setor: # # Verifica se o setor do colaborador é igual ao setor digitado
                print('---------------------------------')
                for key,value in nome.items(): # Varrer todos os conjuntos chaves e valor do dicionario Colaborador
                    print('{}: {}'.format(key, value))
                print('---------------------------------')

        elif opcao_consultar == '4':
            return # Sai da funcao opcao_consultar e volta para o Main        
        else:
            print('Opcao invalidade. Tente Novamente')
            continue # Volta para o inicio do while

# Função para remover um colaborador
def Remover_colaborador():
        print('Bem-vindo ao menu Remover Colaborador')
        valor_desejado = int((input('Digite o ID do colaborador a ser removido: ')))
        for nome in lista_colaborador:
            if nome ['Codigo'] == valor_desejado: # Verifica se o código do colaborador é igual ao ID digitado
                lista_colaborador.remove(nome) # Verifica se o código do colaborador é igual ao ID digitado
                print('Colaborador Removido')
            


# Inicio Main
print('--------------Bem-Vindo ao Controle de Colaboradores do Luccas Duarte Mendanha-----------')
while True:
    
    print('-------------------------------------Menu Principal--------------------------------------')
    print('\nEscolha a opcao desejada: \n')
    print('1 - Cadastrar Colaborador')
    print('2 - Consultar Colaborador(es)')
    print('3 - Remover Colaborador')
    print('4 - Sair\n')
    opcao = input('>>')

    if opcao == '1':
        codigo_colaborador += 1 # Incrementa o código do colaborador
        cadastrar_colaborador(codigo_colaborador) # Chama a função para cadastrar um novo colaborador
    elif opcao == '2':
        Consultar_colaborador()  # Chama a função para consultar colaboradores
    elif opcao == '3':
        Remover_colaborador() # Chama a função para remover um colaborador
    elif opcao == '4':
        break # Encerra o while principal e o programa
    else:
        print('Opcao invalidade. Tente Novamente')
        continue # Volta para o inicio do while