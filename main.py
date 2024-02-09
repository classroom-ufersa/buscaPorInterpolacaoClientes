from clientes import Cliente, preenche, imprime, menu

lista = []

while(True):
    menu()
    opc = int(input('ESCOLHA UMA OPÇÃO: '))
    if opc == 1:
        preenche(lista)
    elif opc == 2:
        imprime(lista)
    elif opc == 4:
        break