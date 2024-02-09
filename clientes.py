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


def preenche(lista):
    """
    Função preenche: Preenche a lista de clientes com os dados dos clientes.
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
