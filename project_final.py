import os

games = []
kill_programing = False
menu_list = """
    MENU DE OPÇÕES:
    1. Inserir um novo game
    2. Buscar um game pelo nome
    3. Imprimir todos os games cadastrados
    4. Imprimir um trecho específico da lista de games
    5. Sair do sistema
"""

#FIXME: METHODS

def handle_add_game():
    os.system("clear")
    name = input("Nome do game: ")
    year = int(input("Ano de lançamento: "))
    price = float(input("Preço do game: "))
    game = {"name": name, "year": year, "price": price}
    games.append(game)
    os.system("clear")
    print("Game cadastrado com sucesso!")

def search_games():
    os.system("clear")
    name = input("Nome do game: ")
    len_list = len(games)
    found_game = False
    for game_index in range(len_list):
        get_game = games[game_index]
        if get_game["name"].lower() == name.lower():
            found_game = True
            print(f"Nome: {get_game['name']}")
            print(f"Ano de lançamento: {get_game['year']}")
            print(f"Preço: {get_game['price']}")
    if not found_game:
        print("Game não encontrado.")

def games_list():
    os.system("clear")
    len_list = len(games)
    print("Todos os games cadastrados:")
    for game_index in range(len_list):
        get_game = games[game_index]
        print(f"Nome: {get_game['name']}")
        print(f"Ano de lançamento: {get_game['year']}")
        print(f"Preço: {get_game['price']}\n")
        print()

def find_interval_games():
    os.system("clear")
    start_index = int(input("Índice inicial: "))
    end_index = int(input("Índice final: "))
    len_list = len(games)

    if start_index >= 0 and end_index < len_list and start_index <= end_index:
        print("Trecho da lista:")
        for game_index in range(start_index, end_index + 1):
            get_game = games[game_index]
            print(f"Nome: {get_game['name']}")
            print(f"Ano de lançamento: {get_game['year']}")
            print(f"Preço: {get_game['price']}\n")
            print()
    else:
        print("Intervalo inválido.")

while not kill_programing:
    print(menu_list)
    option = input("Escolha uma opção: ")

    if option == "1":
        if len(games) >= 50:
            print("Limite de jogos atingido! Não é possível cadastrar mais.")
            continue
        try:
            handle_add_game()
        except Exception as e:
            print("Você inseriu dados inválidos! Por favor, tente novamente...")
            continue
       
    if option == "2":
        try:
            search_games()
        except Exception as e:
            print("Falha ao buscar game! Por favor, tente novamente...")
            continue

    if option == "3":
        try:
            games_list()
        except Exception as e:
            print("Falha ao carregar games! Por favor, tente novamente...")
            continue

    if option == "4":
        try:
            find_interval_games()
        except Exception as e:
            print("Você inseriu dados inválidos! Por favor, tente novamente...")
            continue        

    if option == "5":
        os.system("clear")
        kill_programing = True
        print("Saindo do sistema...")

