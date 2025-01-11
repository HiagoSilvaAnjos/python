#Hiago Silva - Questão 01

list_atletas = []
list_atletas_acima_peso = []
sum_pesos = 0
media_pesos = 0

try:
    quantity_atletas = int(input("Digite um número N que represente a quantidade de atletas: "))

    for i in range(quantity_atletas): 
            input_peso = float(input("Digite o peso de cada atleta: "))
            list_atletas.append((i, input_peso))
            sum_pesos += input_peso
       
            list_atletas.append((i, 0))

    media_pesos = sum_pesos / quantity_atletas

    for atleta in list_atletas:
        if atleta[1] >= media_pesos:
            list_atletas_acima_peso.append(atleta)

    print("Atletas acima do peso: ")
    for atleta_acima_peso in list_atletas_acima_peso:
        print(f"indice: {atleta_acima_peso[0]}, com o peso: {atleta_acima_peso[1]}")
except:
    print("Dado inválido!")
