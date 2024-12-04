# 5. Crie um vetor para guardar 5 números inteiros. Em seguida, armazene em outro vetor a
# raíz quadrada de cada elemento do primeiro vetor. Use sqrt().

import math
import random

list_numbers = []
list_raizes = []

for i in range(5):
    
    number_random = random.randint(-100, 100)

    try:
        raiz = math.sqrt(number_random)

        list_numbers.append(number_random)
        list_raizes.append(raiz)
    except:
        list_numbers.append(number_random)
        list_raizes.append(0)


print(list_numbers)
print(list_raizes)