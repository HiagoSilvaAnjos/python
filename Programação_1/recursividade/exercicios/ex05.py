#TODO: 5. Faça uma função recursiva para calcular a potência e retorna o valor de number elevado a n. 

def power(base, exponent):
    if exponent == 0:  # Caso base: qualquer número elevado a 0 é 1
        return 1
    return base * power(base, exponent - 1)  # Chamada recursiva (2 * (2 * (2 * (2 * (2 * 1))))) == 32

# Exemplo de uso
base = 2
exponent = 5
print(power(base, exponent))  # Saída: 32 (2^5 = 32)

