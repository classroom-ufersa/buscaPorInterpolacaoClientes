from clientes import Cliente, preenche, busca_interpolacao_nomes, menu, busca_interpolacao_codigos, lerArquivo, verClientes, int_input, str_input
import os
lista = lerArquivo()

while (True):
    menu()
    opc = int_input('\033[36m ESCOLHA UMA OPÇÃO: \033[m\033[35m')
    print('\033[m=-' * 14)
    os.system('cls')
    
    if opc == 1:
        cliente = preenche(lista)
    elif opc == 2:  
        nome_busca = str_input('Digite o nome a ser buscado: ')
        resultado = int(busca_interpolacao_nomes(lista, nome_busca, True))
        if resultado != -1:
            print(f'O nome do cliente {nome_busca} foi encontrado na lista.')
            print('=-' * 30)
            lista.sort(key=lambda x: x.nome) # Ordena a lista de clientes pelo nome
            print(lista[resultado])
        else:
            print(f'O nome do cliente {nome_busca} não foi encontrado na lista.')
    
    elif opc == 3:
        cod_busca = int(int_input('Digite o código a ser buscado: '))
        resultado = busca_interpolacao_codigos(lista, cod_busca, True)
        if resultado != -1:
            print(f'O código do cliente {cod_busca} foi encontrado na lista.')
            print('=-' * 14)
            lista.sort(key=lambda x: x.codCliente) # Ordena a lista de clientes pelo código
            print(lista[resultado])
        else:
            print(f'O código do cliente {cod_busca} não foi encontrado na lista.')
    
    elif opc == 4:
        verClientes(lista)
    
    elif opc == 5:
        break
    else:
        print('\033[31m  OPÇÃO INVÁLIDA!  \033[m'.center(37))
