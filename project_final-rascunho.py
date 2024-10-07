# Sistema de Cadastro de Games - Algoritmo Explicado em Comentários

# Lista para armazenar os dados
# Inicialmente, teremos uma lista vazia chamada "games" onde os dados dos jogos serão armazenados.
# A lista terá um limite de 50 registros.
games = []

# Função para inserir um novo game:
# 1. Verifique se a lista já tem 50 elementos (para evitar que a lista ultrapasse o limite).
# 2. Se a lista estiver cheia, exiba uma mensagem avisando que não é possível adicionar mais jogos.
# 3. Caso haja espaço, solicite ao usuário:
#    - O nome do game (string)
#    - O ano de lançamento (inteiro)
#    - O preço do game (float)
# 4. Crie um dicionário com essas informações e adicione-o ao final da lista "games".
# 5. Exiba uma mensagem confirmando que o game foi cadastrado com sucesso.

# Função para buscar um game pelo nome:
# 1. Solicite ao usuário o nome do game que deseja buscar.
# 2. Percorra a lista "games" utilizando um laço de repetição.
# 3. Para cada game, compare o nome (transformado para minúsculas) com o nome fornecido pelo usuário.
# 4. Se o nome for encontrado:
#    - Exiba as informações do game e a posição onde ele foi encontrado na lista.
#    - Finalize o laço sem usar "break", apenas ajustando o índice para sair.
# 5. Se o game não for encontrado, exiba a mensagem "Game não encontrado."

# Função para imprimir todos os games:
# 1. Verifique se a lista está vazia.
# 2. Se a lista estiver vazia, exiba uma mensagem avisando que não há games cadastrados.
# 3. Caso contrário, percorra a lista "games" e, para cada elemento:
#    - Exiba o índice do game na lista.
#    - Exiba o nome, o ano de lançamento e o preço do game.

# Função para imprimir um trecho da lista:
# 1. Solicite ao usuário dois índices: o índice inicial e o índice final.
# 2. Verifique se os índices fornecidos são válidos:
#    - O índice inicial deve ser maior ou igual a 0.
#    - O índice final deve ser menor que o tamanho da lista.
#    - O índice inicial deve ser menor ou igual ao índice final.
# 3. Se os índices forem válidos:
#    - Percorra a lista do índice inicial até o índice final e exiba as informações dos games.
# 4. Se os índices forem inválidos, exiba a mensagem "Intervalo inválido."

# Função para mostrar o menu e processar as opções:
# 1. Exiba um menu com as opções:
#    - Inserir um novo game.
#    - Buscar um game pelo nome.
#    - Imprimir todos os games cadastrados.
#    - Imprimir um trecho específico da lista de games.
#    - Sair do sistema.
# 2. Solicite ao usuário que escolha uma opção.
# 3. Dependendo da escolha:
#    - Chame a função correspondente (inserir, buscar, imprimir todos, imprimir trecho).
# 4. Caso o usuário escolha uma opção inválida, exiba uma mensagem de erro e peça para ele escolher novamente.
# 5. Continue exibindo o menu até que o usuário escolha a opção "Sair".
# 6. Ao escolher a opção "Sair", o sistema deve finalizar.

# Execução do sistema:
# 1. Quando o programa é iniciado, chame a função "menu".
# 2. O sistema continuará em loop, exibindo o menu e aguardando as interações do usuário.
# 3. O sistema só terminará quando o usuário escolher explicitamente a opção de saída.
