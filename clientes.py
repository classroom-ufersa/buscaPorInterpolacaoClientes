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


def menu():
    """
    Função menu: Imprime o menu de opções do programa.
    não recebe parâmetros e não retorna nada.
    """
    print('=-' *14)
    print('[1] ADICIONAR CLIENTE\n[2] BUSCAR POR NOME\n[3] BUSCAR POR CÓDIGO\n[4] SAIR')
    print('=-' *14)


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
    return lista


def imprime(lista):
    """
    Função imprime: Imprime a lista de clientes.
    """
    print("Lista de Clientes:")
    for clientes in lista:
        print(clientes)
    return print(f'Clintes cadastrados {len(lista)}')
