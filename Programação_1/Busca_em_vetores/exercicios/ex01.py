#  Faça um programa que lê diversos números inteiros, ordenados, e depois realiza uma busca binária 
# nesse vetor. O programa deve contar quantas comparações foram realizadas durante a busca.

# Entradas:
#  1.  Quantidade de números a serem armazenados no vetor.
#  2.  Vários números inteiros, em ordem crescente, para armazenar no vetor.
#  3.  Número inteiro a ser buscado no vetor.

#  Saídas:
#  1.
#  O índice do elemento procurado no vetor. Caso o valor não seja encontrado deve ser impresso -1.
#  2.
#  O número de comparações realizadas entre elementos do vetor e o elemento procurado que foram 
# necessárias para encontrar o valor

def obter_lista():
    try:
        length_array = int(input("Digite a quantidade de números a serem armazenados: "))
        vetor_list = []
        
        print("Digite os números em ordem crescente:")
        for i in range(length_array):
            number_input = int(input(f"Número {i+1}: "))
            vetor_list.append(number_input)
        
        return vetor_list
    except:
        print("Entrada inválida. Digite um número inteiro.")
        return None
    
# [1, 2, 3 , 4, 5]
# 2

def busca_binaria(vetor_list, value_search):
    start = 0
    found = False
    counter_search = 0
    finish = len(vetor_list) - 1 #4 #1

    while start <= finish and not found:
        meio = (start + finish) // 2
        if vetor_list[meio] == value_search:
            found = True
            counter_search += 1
        else:
            counter_search += 1
            if value_search < vetor_list[meio]:
                finish = meio - 1
            else:
                start = meio + 1

    return found, meio, counter_search

def main():
    vetor_list = obter_lista()
    if vetor_list is None:
        return
    
    try:
        value_search = int(input("Digite o valor a ser buscado: "))
        found, meio, counter_search = busca_binaria(vetor_list, value_search)

        if found:
            print(f"Encontrado: {found} | Valor: {vetor_list[meio]} | Índice: {meio}")
            print(f"Total de buscas: {counter_search}")
        else:
            print(-1)
    except:
        print("Entrada inválida. Digite um número inteiro.")

main()