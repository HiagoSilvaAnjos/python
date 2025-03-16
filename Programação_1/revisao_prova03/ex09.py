# 9) Faça um programa para gravar uma lista de palavras em um arquivo-texto. O programa
# deve ler enquanto não for digitada a palavra “fim”. A palavra fim não deve ser armazenada
# no arquivo. Não é permitido o uso de listas. Assim que uma palavra válida for digitada, ela
# deve ser armazenada no arquivo.
# O programa deve imprimir na tela quantas palavras válidas foram lidas. O nome do
# arquivo-texto deverá ser informado pelo usuário.

try:
    kill_programin = False
    input_name_file = input("Digite o nome do arquivo que deseja salvar: ")

    if len(input_name_file.strip()) == 0:
        raise Exception("nome vazio!!")

    while not kill_programin:
        try:
            input_text = input("Digite a palavra que deseja adicionar: ")

            if len(input_text.strip()) == 0:
                raise Exception("Palavra vazia!!")

            if input_text == "fim":
                kill_programin = True
                continue   

            with open(f"/workspaces/python/Programação_1/revisao_prova03/{input_name_file}.txt", "a",  encoding="utf-8") as file:
                file.write(f"{input_text}\n") 
        except FileNotFoundError :
            print("Erro ao abrir arquivo!!")

        except Exception as e:
            print(e)
except Exception as e:
    print(e)
