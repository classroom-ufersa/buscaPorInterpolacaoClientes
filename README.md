<div>
<img align="right" width="110" height="170" src="https://assecom.ufersa.edu.br/wp-content/uploads/sites/24/2014/09/PNG-bras%C3%A3o-Ufersa.png">
<br>
<h1 align="center" style="font-weight: bold;">Busca por interpolação 💻</h1>
<p align="center">
    <a href="#requirements">Requisitos do Projeto</a>•
    <a href="#tech">Tecnologias</a> •
    <a href="#about">Sobre o Algoritmo</a> •
    <a href="#complexity">Complexidade</a> •
    <a href="#config">Config. de Teste</a> •
    <a href="#colab">Colaboradores</a> •
</p>

<h2 id="requirements" style="font-weight: bold; font-size: 2rem">Requisitos do Projeto</h2>
</div>

✅A cada execução do programa, ele deve carregar os dados(armazenados em um arquivo texto).</br>
✅O programa deve perguntar ao usuario qual cliente ele deseja buscar por nome ou codigo com o algoritmo Busca por interpolação.</br>
✅Compute o tempo de execução do processo de busca.</br>
✅Informe a complexidade do algoritmo Busca por Interpolação.</br>

<div>
  <h2 id="tech" style="font-weight: bold; font-size: 2rem">Tecnologia Utilizada</h2> 
  <img align="center" alt="python" src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/>

  <h2 id="about" style="font-weight: bold; font-size: 2rem">Sobre o Algoritmo</h2>

O algoritmo de busca por interpolação é uma técnica de busca em estruturas de dados ordenadas que usa uma fórmula de interpolação para estimar a posição do elemento desejado de forma mais precisa do que a busca binária tradicional.

## Como Funciona

O algoritmo de busca por interpolação estima a posição do elemento desejado usando uma fórmula e ajusta essa estimativa com base nos valores dos elementos até encontrar o elemento desejado ou determinar sua ausência.

![busca por interpolação](https://github.com/classroom-ufersa/buscaPorInterpolacaoClientes/assets/111452823/fdc14f93-df12-4190-b048-d2181bcc6465)

## Implementação

```
  def busca_interpolacao(lista, chave):
      inicio = 0
      tentativas = 1
      fim = len(lista) - 1

      while inicio <= fim and ord(lista[inicio][0]) <= ord(chave[0]) <= ord(lista[fim][0]):
          # calcula a posição utilizando uma média ponderada das posições.
          posicao = inicio + int(((ord(chave[0]) - ord(lista[inicio][0]))/(ord(lista_nomes[fim][0]) - ord(lista[inicio][0]))) * (fim - inicio))
          if lista[posicao] == chave:
              return posicao # chave encontrada
          elif lista[posicao] < chave:
              inicio = posicao - 1
          else:
              fim = posicao - 1

      return -1 # chave não encontrada
```

## Como rodar na minha maquina?

Clone o repositorio na sua maquina:

```bash
git clone https://github.com/classroom-ufersa/buscaPorInterpolacaoClientes.git
```

Para executar você precisa navegar até o diretório onde o arquivo Python está localizado. No terminal use este comando:

```python
python main.py
```

  <h2 id="complexity" style="font-weight: bold; font-size: 2rem">Complexidade</h2>

### Pior Caso:

O pior caso ocorre quando a estimativa da posição do elemento não é precisa e o algoritmo se comporta de forma semelhante à busca linear, visitando cada elemento do array. Portanto, a complexidade para o pior caso é O(n).

```
c1 * 1 + c2 * 1 + c3 * n + c4 * n + c5 * n + c6 * n + c7 * n + c8 * n + c9 * 1 = O(n)
```

### Caso Médio:

No caso médio, a complexidade depende da distribuição dos dados. Se assumirmos que os dados estão uniformemente distribuídos, a complexidade média é aproximadamente <span style="font-weight: bold;">O(log(log n))</span> ou melhor. No entanto, calcular a complexidade exata do caso médio requer uma análise probabilística detalhada da distribuição dos dados.

### Melhor Caso:

O melhor caso ocorre quando a interpolação consegue estimar a posição do elemento corretamente desde o início, resultando em uma única iteração. Portanto, a complexidade para o melhor caso é O(1).

```
c1 * 1 + c2 * 1 + c3 * 1 + c4 * 1 + c5 * 1 + c6 * 1 + c7 * 1 + c8 * 1 + c9 * 1 = O(1)
```

  <h2 id="config" style="font-weight: bold; font-size: 2rem">Configuração usada nos testes</h2>
  CPU: AMD Ryzen 5 5500U</br>
  Frequência: 2.1GHz até 4GHz</br>
  Clock base: 100MHz</br>
  RAM: 10gb DDR4</br>
  
  <h2 id="colab" style="font-weight: bold; font-size: 2rem">Colaboradores</h2>
  Um agradecimento especial a todas as pessoas que contribuíram para este projeto.
  <table>
    <tr>
      <td align="center">
        <a href="#">
          <img src="https://avatars.githubusercontent.com/u/111452823?v=4" width="100px;" alt="Fernanda Kipper Profile Picture"/><br>
          <sub>
            <a href="https://github.com/gusjjpv"><b>João Gustavo</b></a>
          </sub>
        </a>
      </td>
      <td align="center">
        <a href="#">
          <img src="https://avatars.githubusercontent.com/u/146228058?v=4" width="100px;" alt="Elon Musk Picture"/><br>
          <sub>
            <a href="https://github.com/ViniciusOliver13"><b>Antonio Vinícius</b></a>
          </sub>
        </a>
      </td>
      <td align="center">
        <a href="#">
          <img src="https://avatars.githubusercontent.com/u/140117398?v=4" width="100px;" alt="Foto do Steve Jobs"/><br>
          <sub>
            <a href="https://github.com/marceloDev0"><b>Marcelo Augusto</b></a>
          </sub>
        </a>
      </td>
      <td align="center">
        <a href="#">
          <img src="https://avatars.githubusercontent.com/u/88439767?v=4" width="100px;" alt="Foto do Steve Jobs"/><br>
            <sub>
              <a href="https://github.com/DuardoEdu2"><b>Eduardo Abrantes</b></a>
            </sub>
        </a>
      </td>
    </tr>
  </table>
</div>
