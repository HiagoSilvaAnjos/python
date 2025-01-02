list_numbers = []

min_value = 0
max_value = 0 
min_index = 0
max_index = 0

for i in range(1, 6, 1):

    value = int(input("Enter a number: "))
    list_numbers.append(value)

    min_value = list_numbers[0]
    max_value = list_numbers[0] 

 
for i in range(len(list_numbers)):

    if list_numbers[i] < min_value:
        min_value = list_numbers[i]
        min_index = i
    if list_numbers[i] > max_value:
        max_value = list_numbers[i]
        max_index = i

print(f"Menor valor: {min_value}, Índice: {min_index}")
print(f"Maior valor: {max_value}, Índice: {max_index}")
