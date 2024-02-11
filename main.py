from clientes import Cliente, preenche, busca_interpolacao_nomes, menu, escreverArquivo, busca_interpolacao_codigos, lerArquivo, verClientes

lista = lerArquivo()

while (True):
    menu()
    opc = int(input('ESCOLHA UMA OPÇÃO: '))
    print('=-' * 14)
    if opc == 1:
        cliente = preenche(lista)
    elif opc == 2:
        
        nome_busca = input('Digite o nome a ser buscado: ')
        resultado = int(busca_interpolacao_nomes(lista, nome_busca))
        aux_nome = lista.copy()  #Variável auxiliar para a busca por nome. Para não modificar a lista principal.
        if resultado != -1:
            print(f'O nome {nome_busca} foi encontrado na posição {resultado}.')
            print('=-' * 14)
            aux_nome.sort(key=lambda x: x.nome)
            print(f'{aux_nome[resultado]}')
        else:
            print(f'O nome {nome_busca} não foi encontrado na lista.')
    elif opc == 3:

        cod_busca = int(input('Digite o código a ser buscado: '))
        resultado = busca_interpolacao_codigos(lista, cod_busca)
        aux_id = lista.copy()  #Variável auxiliar para a busca por código. Para não modificar a lista principal.
        if resultado != -1:
            print(f'O código {cod_busca} foi encontrado na posição {resultado}')
            print('=-' * 14)
            aux_id.sort(key=lambda x: x.codCliente)
            print(f'{aux_id[resultado]}')
        else:
            print(f'O código {cod_busca} não foi encontrado na lista.')
    elif opc == 4:
        verClientes(lista)
        
    elif opc == 5:
        break
