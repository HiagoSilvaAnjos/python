#TODO: 
# 4. Crie um subprograma recursivo que receba um número inteiro N e imprima todos os 
# números naturais de 0 até N em ordem crescente.
#  Entradas:
#  Um número inteiro
#  Saídas:
#  Uma sequência de números naturais de 0 até N
#  Exemplo de Entradas:
#  15
#  Exemplo de Saída:
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

def print_naturals(n, current=0):
    if current > n:  # Caso base: quando o número atual excede N, a recursão para
        return
    print(current, end=" ")  # Imprime o número atual
    print_naturals(n, current + 1)  # Chamada recursiva para o próximo número

# Exemplo de uso
n = 15
print_naturals(n)
