#TODO: 2. Escreva uma função recursiva que calcule a soma dos primeiros n cubos

def sum_of_cubes(n):
    if n == 1:  # Caso base
        return 1
    return n**3 + sum_of_cubes(n - 1)  # Chamada recursiva

# Exemplo de uso
print(sum_of_cubes(4))  # Saída: 100 (1^3 + 2^3 + 3^3 + 4^3 = 100)
