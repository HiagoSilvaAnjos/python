#TODO: 3. Crie uma função recursiva que retorne a soma dos elementos de um vetor de inteiros.

def sum_vector(vetor):
    if not vetor:  # Caso base: vetor vazio
        return 0
    return vetor[0] + sum_vector(vetor[1:])  # Chamada recursiva com fatiamento (1 + (2 + (3 + (4 + 5)))) == 15

vetor = [1, 2, 3, 4, 5]
print(sum_vector(vetor))  # Saída: 15   
