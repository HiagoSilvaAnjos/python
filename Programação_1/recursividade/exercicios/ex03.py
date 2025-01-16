#TODO: 3. Crie uma função recursiva que retorne a soma dos elementos de um vetor de inteiros.

def sum_vector(vetor):
    if not vetor:  # Caso base: vetor vazio
        return 0
    return vetor[0] + sum_vector(vetor[1:])  # Chamada recursiva com fatiamento (1 + (2 + (3 + (4 + 5)))) == 15

vetor = [1, 2, 3, 4, 5]
print(sum_vector(vetor))  # Saída: 15   

(
    # Recursão
    # vetor[0] + sum_vector(vetor[1:])
    # 1 + sum_vector([2, 3, 4, 5])
    # 2 + sum_vector([3, 4, 5])
    # 3 + sum_vector([4, 5])
    # 4 + sum_vector([5])
    # 5 + sum_vector([])  # Vetor vazio retorna 0

    # 5 + 0 = 5
    # 4 + 5 = 9
    # 3 + 9 = 12
    # 2 + 12 = 14
    # 1 + 14 = 15

    (1 + (2 + (3 + (4 + 5))))  # 15
)
