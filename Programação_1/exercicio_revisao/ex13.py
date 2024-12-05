import random 
# 3. Escreva um programa que leia dois vetores de 10 posições cada um. Crie um terceiro que
# será preenchido com o resultado da soma dos elementos dos dois vetores. Mostre o vetor
# resultante. Use random.randint.

list_01 = []
list_02 = []
list_sum = []
sum = 0

for i in range(10):
    num_random_01 = random.randint(1, 100)
    num_random_02= random.randint(1, 100)

    list_01.append(num_random_01)
    list_02.append(num_random_02)

    sum += list_01[i] + list_02[i]

list_sum.append(sum)

print("Vetor 1:", list_01)
print("Vetor 2:", list_02)
print("Vetor soma:", list_sum)
