import pickle
compras=[ ]
tamanho=int(input("Quantos produtos deseja comprar "))
for i in range (tamanho):
    compras.append({})
    compras[i]["produto"]=input(f"Digite o nome do produto {i + 1}: ")
    compras[i]["quantidade"]=int(input("Quantos itens do produto: "))

with open("/workspaces/python/Programação_1/arquivo_binario/compras.txt", "w") as file:
    for item in compras:
        file.write(f"produto: {item["produto"]}\nquantidade:{str(item["quantidade"])}\n\n")
        

#gravar a lista de compras
arquivo="/workspaces/python/Programação_1/arquivo_binario/compras_binario"
with open (arquivo,"wb") as arq:
    pickle.dump(compras,arq)

#ler a lista de compras
compras=[ ]
with open ("/workspaces/python/Programação_1/arquivo_binario/compras_binario", "rb") as arq:
    compras = pickle.load(arq)
    print(compras)