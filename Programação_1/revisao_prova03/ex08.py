def make_piramidy(length_piramidy):
    for i in range(1, length_piramidy + 1):
        values = ""
        for index in range(1, i + 1):
            values += str(index) + " "

        try:
            with open("/workspaces/python/Programação_1/revisao_prova03/piramide.txt", "a", encoding="utf-8") as file:
                file.write(f"{values}\n")
        except Exception as e:
           print("Erro ao escrever no arquivo")
           raise Exception(e)
       

try:
    length_piramidy = int(input("Digite o tamanho da pirâmide a ser criada: "))
    make_piramidy(length_piramidy)
except ValueError:
    print("Insira apenas um número inteiro!!!")
except Exception as e:
    print(e)

