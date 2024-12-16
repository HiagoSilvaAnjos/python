# 3. Escreva um programa que leia dois vetores de 10 posições cada um. Crie um terceiro que
# será preenchido com o resultado da soma dos elementos dos dois vetores. Mostre o vetor
# resultante. Use random.randint.

import random

list_values_01 = []
list_values_02 = []
sum_lists = []

for i in range(10):
    value_random_01 = random.randint(1, 100)
    value_random_02 = random.randint(1, 100)

    list_values_01.append(value_random_01)
    list_values_02.append(value_random_02)

    sum_lists.append(list_values_01[i] + list_values_02[i])

print(list_values_01)
print(list_values_02)
print(sum_lists)