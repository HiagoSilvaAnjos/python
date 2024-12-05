# Repetição e Listas
# 1. Faça um programa que leia uma sequência de números positivos ou nulos. O final desta
# sequência será indicado por um número negativo qualquer. Após isso, imprima: o menor
# valor, segundo menor valor, o maior valor e o segundo maior valor. Assuma que a sequência
# tem pelo menos dois números e que não há elementos repetidos.
# Entradas:
# • int n - Números que o usuário irá digitar.
# Saídas:
# • Menor valor digitado (float).
# • Maior valor digitado (float).

list_numbers = []

min_value = 0
max_value = 0 

kill_programing = False

while not kill_programing:
    number = float(input("Digite um número (ou -1 para encerrar): "))
    if number < 0:
        kill_programing = True
        print("Digitou -1")
    else:
        list_numbers.append(number)

for i in range(len(list_numbers)):

    min_value = list_numbers[0]
    max_value = list_numbers[0] 

    if list_numbers[i] < min_value:
        min_value = list_numbers[i]

    if list_numbers[i] > max_value:
        max_value = list_numbers[i]

print(f"O maior é {max_value}")
print(f"O menor é {min_value}")