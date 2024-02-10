class Cliente:
    """
    Classe Cliente: Representa um cliente de uma loja.
    """

    def __init__(self, nome, endereco, codCliente):
        self.nome = nome
        self.endereco = endereco
        self.codCliente = codCliente

    def __str__(self):
        """
        Método __str__: Retorna uma string com os dados do cliente.
        """
        return f"Nome: {self.nome}\nIdade: {self.endereco}\nID: {self.codCliente}"


def menu(lista):
    """
    Função menu: Imprime o menu de opções do programa.
    não recebe parâmetros e não retorna nada.
    """
    print('=-' *14)
    print('[1] ADICIONAR CLIENTE\n[2] BUSCAR POR NOME\n[3] BUSCAR POR CÓDIGO\n[4] SAIR')
    
    while(True):
        opc = int(input('ESCOLHA UMA OPÇÃO: '))
        print('=-' *14)
        if opc == 1:
            cliente = preenche(lista)
            escreverArquivo(cliente)
        elif opc == 2:
            imprime(lista)
        elif opc == 3:
            arquivo = open("clientes.txt", "r")
            print(arquivo.read())
        elif opc == 4:
            fecharArquivo(arquivo)
            break


def preenche(lista):
    """
    Função preenche: Preenche a lista de clientes com os dados dos clientes.
    receberá a lista de clientes e retornará a lista atualizada.
    """
    print("Informe os dados do Cliente:")
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    codCliente = int(input("ID: "))
    cliente = Cliente(nome, endereco, codCliente)
    lista.append(cliente)
    return cliente


def escreverArquivo(cliente):
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f"{cliente}\n")


def imprime(lista):
    """
    Função imprime: Imprime a lista de clientes.
    """
    print("Lista de Clientes:")
    for clientes in lista:
        print(clientes)
    return print(f'Clintes cadastrados {len(lista)}')

def fecharArquivo(arquivo):
    arquivo.close()
    return print('Arquivo fechado com sucesso!')