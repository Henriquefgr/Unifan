from datetime import datetime
import sys
import heapq

class Livro:
    
    #Classe que representa um livro na biblioteca.

   
    def __init__(self, id, titulo, autor, categoria):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria

    def __repr__(self):
        """
        Retorna uma representação string do livro, útil para exibição.
        """
        return f"{self.id} - {self.titulo} - {self.autor} - {self.categoria}"

class NoAVL:
    """
    Representa um no da árvore AVL .
    
    Atributos:
    livro: Objeto da classe Livro armazenado no no.
    esquerda: Referencia para o no a esquerda.
    direita: Referencia para o no a direita.
    altura: Altura do no, usada para o balanceamento da arvore.
    """
    def __init__(self, livro):
        self.livro = livro
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    
    #Implementacao de uma arvore AVL para armazenar livros de forma balanceada.
    
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        """
        Retorna a altura de um no.
        """
        if not no:
            return 0
        return no.altura

    def balanceamento(self, no):
        """
        Calcula o fator de balanceamento de um no
        """
        if not no:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, y):
        """
        Realiza a rotacao a direita em torno do no 'y' para balancear a arvore.
        """
        x = y.esquerda
        T2 = x.direita
        x.direita = y
        y.esquerda = T2
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))
        return x

    def rotacao_esquerda(self, x):
        """
        Realiza a rotacao a esquerda em torno do nó 'x' para balancear a arvore.
        """
        y = x.direita
        T2 = y.esquerda
        y.esquerda = x
        x.direita = T2
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        return y

    def inserir(self, no, livro):
        """
        Insere um livro na árvore AVL, mantendo o balanceamento.
        """
        if not no:
            return NoAVL(livro)
        if livro.titulo < no.livro.titulo:
            no.esquerda = self.inserir(no.esquerda, livro)
        else:
            no.direita = self.inserir(no.direita, livro)

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        balance = self.balanceamento(no)

        if balance > 1 and livro.titulo < no.esquerda.livro.titulo:
            return self.rotacao_direita(no)
        if balance < -1 and livro.titulo > no.direita.livro.titulo:
            return self.rotacao_esquerda(no)
        if balance > 1 and livro.titulo > no.esquerda.livro.titulo:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)
        if balance < -1 and livro.titulo < no.direita.livro.titulo:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def remover(self, no, titulo):
        """
        Remove um livro da arvore AVL, mantendo o balanceamento apos a remocao.
        """
        if not no:
            return no

        if titulo < no.livro.titulo:
            no.esquerda = self.remover(no.esquerda, titulo)
        elif titulo > no.livro.titulo:
            no.direita = self.remover(no.direita, titulo)
        else:
            if no.esquerda is None:
                temp = no.direita
                no = None
                return temp
            elif no.direita is None:
                temp = no.esquerda
                no = None
                return temp

            temp = self.get_minimo(no.direita)
            no.livro = temp.livro
            no.direita = self.remover(no.direita, temp.livro.titulo)

        if not no:
            return no

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        balance = self.balanceamento(no)

        if balance > 1 and self.balanceamento(no.esquerda) >= 0:
            return self.rotacao_direita(no)
        if balance > 1 and self.balanceamento(no.esquerda) < 0:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)
        if balance < -1 and self.balanceamento(no.direita) <= 0:
            return self.rotacao_esquerda(no)
        if balance < -1 and self.balanceamento(no.direita) > 0:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def get_minimo(self, no):
        """
        Retorna o nó com o menor valor.
        """
        if no is None or no.esquerda is None:
            return no
        return self.get_minimo(no.esquerda)

    def in_order(self, no, livros=[]):
        """
        Realiza uma travessia em ordem  da arvore, retornando uma lista
        com todos os livros armazenados na arvore.
        """
        if no:
            self.in_order(no.esquerda, livros)
            livros.append(no.livro)
            self.in_order(no.direita, livros)
        return livros

class FilaPrioridade:
    """
    Implementação de uma fila de prioridade baseada em heap (min-heap).
    Usada para gerenciar empréstimos de livros com prioridade.
    """
    def __init__(self):
        self.pq = []  # Lista para heap
        self.contador = 0  # Contador para manter a ordem de inserção

    def enqueue(self, prioridade, item):
        """
        Adiciona um item à fila com uma prioridade. Os itens com maior prioridade
        serão retirados primeiro.
        """
        heapq.heappush(self.pq, (-prioridade, self.contador, item))
        self.contador += 1

    def dequeue(self):
        """
        Remove e retorna o item com a maior prioridade da fila.
        """
        if self.is_empty():
            return None
        return heapq.heappop(self.pq)[-1]

    def is_empty(self):
        """
        Verifica se a fila de prioridade está vazia.
        """
        return len(self.pq) == 0

class Biblioteca:
    """
    Classe principal que gerencia a biblioteca, incluindo o acervo de livros, empréstimos
    e a organização por autor e categoria.
    """
    def __init__(self):
        self.livros = ArvoreAVL()
        self.autores = {}  # Dicionário de autores -> lista de livros
        self.categorias = {}  # Dicionário de categorias -> lista de livros
        self.emprestimos = FilaPrioridade()
        self.registros_atividade = []

    def adicionar_livro(self, livro):
        """
        Adiciona um livro ao acervo da biblioteca. O livro é inserido na árvore AVL,
        além de ser indexado nos dicionários por autor e categoria.
        """
        self.livros.raiz = self.livros.inserir(self.livros.raiz, livro)
        if livro.autor not in self.autores:
            self.autores[livro.autor] = []
        self.autores[livro.autor].append(livro)
        if livro.categoria not in self.categorias:
            self.categorias[livro.categoria] = []
        self.categorias[livro.categoria].append(livro)

    def remover_livro(self, titulo):
        """
        Remove um livro do acervo da biblioteca, tanto da árvore AVL quanto dos
        dicionários de autor e categoria.
        """
        livro_removido = self.livros.raiz = self.livros.remover(self.livros.raiz, titulo)
        if livro_removido:
            self.autores[livro_removido.autor].remove(livro_removido)
            if not self.autores[livro_removido.autor]:
                del self.autores[livro_removido.autor]

            self.categorias[livro_removido.categoria].remove(livro_removido)
            if not self.categorias[livro_removido.categoria]:
                del self.categorias[livro_removido.categoria]

    def buscar_por_titulo(self, titulo):
        """
        Busca um livro pelo título na árvore AVL.
        """
        livros = self.livros.in_order(self.livros.raiz)
        for livro in livros:
            if livro.titulo == titulo:
                return livro
        return None

    def buscar_por_autor(self, autor):
        """
        Busca livros por autor nos dicionários de autores.
        """
        return self.autores.get(autor, [])

    def buscar_por_categoria(self, categoria):
        """
        Busca livros por categoria nos dicionários de categorias.
        """
        return self.categorias.get(categoria, [])

    def ordenar_livros(self, chave):
        """
        Ordena os livros por título, autor ou categoria.
        """
        livros = self.livros.in_order(self.livros.raiz)
        if chave == 'titulo':
            return sorted(livros, key=lambda livro: livro.titulo)
        elif chave == 'autor':
            return sorted(livros, key=lambda livro: livro.autor)
        elif chave == 'categoria':
            return sorted(livros, key=lambda livro: livro.categoria)

    def registrar_atividade(self, descricao):
        """
        Registra uma atividade realizada na biblioteca.
        """
        self.registros_atividade.append((datetime.now(), descricao))

class BibliotecaCLI:
    """
    Interface de linha de comando para interagir com a biblioteca.
    Oferece um menu para o usuário escolher as opções de gestão de livros, empréstimos, etc.
    """
    def __init__(self):
        self.biblioteca = Biblioteca()

    def menu(self):
        """
        Exibe o menu principal para o usuário, permitindo que ele escolha
        a operação que deseja realizar (gerenciar acervo, buscar livros, etc).
        """
        while True:
            print("\n--- Menu da Biblioteca ---")
            print("1. Gerenciar Acervo de Livros")
            print("2. Buscar Livros")
            print("3. Ordenar Livros")
            print("4. Gerenciar Empréstimos")
            print("5. Relatório de Atividades")
            print("6. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.gerenciar_acervo()
            elif escolha == '2':
                self.buscar_livros()
            elif escolha == '3':
                self.ordenar_livros()
            elif escolha == '4':
                self.gestionar_emprestimos()
            elif escolha == '5':
                self.relatorio_atividade()
            elif escolha == '6':
                sys.exit(0)
            else:
                print("Opção inválida, tente novamente.")

    def gerenciar_acervo(self):
        """
        Permite ao usuário adicionar ou remover livros do acervo da biblioteca.
        """
        print("\n--- Gerenciar Acervo de Livros ---")
        print("1. Adicionar Livro")
        print("2. Remover Livro")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            id = input("Digite o ID do livro: ")
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            categoria = input("Digite a categoria do livro: ")
            livro = Livro(id, titulo, autor, categoria)
            self.biblioteca.adicionar_livro(livro)
            print(f"Livro {titulo} adicionado com sucesso!")
        elif escolha == '2':
            titulo = input("Digite o título do livro a ser removido: ")
            self.biblioteca.remover_livro(titulo)
            print(f"Livro {titulo} removido com sucesso!")
        else:
            print("Opção inválida!")

    def buscar_livros(self):
        """
        Permite ao usuário buscar livros por título, autor ou categoria.
        """
        print("\n--- Buscar Livros ---")
        print("1. Por Título")
        print("2. Por Autor")
        print("3. Por Categoria")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            titulo = input("Digite o título do livro: ")
            livro = self.biblioteca.buscar_por_titulo(titulo)
            if livro:
                print(livro)
            else:
                print("Livro não encontrado!")
        elif escolha == '2':
            autor = input("Digite o nome do autor: ")
            livros = self.biblioteca.buscar_por_autor(autor)
            if livros:
                for livro in livros:
                    print(livro)
            else:
                print("Nenhum livro encontrado para esse autor!")
        elif escolha == '3':
            categoria = input("Digite a categoria do livro: ")
            livros = self.biblioteca.buscar_por_categoria(categoria)
            if livros:
                for livro in livros:
                    print(livro)
            else:
                print("Nenhum livro encontrado para essa categoria!")
        else:
            print("Opção inválida!")

    def ordenar_livros(self):
        """
        Permite ao usuário ordenar os livros por título, autor ou categoria.
        """
        print("\n--- Ordenar Livros ---")
        print("1. Por Título")
        print("2. Por Autor")
        print("3. Por Categoria")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            livros_ordenados = self.biblioteca.ordenar_livros('titulo')
        elif escolha == '2':
            livros_ordenados = self.biblioteca.ordenar_livros('autor')
        elif escolha == '3':
            livros_ordenados = self.biblioteca.ordenar_livros('categoria')
        else:
            print("Opção inválida!")
            return
        print("\n--- Livros Ordenados ---")
        for livro in livros_ordenados:
            print(livro)

    def gestionar_emprestimos(self):
        """
        Gerencia os empréstimos de livros, mas ainda não implementado.
        """
        print("\n--- Gerenciar Empréstimos ---")
        # Implementar a lógica de empréstimos com base na prioridade
        pass

    def relatorio_atividade(self):
        """
        Exibe o relatório de atividades realizadas na biblioteca.
        """
        print("\n--- Relatório de Atividades ---")
        # Implementar relatório de atividades
        pass

# Executa o menu inicial
BibliotecaCLI().menu()
