#TODO: 1. Faça uma função recursiva para somar os números de 1 até n.

def sum_numbers(n):
    if n == 1:  # Caso base
        return 1
    print(f"valor de n:{n}")
    return n + sum_numbers(n - 1)  # Chamada recursiva (4 + (3 + (2 + 1)) = 10

print(sum_numbers(4))  # Saída: 10

(
    # Recursão 
    # 4 + sum_numbers(4-1 = 3)
    # 3 + sum_numbers(3-1 = 2)
    # 2 + sum_numbers(2-1 = 1)
    # 1 

    # 4 + 6 = 10
    # 3 + 3 = 6
    # 2 + 1 = 3
    # 1

    (4 + (3 + (2 + 1) )) # 10
)
    