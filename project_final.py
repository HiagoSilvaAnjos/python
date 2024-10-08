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

os.system("clear")

while not kill_programing:
    print(menu_list)
    option = input("Escolha uma opção: ")

    if option == "1":
        os.system("clear")
        name = input("Nome do game: ")
        year = int(input("Ano de lançamento: "))
        price = float(input("Preço do game: "))
        game = {"name": name, "year": year, "price": price}
        games.append(game)
        print("Game cadastrado com sucesso!")

    if option == "2":
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
                break
        if not found_game:
            print("Game não encontrado.")

    if option == "3":
        os.system("clear")
        len_list = len(games)
        print("Todos os games cadastrados:")
        for game_index in range(len_list):
            get_game = games[game_index]
            print(f"Nome: {get_game['name']}")
            print(f"Ano de lançamento: {get_game['year']}")
            print(f"Preço: {get_game['price']}\n")
            print()

    if option == "5":
        os.system("clear")
        kill_programing = True
        print("Saindo do sistema...")

