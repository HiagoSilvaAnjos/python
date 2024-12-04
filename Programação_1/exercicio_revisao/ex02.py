list_numbers = []
quantity_numbers_positives = 0
sum_numbers_negatives = 0

for i in range(10):
    try:
        number_input = float(input("Enter a number: "))
        list_numbers.append(number_input)

        quantity_numbers_positives += 1 if number_input >= 0 else 0
        sum_numbers_negatives += number_input if number_input < 0 else 0
    except:
        print("Invalid caracter")


print(list_numbers)
print(f"Quantity of numbres positives in to list: {quantity_numbers_positives}")
print(f"Sum of numbres negatives in to list: {sum_numbers_negatives}")
print(list_numbers[::-1])