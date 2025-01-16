#TODO: 5. Faça uma função recursiva para calcular a potência e retorna o valor de number elevado a n. 

def power(base, exponent):
    if exponent == 0:  # Caso base: qualquer número elevado a 0 é 1
        return 1
    return base * power(base, exponent - 1)  # Chamada recursiva (2 * (2 * (2 * (2 * (2 * 1))))) == 32

# Exemplo de uso
base = 2
exponent = 5
print(power(base, exponent))  # Saída: 32 (2^5 = 32)

(
    # Recursão
    # base * power(base, exponent - 1)
    # 2 * power(2, 4)
    # 2 * power(2, 3) 
    # 2 * power(2, 2) 
    # 2 * power(2, 1) 
    # 2 * power(2, 0) 
    # Caso base: 1

    # 2 * 16 = 32
    # 2 * 8 = 16
    # 2 * 4 = 8
    # 2 * 2 = 4
    # 2 * 1 = 2
    # 1

    # 2 * (2 * (2 * (2 * (2 * 1)))) = 32
)

# 2^5 = 32
