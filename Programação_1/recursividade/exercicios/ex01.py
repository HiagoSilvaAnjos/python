#TODO: 1. Faça uma função recursiva para somar os números de 1 até n.

def sum_numbers(n):
    if n == 1:  # Caso base
        return 1
    print(f"valor de n:{n}")
    return n + sum_numbers(n - 1)  # Chamada recursiva (4 + (3 + (2 + 1)) = 10

print(sum_numbers(4))  # Saída: 10

    
    