# 2. Faça um programa que usa busca binária para procurar um número em um vetor. O
# programa deve escrever todos os números que foram comparados ao número procurado
# (elemento central), na ordem.
# O programa deverá ler o vetor no qual a busca será realizada, este vetor já estará
# ordenado. A busca binária deverá ser implementada utilizando um módulo recursivo

# Entradas:
# 1. o número de elementos do vetor,
# 2. os elementos do vetor (números inteiros que estão em ordem crescente),
# 3. o número procurado.

# Saídas: O programa deverá escrever cada elemento do vetor comparado com o número
# procurado (elemento central), na ordem em que eles forem comparados.


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
    list_numbers_test = []

    while start <= finish:
        meio = (start + finish) // 2
        counter_search += 1 

        if vetor_list[meio] == value_search:
            list_numbers_test.append(vetor_list[meio])
            return True, meio, counter_search, list_numbers_test
        elif value_search < vetor_list[meio]:
            list_numbers_test.append(vetor_list[meio])
            finish = meio - 1
        else:
            list_numbers_test.append(vetor_list[meio])
            start = meio + 1

    return False, -1, counter_search, list_numbers_test

def main():
    vetor_list = obter_lista()
    if vetor_list is None:
        return

    try:
        value_search = int(input("Digite o valor a ser buscado: "))

        found_binaria, indice_binaria, comparacoes_binaria, comparacoes = busca_binaria(vetor_list, value_search)
        print(f"Valor encontrado: {found_binaria}, indice: {indice_binaria}, comparações: {comparacoes_binaria}")
        print(f"Números que foram pesquisados: {comparacoes}")

    except Exception as e:
        print("Entrada inválida. Digite um número inteiro.")
        print(e)

main()