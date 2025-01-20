vetor_list=[3,70,20,15,88,49]

try:
    value_input = int(input("Informe um valor para buscar: "))

    for indice in range (len(vetor_list)):
        if vetor_list[indice]== value_input:
            print(f"valor: {vetor_list[indice]} | indice: {indice}")        
except:
    print("Input inválido")

vetor_list=[3,70,20,15,88,49]
indice = 0