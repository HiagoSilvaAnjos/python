import os

games = [
    {"name": "The Witcher 3: Wild Hunt", "year": 2015, "price": 29.99},
    {"name": "Red Dead Redemption 2", "year": 2018, "price": 39.99},
    {"name": "Cyberpunk 2077", "year": 2020, "price": 59.99},
    {"name": "Hades", "year": 2020, "price": 24.99},
    {"name": "God of War", "year": 2018, "price": 19.99},
    {"name": "Hollow Knight", "year": 2017, "price": 14.99},
    {"name": "Celeste", "year": 2018, "price": 19.99},
    {"name": "Elden Ring", "year": 2022, "price": 59.99},
    {"name": "Dark Souls III", "year": 2016, "price": 39.99},
    {"name": "Sekiro: Shadows Die Twice", "year": 2019, "price": 49.99},
    {"name": "Spider-Man: Miles Morales", "year": 2020, "price": 49.99},
    {"name": "Fortnite", "year": 2017, "price": 0.00},
    {"name": "Apex Legends", "year": 2019, "price": 0.00},
    {"name": "Overwatch", "year": 2016, "price": 39.99},
    {"name": "League of Legends", "year": 2009, "price": 0.00},
    {"name": "Valorant", "year": 2020, "price": 0.00},
    {"name": "Among Us", "year": 2018, "price": 4.99},
    {"name": "Minecraft", "year": 2011, "price": 26.95},
    {"name": "Stardew Valley", "year": 2016, "price": 14.99},
    {"name": "Terraria", "year": 2011, "price": 9.99},
    {"name": "DOOM Eternal", "year": 2020, "price": 39.99},
    {"name": "Animal Crossing: New Horizons", "year": 2020, "price": 59.99},
    {"name": "Genshin Impact", "year": 2020, "price": 0.00},
    {"name": "The Legend of Zelda: Breath of the Wild", "year": 2017, "price": 59.99},
    {"name": "Super Mario Odyssey", "year": 2017, "price": 59.99},
    {"name": "Call of Duty: Warzone", "year": 2020, "price": 0.00},
    {"name": "Battlefield V", "year": 2018, "price": 49.99},
    {"name": "FIFA 22", "year": 2021, "price": 59.99},
    {"name": "Madden NFL 22", "year": 2021, "price": 59.99},
    {"name": "Fall Guys: Ultimate Knockout", "year": 2020, "price": 19.99},
    {"name": "Rocket League", "year": 2015, "price": 0.00},
    {"name": "Cuphead", "year": 2017, "price": 19.99},
    {"name": "Resident Evil Village", "year": 2021, "price": 59.99},
    {"name": "Resident Evil 2", "year": 2019, "price": 39.99},
    {"name": "Control", "year": 2019, "price": 29.99},
    {"name": "Outer Wilds", "year": 2019, "price": 24.99},
    {"name": "Horizon Zero Dawn", "year": 2017, "price": 49.99},
    {"name": "Destiny 2", "year": 2017, "price": 0.00},
    {"name": "Far Cry 6", "year": 2021, "price": 59.99},
    {"name": "Dragon Ball Z: Kakarot", "year": 2020, "price": 49.99},
]
kill_programing = False
menu_list = """
    MENU DE OPÇÕES:
    1. Inserir um novo game
    2. Buscar um game pelo nome
    3. Imprimir todos os games cadastrados
    4. Imprimir um trecho específico da lista de games
    5. Remover game de sua lista
    6. Atualizar um game na lista
    7. Sair do sistema
"""

update_list = """
    Opções:
    1. Nome
    2. Ano de lançamento
    3. Preço
"""

def handle_add_game():
    os.system("clear")
    print(f"Espaços vazios na sua lista {50 - len(games)}")
    name = input("Nome do game: ")
    year = int(input("Ano de lançamento: "))
    price = float(input("Preço do game: "))
    game = {"name": name, "year": year, "price": price}
    games.append(game)
    os.system("clear")
    print("Game cadastrado com sucesso!")

def search_games():
    os.system("clear")

    if not games:
        return print("Lista de games vazia...")    

    name = input("Nome do game: ")
    len_list = len(games)
    found_game = False
    for game_index in range(len_list):
        get_game = games[game_index]
        if get_game["name"].lower() == name.lower():
            found_game = True
            print(f"Nome: {get_game['name']}")
            print(f"Ano de lançamento: {get_game['year']}")
            print(f"Preço: R${get_game['price']}")
    if not found_game:
        print("Game não encontrado." )

def games_list():
    os.system("clear")

    if not games:
        return print("Lista de games vazia...")

    len_list = len(games)
    print("Todos os games cadastrados:")
    for game_index in range(len_list):
        get_game = games[game_index]
        print(f"Nome: {get_game['name']}")
        print(f"Ano de lançamento: {get_game['year']}")
        print(f"Preço: R${get_game['price']}\n")
        print()

def find_interval_games():
    os.system("clear")

    if not games:
        return print("Lista de games vazia...")
    
    len_list = len(games)
    print(f"Tamanho da sua lista de games: {len_list}")
    start_index = int(input("Índice inicial: "))
    end_index = int(input("Índice final: "))
    print()

    if start_index >= 0 and end_index < len_list and start_index <= end_index:
        print("Trecho da lista: ")
        print()
        for game_index in range(start_index, end_index + 1):
            get_game = games[game_index]
            print(f"Nome: {get_game['name']}")
            print(f"Ano de lançamento: {get_game['year']}")
            print(f"Preço: R${get_game['price']}")
            print()
    else:
        print(f"Intervalo inválido.")
        print(f"Tamanho da sua lista de games: {len_list}")

def remove_game_to_list():
    os.system("clear")
    
    if not games:
        return print("Lista de games vazia...")

    game_name = input("Digite o nome do game a remover: ")
    len_list = len(games)
    
    for game_index in range(len_list):
        current_game = games[game_index]
        if current_game["name"].lower() == game_name.lower():
            games.remove(current_game)
            print(f"Game removido com sucesso: {current_game}")
            return
    print("Game não encontrado.")

def update_game_to_list():
    os.system("clear")
    
    if not games:
        return print("Lista de games vazia...")

    game_name = input("Digite o nome do game a atualizar: ")
    len_list = len(games)
    
    for game_index in range(len_list):
        current_game = games[game_index]
        if current_game["name"].lower() == game_name.lower():

            print(update_list)
            input_update = input("Campo que deseja Atualizar: ")
            
            if input_update == "1":
                current_game["name"] = input("Novo nome do game: ")
                print(f"Game atualizado com sucesso: {current_game}")
                return
            
            if input_update == "2":
                current_game["year"] = int(input("Novo ano de lançamento do game: "))
                print(f"Game atualizado com sucesso: {current_game}")
                return
            
            if input_update == "3":
                current_game["price"] = float(input("Novo preço do game: "))
                print(f"Game atualizado com sucesso: {current_game}")
                return
            
            return print("Opção inválida.")
            
    print("Game não encontrado.")

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
        try:
            remove_game_to_list()
        except Exception as e:
            print("Você inseriu dados inválidos! Por favor, tente novamente...")
            print(e)
            continue  

    if option == "6":
        try:
            update_game_to_list()
        except Exception as e:
            print("Você inseriu dados inválidos! Por favor, tente novamente...")
            print(e)         

    if option == "7":
        os.system("clear")
        kill_programing = True
        print("Saindo do sistema...")