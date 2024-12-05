# 7. Ler 2 vetores X e Y de 10 elementos cada um. Intercalar os elementos desses 2 vetores
# formando assim, um novo vetor R de 20 elementos, onde nas posições pares de R (0, 2, 4,
# ..., 8) estejam os elementos de X e nas posições ímpares (1, 3, ..., 9) os elementos de Y.
# Após a geração completa do vetor R, escreva-o.

import random
list_01 = []
list_02 = []
list_intercalada = []

for i in range(10):
    num_x = random.randint(0, 10)
    num_y = random.randint(0, 10)
    list_01.append(num_x)
    list_02.append(num_y)


for i in range(10):
    list_intercalada.append(list_01[i])
    list_intercalada.append(list_02[i])

print(list_01)
print(list_02)
print(list_intercalada)
