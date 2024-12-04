numbers = []
kill_programing = False
max_number = 0
min_number = 0

while not kill_programing:
    number_input = int(input("enter a number (negative to exit): "))

    if number_input < 0:
        print("Your enter number negative!!, exiting...")
        kill_programing = True
    else:
        numbers.append(number_input)

max_number = numbers[0]
min_number = numbers[0]

for i in range(len(numbers)):
    if numbers[i] > max_number:
        max_number = numbers[i]
    
    if numbers[i] < min_number:
        min_number = numbers[i]

print(f"Menor: {min_number}")
print(f"Maior: {max_number}")