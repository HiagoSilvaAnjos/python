# 1. Faça um programa que leia uma sequência de números positivos ou nulos. O final desta
# sequência será indicado por um número negativo qualquer. Após isso, imprima: o menor
# valor, segundo menor valor, o maior valor e o segundo maior valor. Assuma que a sequência
# tem pelo menos dois números e que não há elementos repetidos.
# Entradas:
# • int n - Números que o usuário irá digitar.
# Saídas:
# • Menor valor digitado (float).
# • Maior valor digitado (float).

kill_programing = False
list_numbers = []
max_number = 0
min_number = 0

while not kill_programing: 
    value_number = int(input("Digite um número positivo ou nulo: "))

    if value_number < 0:
        kill_programing = True
        continue

    list_numbers.append(value_number)

max_number = list_numbers[0]
min_number = list_numbers[0]

for current_number in list_numbers:

    if current_number > max_number:
        max_number = current_number
    
    if current_number < min_number:
        min_number = current_number


print(list_numbers)
print(min_number)
print(max_number)