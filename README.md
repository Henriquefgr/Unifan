Disciplina: ALGORITMO E ESTRUTURA DE DADOS
Professor: Msc. João Alberto Castelo Branco Oliveira

Atividade Individual: Projeto de Sistema de Gestão de
Biblioteca
Objetivo da Atividade:
Essa atividade desafia os alunos a aplicar conceitos fundamentais de estruturas
de dados e algoritmos para resolver problemas reais. Os alunos devem
demonstrar uma compreensão sólida de como escolher e implementar a
estrutura de dados e o algoritmo mais adequado para cada situação, levando em
consideração aspectos como complexidade de tempo e espaço, eficiência de
busca e ordenação, e gerenciamento dinâmico de informações.
Situação-Problema:
Você foi contratado como desenvolvedor para criar um sistema de gestão de
uma biblioteca digital. A biblioteca precisa de uma solução eficiente para
gerenciar seu acervo de livros, otimizar a busca por títulos, autores e categorias,
além de manter o controle sobre os empréstimos realizados pelos usuários. O
sistema deve utilizar estruturas de dados adequadas para garantir o bom
desempenho em todas as operações de gerenciamento.
Desafios a serem resolvidos:
1. Organização do Acervo de Livros
o Cenário: O acervo da biblioteca contém atualmente 50.000 livros,
e esse número cresce a cada dia. Os livros são identificados por
um ID único, título, autor e categoria.
o Tarefa: Implemente uma estrutura de dados que permita
armazenar essas informações de maneira eficiente. Considere o
uso de uma árvore de busca binária (BST) para manter os livros
ordenados pelo título e, ao mesmo tempo, permitir a busca rápida
por autor ou categoria.
o Desafio adicional: Modifique a estrutura para usar uma árvore
AVL para garantir que a árvore esteja sempre balanceada e as
operações de busca sejam rápidas, mesmo com o crescimento do
acervo.

2. Busca Rápida de Livros
o Cenário: Os usuários frequentemente buscam por livros
específicos utilizando o título, autor ou categoria. O sistema deve
responder rapidamente às solicitações de busca.
o Tarefa: Implemente funções de pesquisa binária e pesquisa
sequencial para encontrar livros com base em diferentes critérios

(por título, autor ou categoria). Compare o desempenho das duas
funções em diferentes tamanhos de dados e justifique a escolha do
algoritmo de busca mais eficiente para cada caso.
o Desafio adicional: Implemente uma função de busca que combine
os três critérios (título, autor, categoria) utilizando uma estrutura de
árvore de busca que mantenha os dados indexados por múltiplos
campos.
3. Ordenação dos Livros
o Cenário: A biblioteca deseja oferecer listas de livros ordenadas por
diferentes critérios, como ano de publicação, popularidade (número
de empréstimos) ou ordem alfabética.
o Tarefa: Implemente algoritmos de ordenação (como Quick Sort,
Merge Sort e Bubble Sort) para ordenar os livros por diferentes
critérios. Avalie qual algoritmo é mais adequado para cada critério,
considerando o tamanho do acervo e a frequência de atualização
das informações.
o Desafio adicional: Automatize a escolha do algoritmo de
ordenação com base no tamanho da coleção e na eficiência
necessária.

4. Gerenciamento de Empréstimos
o Cenário: A biblioteca precisa de um sistema para gerenciar os
empréstimos de livros pelos usuários. Os livros emprestados
devem ser retirados do acervo disponível, e os usuários devem ser
notificados sobre a data de devolução.
o Tarefa: Implemente uma fila para gerenciar os empréstimos de
livros. Use uma estrutura de dados de pilha para implementar o
histórico de empréstimos de cada usuário, permitindo "desfazer"
empréstimos em caso de erro.
o Desafio adicional: Crie um sistema de prioridade para a fila de
empréstimos, onde usuários com um histórico maior de devoluções
em dia tenham prioridade no acesso a livros disputados.

5. Relatórios de Atividade e Desempenho
o Cenário: A biblioteca deseja gerar relatórios de desempenho
semanalmente, mostrando as operações de empréstimo,
devoluções pendentes, e o uso das diferentes funcionalidades do
sistema.
o Tarefa: Use estruturas contíguas e encadeadas para armazenar
registros de operações. Implemente funções que gerem relatórios
sobre a atividade dos usuários e o desempenho do sistema,
analisando a eficiência das operações realizadas.
