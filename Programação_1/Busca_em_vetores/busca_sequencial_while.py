vetor_list=[3,70,20,15,88,49]
indice = 0

try:
    value_input = int(input("Informe um valor para buscar: "))

    while indice < len(vetor_list) and vetor_list[indice] != value_input:
        indice += 1

    if indice < len(vetor_list):
        print(indice)  
    else: 
        print("Não encontrado")   
except:
    print("Input inválido")