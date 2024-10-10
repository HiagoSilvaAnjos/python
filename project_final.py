import os
from colorama import init, Fore, Style
init()

games = []
kill_programing = False
menu_list = """
    MENU DE OPÇÕES:
    1. Inserir um novo game
    2. Buscar um game pelo nome
    3. Imprimir todos os games cadastrados
    4. Imprimir um trecho específico da lista de games
    5. Remover game de sua lista
    6. Sair do sistema
"""

def handle_add_game():
    os.system("clear")
    name = input(Fore.YELLOW + "Nome do game: " + Style.RESET_ALL)
    year = int(input(Fore.YELLOW + "Ano de lançamento: " + Style.RESET_ALL))
    price = float(input(Fore.YELLOW + "Preço do game: " + Style.RESET_ALL))
    game = {"name": name, "year": year, "price": price}
    games.append(game)
    os.system("clear")
    print(Fore.GREEN + "Game cadastrado com sucesso!" + Style.RESET_ALL)

def search_games():
    os.system("clear")

    if not games:
        return print(Fore.RED + "Lista de games vazia..." + Style.RESET_ALL)    

    name = input(Fore.YELLOW + "Nome do game: " + Style.RESET_ALL)
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
        print(Fore.RED + "Game não encontrado." + Style.RESET_ALL )

def games_list():
    os.system("clear")

    if not games:
        return print(Fore.RED + "Lista de games vazia..." + Style.RESET_ALL)

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

    if not games:
        return print(Fore.RED + "Lista de games vazia..." + Style.RESET_ALL)
    
    start_index = int(input(Fore.YELLOW + "Índice inicial: " + Style.RESET_ALL))
    end_index = int(input(Fore.YELLOW + "Índice final: " + Style.RESET_ALL))
    len_list = len(games)

    if start_index >= 0 and end_index < len_list and start_index <= end_index:
        print(Fore.GREEN + "Trecho da lista: " + Style.RESET_ALL)
        for game_index in range(start_index, end_index + 1):
            get_game = games[game_index]
            print(f"Nome: {get_game['name']}")
            print(f"Ano de lançamento: {get_game['year']}")
            print(f"Preço: R${get_game['price']}")
            print()
    else:
        print(Fore.RED +  "Intervalo inválido." + Style.RESET_ALL)

def remove_game_to_list():
    os.system("clear")
    
    if not games:
        return print(Fore.RED + "Lista de games vazia..." + Style.RESET_ALL)

    game_name = input(Fore.YELLOW + "Digite o nome do game a remover: " + Style.RESET_ALL)
    len_list = len(games)
    
    for game_index in range(len_list):
        current_game = games[game_index]
        if current_game["name"].lower() == game_name.lower():
            games.remove(current_game)
            print(Fore.GREEN + f"Game removido com sucesso: {current_game}" + Style.RESET_ALL)
            return
    print(Fore.RED + "Game não encontrado." + Style.RESET_ALL)

while not kill_programing:
    print(Fore.CYAN + menu_list + Style.RESET_ALL)
    option = input(Fore.YELLOW + "Escolha uma opção: " + Style.RESET_ALL)

    if option == "1":
        if len(games) >= 50:
            print(Fore.RED + "Limite de jogos atingido! Não é possível cadastrar mais." + Style.RESET_ALL)
            continue
        try:
            handle_add_game()
        except Exception as e:
            print(Fore.RED + "Você inseriu dados inválidos! Por favor, tente novamente..." + Style.RESET_ALL)
            continue
       
    if option == "2":
        try:
            search_games()
        except Exception as e:
            print(Fore.RED + "Falha ao buscar game! Por favor, tente novamente..." + Style.RESET_ALL)
            continue

    if option == "3":
        try:
            games_list()
        except Exception as e:
            print(Fore.RED + "Falha ao carregar games! Por favor, tente novamente..." + Style.RESET_ALL)
            continue

    if option == "4":
        try:
            find_interval_games()
        except Exception as e:
            print(Fore.RED + "Você inseriu dados inválidos! Por favor, tente novamente..." + Style.RESET_ALL)
            continue        

    if option == "5":
        try:
            remove_game_to_list()
        except Exception as e:
            print(Fore.RED + "Você inseriu dados inválidos! Por favor, tente novamente..." + Style.RESET_ALL)
            print(e)
            continue           

    if option == "6":
        os.system("clear")
        kill_programing = True
        print(Fore.BLUE + "Saindo do sistema..." + Style.RESET_ALL)