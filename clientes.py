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
        return f"Nome: {self.nome}\nEndereço: {self.endereco}\nID: {self.codCliente}"


def menu():
    """
    Função menu: Imprime o menu de opções do programa.
    não recebe parâmetros e não retorna nada.
    """
    print('====== <<< \033[36m MENU\033[m  >>> ======')
    print('|  [\033[36m1\033[m] ADICIONAR CLIENTE   |\n|  [\033[36m2\033[m] BUSCAR POR NOME     |\n|  [\033[36m3\033[m] BUSCAR POR CÓDIGO   |\n|  [\033[36m4\033[m] VER OS CLIENTES     |\n|  [\033[36m5\033[m] SAIR\t\t   |')
    print('-' * 28)


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
    Função escreverArquivo: Escreve os dados do cliente no arquivo clientes.txt.
    """
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f'{cliente.nome}, {cliente.endereco}, {cliente.codCliente}\n')


def verificarID(lista):
    """
    Função verificarID: Recebe uma lista e verifica o ID fornecido está disponível.
    Caso o ID já esteja em uso, a função pedirá ao usuário para fornecer um novo ID até que um ID válido seja inserido.
    """
    while True:
        id = int_input('ID: ')

        if any(cliente.codCliente == id for cliente in lista):
            print('\033[31mID já existe. Tente novamente.\033[m')
        else:
            return id


def int_input(msg):
    """
    Função para ler apenas números.
    """

    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError, NameError, EOFError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu digitar nada.\033[m')
            return 0
        else:
            return num
        

def str_input(msg):
    """
    Função para ler apenas nomes.
    """
    while True:
        try:
            nome = input(msg)    # Converte o nome para minúsculas
            if not nome.replace(" ", "").isalpha():
                raise ValueError('O nome deve conter apenas letras.')
        except ValueError as ve:
            print('\033[31mERRO! Por favor, digite um nome válido.\033[m')
        except EOFError:
            print('\033[31mERRO! Por favor, digite um nome válido.\033[m')
        except KeyboardInterrupt:
                print('\033[31mUsuário preferiu digitar nada.\033[m')
                return 'NULL'
        else:
            return nome.strip()


def preenche(lista):
    """
    Função preenche: Preenche a lista de clientes com os dados dos clientes.
    receberá a lista de clientes e retornará a lista atualizada.
    """
    print("Informe os dados do Cliente:")
    nome = str(str_input('Nome: ')) 
    endereco = str(input("Endereço: "))
    codCliente = verificarID(lista)
    cliente = Cliente(nome, endereco, codCliente)
    lista.append(cliente)
    escreverArquivo(cliente)
    
    return cliente


def verClientes(lista):
    """
    Mostra na tela a quantidade e as infomações de todos os clientes cadastrados. 
    """
    for cliente in lista:
        print(f'{cliente}')
        print('-=' * 15)
    print(f'Total de clientes: {len(lista)}')


def busca_interpolacao_nomes(lista_nomes, chave, contagem=False):
    """
    Função busca_interpolacao_nomes: Realiza a busca por um nome na lista de clientes utilizando o método de busca por interpolação.
    """
    import time

    if contagem:
        start_time = time.time()

    lista_clientes = lista_nomes
    lista_nomes = [cliente.nome for cliente in lista_clientes]
    lista_nomes.sort()
    inicio = 0
    fim = len(lista_nomes) - 1

    if(inicio == fim):
        return 0
    
    while inicio <= fim:
        try:
            # Calcula a posição utilizando uma média ponderada das posições dos caracteres
            posicao = inicio + int(((ord(chave[0]) - ord(lista_nomes[inicio][0])) / (
            ord(lista_nomes[fim][0]) - ord(lista_nomes[inicio][0]))) * (fim - inicio))
        except ZeroDivisionError:
            return -1
        if lista_nomes[posicao] == chave:
            if contagem:
                end_time = time.time() - start_time
                print(f'Tempo de execução: {end_time} segundos')
            return posicao  # Chave encontrada
        elif lista_nomes[posicao] < chave:
            inicio = posicao + 1
        else:
            fim = posicao - 1

    return -1  # Chave não encontrada


def busca_interpolacao_codigos(lista_codigos, chave, contagem=False):
    """
    Função busca_interpolacao_codigos: Realiza a busca por um código na lista de clientes utilizando o método de busca por interpolação.
    """
    import time

    if contagem:
        start_time = time.time()
    
    lista_clientes = lista_codigos
    lista_codigos = [cliente.codCliente for cliente in lista_clientes]
    lista_codigos.sort()
    inicio = 0
    fim = len(lista_codigos) - 1

    if (inicio == fim):
        return 0
    
    while inicio <= fim and lista_codigos[inicio] <= chave <= lista_codigos[fim]:
        try:
        # Calcula a posição utilizando uma média ponderada das posições dos códigos
            posicao = inicio + int(((chave - lista_codigos[inicio]) / (
            lista_codigos[fim] - lista_codigos[inicio])) * (fim - inicio))
        except ZeroDivisionError:
            return -1
        if lista_codigos[posicao] == chave:
            if contagem:
                end_time = time.time() - start_time
                print(f'Tempo de execução: {end_time} segundos')
            return posicao  # Chave encontrada
        elif lista_codigos[posicao] < chave:
            inicio = posicao + 1
        else:
            fim = posicao - 1

    return -1

