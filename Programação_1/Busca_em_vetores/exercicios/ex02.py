# Dado um vetor com elementos ordenados, elaborar um programa para realizar a busca. Utilizar para isso: busca 
# sequencial e binária.

#  Entradas:
#  1. A quantidade de números que devem ser lidos,
#  2. Vários números (inteiros, em ordem crescente, pode haver repetição de números),
#  3. um número a ser procurado.

#  Saídas:
#  1. A posição do número procurado no vetor,
#  2. O número de comparações necessárias na busca sequencial,
#  3. O número de comparações necessárias na busca binária.

#  O programa deve indicar que não encontrou o elemento procurado usando -1 como posição do elemento.

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

def busca_binaria(vetor_list, value_search):
    start = 0
    finish = len(vetor_list) - 1
    counter_search = 0

    while start <= finish:
        meio = (start + finish) // 2
        counter_search += 1 

        if vetor_list[meio] == value_search:
            return True, meio, counter_search
        elif value_search < vetor_list[meio]:
            finish = meio - 1
        else:
            start = meio + 1

    return False, -1, counter_search  

def busca_sequencial(vetor_list, value_search):
    counter_search = 0

    for indice in range(len(vetor_list)):
        counter_search += 1 
        if vetor_list[indice] == value_search:
            return True, indice, counter_search  

    return False, -1, counter_search  

def main():
    vetor_list = obter_lista()
    if vetor_list is None:
        return

    try:
        value_search = int(input("Digite o valor a ser buscado: "))

        found_binaria, indice_binaria, comparacoes_binaria = busca_binaria(vetor_list, value_search)
        found_sequencial, indice_sequencial, comparacoes_sequencial = busca_sequencial(vetor_list, value_search)

        if found_binaria and found_sequencial:
            indice = indice_sequencial if found_sequencial else indice_binaria
            print(f"Valor encontrado no índice: {indice}")
            print(f"Comparações na busca sequencial: {comparacoes_sequencial}")
            print(f"Comparações na busca binária: {comparacoes_binaria}")
        else:
            print(-1)

    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

main()
