# import random 
# import math

# list_01 = []
# list_02 = []

# for i in range(5):
#     num_random_01 = random.randint(-100, 100)
    
#     if(num_random_01 < 0):
#         num_random_negtive = num_random_01
#         list_01.append(num_random_negtive)
#         list_02.append(0)
#     else:
#         list_01.append(num_random_01)
#         raiz = math.sqrt(num_random_01)
#         list_02.append(raiz)


# print("Vetor 1:", list_01)
# print("Vetor 2:", list_02)

import random 
import math

list_01 = []
list_02 = []

for i in range(5):
    num_random_01 = random.randint(-100, 100)
    
    try:
        raiz = math.sqrt(num_random_01)
        list_01.append(num_random_01)
        list_02.append(raiz)
    except:
        list_01.append(num_random_01)
        list_02.append(0)


print("Vetor 1:", list_01)
print("Vetor 2:", list_02)
