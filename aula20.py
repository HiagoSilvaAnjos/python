set_value_one_input = input("Digite um número: ")
set_value_two_input = input("Digite outro número: ")

set_value_one = float(set_value_one_input)
set_value_two = float(set_value_two_input)

condition = set_value_one >= set_value_two

if condition:
    print(f"O número {set_value_one: .2f} é maior ou igual ao segundo valor, que é {set_value_two: .2f}")
else:
    print(f"O número {set_value_two: .2f} é maior ou igual ao segundo valor, que é {set_value_one: .2f}")