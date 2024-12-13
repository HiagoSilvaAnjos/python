# Problema 1: Acredita-se que a partir de qualquer número positivo é possível criar uma sequência de números que termina em 1 da seguinte forma:

# Se o número for par, o próximo número da sequência será sua metade.
# Se for impar, o próximo será três vezes o número mais um.
# Faça um programa que leia um número positivo, escreva essa sequência de números até o valor 1 e a quantidade de números da sequência (passada por referência para o programa principal). Os valores da sequência devem ser escritos num subprograma. A quantidade de números gerados deve ser escrita no programa principal.

# O planejamento do subprograma e seus parâmetros é parte importante da avaliação neste problema.

# Entradas:

# Um número inteiro positivo.
# Saídas:

# Uma sequência de números conforme as regras acima.
# A quantidade de números da sequência.
# Exemplo de Entrada:

# 13

# Exemplo de Saída:

# 13 40 20 10 5 16 8 4 2 1

# 10

def generate_sequence(number, quantity_interations_number):
    sequence = []
    while number != 1:
        sequence.append(number)
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
    sequence.append(1)
    quantity_interations_number[0] = len(sequence)
    return sequence

number_input = int(input("Digite um número positivo inteiro: "))
if number_input <= 0:
    print("Por favor! Digite apenas números positivos inteiros")
else:
    quantity_interations_number = [0]
    sequence = generate_sequence(number_input, quantity_interations_number)
    for i in sequence: print(i, end=" ")
    print(f"Quantidade de números na sequencia: {quantity_interations_number}")
