#TODO: 5. Faça uma função recursiva para calcular a potência e retorna o valor de x elevado a n. 

def power(x, n):
    if n == 0:  # Caso base: qualquer número elevado a 0 é 1
        return 1
    return x * power(x, n - 1)  # Chamada recursiva: reduz n e multiplica x

# Exemplo de uso
x = 2
n = 5
print(power(x, n))  # Saída: 32 (2^5 = 32)
