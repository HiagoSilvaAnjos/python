leitura="/workspaces/python/Programação_1/arquivo_binario/entrada.txt"
lista =[]
def lendo (leitura, lista):
    with open (leitura) as arq:
        items = [item.strip() for item in arq.readlines()]
        produtos = [item.split(" ") for item in items]
        #complete aqui
        for produto in produtos:
            lista.append({"produto": produto[0], "quantidade": int(produto[1])})
            #complete aqui
lendo (leitura,lista)   
for item in lista:
    print(item)

quantidade_total = 0
for produto in lista:
    quantidade_total += produto["quantidade"]
print(quantidade_total)