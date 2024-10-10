# Fluxo do Programa de Gerenciamento de Jogos

# Este documento descreve o fluxo e a funcionalidade do programa em Python que gerencia uma lista de jogos, permitindo a inserção, busca, visualização, remoção e exibição de um intervalo específico de games. A seguir, será detalhado o que cada parte do código faz, facilitando a compreensão do seu funcionamento.

# 1. Estrutura Principal do Programa

# O programa é um sistema interativo com um menu principal que permite ao usuário escolher entre várias operações relacionadas a games. Ele segue um fluxo de repetição até que o usuário opte por sair.

# 2. Variáveis Globais

# - `games = []`: Uma lista vazia onde os jogos serão armazenados. Cada jogo será um dicionário contendo três atributos: nome, ano de lançamento e preço.
  
# - `kill_programing = False`: Um flag booleano usado para controlar o ciclo do programa. Quando definido como `True`, o programa para de rodar.

# - `menu_list`: Uma string que contém o menu de opções que será exibido ao usuário.

# 3. Funções Implementadas

# a) Função `handle_add_game()`
#    - Objetivo: Permite ao usuário inserir um novo jogo, capturando o nome, o ano de lançamento e o preço.
#    - Passos:
#      1. Limpa o terminal.
#      2. Solicita ao usuário os dados do jogo.
#      3. Armazena os dados como um dicionário na lista `games`.
#      4. Exibe uma mensagem de sucesso.
     
# b) Função `search_games()`
#    - Objetivo: Busca por um jogo específico pelo nome.
#    - Passos:
#      1. Limpa o terminal.
#      2. Verifica se a lista `games` está vazia.
#      3. Solicita o nome do jogo que o usuário deseja buscar.
#      4. Percorre a lista de jogos, comparando o nome do jogo buscado com os nomes na lista.
#      5. Exibe os detalhes do jogo se encontrado, ou uma mensagem de erro se o jogo não estiver cadastrado.
     
# c) Função `games_list()`
#    - Objetivo: Exibe todos os jogos cadastrados.
#    - Passos:
#      1. Limpa o terminal.
#      2. Verifica se a lista `games` está vazia.
#      3. Percorre a lista de jogos e exibe os detalhes de cada jogo.

# d) Função `find_interval_games()`
#    - Objetivo: Exibe uma fatia (intervalo) da lista de jogos, com base em índices fornecidos pelo usuário.
#    - Passos:
#      1. Limpa o terminal.
#      2. Verifica se a lista `games` está vazia.
#      3. Solicita ao usuário o índice inicial e o índice final do intervalo desejado.
#      4. Verifica a validade do intervalo (os índices devem estar dentro dos limites da lista).
#      5. Exibe os jogos no intervalo especificado.

# e) Função `remove_game_to_list()`
#    - Objetivo: Remove um jogo específico da lista de jogos.
#    - Passos:
#      1. Limpa o terminal.
#      2. Verifica se a lista `games` está vazia.
#      3. Solicita o nome do jogo a ser removido.
#      4. Percorre a lista e, se o jogo for encontrado, ele é removido da lista.
#      5. Exibe uma mensagem de sucesso ou erro, dependendo do resultado.

# 4. Fluxo Principal do Programa

# O fluxo principal do programa é controlado por um loop `while`, que continua executando até que o usuário escolha a opção de sair (opção 6). A cada iteração, o menu de opções é exibido, e o usuário pode escolher qual função deseja executar.

# a) Opções do Menu:
#    1. Inserir um novo game: Chama a função `handle_add_game()`.
#    2. Buscar um game pelo nome: Chama a função `search_games()`.
#    3. Imprimir todos os games cadastrados: Chama a função `games_list()`.
#    4. Imprimir um trecho específico da lista de games: Chama a função `find_interval_games()`.
#    5. Remover um game da lista: Chama a função `remove_game_to_list()`.
#    6. Sair do sistema: Define a variável `kill_programing` como `True`, encerrando o loop e o programa.

# b) Fluxo de Tratamento de Erros:
#    - Sempre que o usuário interage com o programa, pode haver entradas inválidas (por exemplo, digitar algo que não seja um número ao se pedir um preço). Nestes casos, exceções são capturadas e uma mensagem de erro amigável é exibida, permitindo que o usuário tente novamente sem quebrar o programa.