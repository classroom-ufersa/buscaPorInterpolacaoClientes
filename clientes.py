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
        Método str: Retorna uma string com os dados do cliente.
        """
        return f"Nome: {self.nome}\nIdade: {self.endereco}\nID: {self.codCliente}"


def menu():
    """
    Função menu: Imprime o menu de opções do programa.
    não recebe parâmetros e não retorna nada.
    """
    print('=-' * 14)
    print('[1] ADICIONAR CLIENTE\n[2] BUSCAR POR NOME\n[3] BUSCAR POR CÓDIGO\n[4] SAIR')


def lerArquivo():
    try:
        with open("clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            lista_clientes = []
            for linha in linhas:
                nome, endereco, codCliente = linha.strip().split(',')
                cliente = Cliente(nome, endereco, int(codCliente))
                lista_clientes.append(cliente)
            return lista_clientes
    except FileNotFoundError:
        return []


def escreverArquivo(cliente):
    """
    Função escreverArquivo: Escreve os dados do cliente no arquivo clientes.txt."""
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f'{cliente.nome}, {cliente.endereco}, {cliente.codCliente}\n')


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
    escreverArquivo(cliente)
    
    return cliente


def busca_interpolacao_nomes(lista_nomes, chave):
    lista_clientes = lista_nomes
    lista_nomes = [cliente.nome for cliente in lista_clientes]
    lista_nomes.sort()
    inicio = 0
    fim = len(lista_nomes) - 1

    while inicio <= fim:
        # Calcula a posição utilizando uma média ponderada das posições dos caracteres
        posicao = inicio + int(((ord(chave[0]) - ord(lista_nomes[inicio][0])) / (
            ord(lista_nomes[fim][0]) - ord(lista_nomes[inicio][0]))) * (fim - inicio))

        if lista_nomes[posicao] == chave:
            return posicao  # Chave encontrada
        elif lista_nomes[posicao] < chave:
            inicio = posicao + 1
        else:
            fim = posicao - 1

    return -1  # Chave não encontrada


def busca_interpolacao_codigos(lista_codigos, chave):
    lista_clientes = lista_codigos
    lista_codigos = [cliente.codCliente for cliente in lista_clientes]
    lista_codigos.sort()
    inicio = 0
    fim = len(lista_codigos) - 1

    while inicio <= fim and lista_codigos[inicio] <= chave <= lista_codigos[fim]:
        # Calcula a posição utilizando uma média ponderada das posições dos códigos
        posicao = inicio + int(((chave - lista_codigos[inicio]) / (
            lista_codigos[fim] - lista_codigos[inicio])) * (fim - inicio))
        if lista_codigos[posicao] == chave:
            return posicao  # Chave encontrada
        elif lista_codigos[posicao] < chave:
            inicio = posicao + 1
        else:
            fim = posicao - 1

    return -1