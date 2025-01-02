"""
Exercício
TODO: Peça ao usuário para digitar seu nome
TODO: Peça ao usuário para digitar sua idade
TODO: Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
TODO: Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

name_user = input("Digit you name: ")
age_user = input("Digit you age: ")

if age_user == '' or age_user == '':
    print("Desculpe, você deixou campos vazios.")
else:
    nome_invertido = name_user[::-1]
    has_space = " " in name_user

    print(f"Seu nome é {name_user}")
    print(f"Seu nome invertido é {nome_invertido}")
    print(f"Seu nome contém espaços? {has_space}")
    print(f"Seu nome tem {len(name_user)} letras")
    print(f"A primeira letra do seu nome é {name_user[0]}")
    print(f"A última letra do seu nome é {name_user[-1]}")