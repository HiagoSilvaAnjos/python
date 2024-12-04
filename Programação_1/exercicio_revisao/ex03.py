import random

list_01 = []
list_02 = []
sum_lists = []

for i in range(10):

    number_random_01 = random.randint(0, 10)
    list_01.append(number_random_01)
    number_random_02 = random.randint(0, 10)
    list_02.append(number_random_02)

    sum_lists.append(list_01[i] + list_02[i])

print(list_01)
print(list_02)
print(sum_lists)