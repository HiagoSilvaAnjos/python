import pickle

path = "/workspaces/python/Programação_1/arquivo_binario/binario"

def gravar (nseila ,relativepath) :
    with open (relativepath, "wb") as file:
        pickle.dump(nseila,file)
    print("finish")
    # print(file)

numero=int(input("Digite um número para ser gravado "))
# nomeArquivo=input("Digite o nome do arquivo de saida ")
gravar(numero, path) 