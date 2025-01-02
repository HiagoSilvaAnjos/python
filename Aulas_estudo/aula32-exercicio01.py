""" TODO:
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

number_input = input("Enter a number integer: ")

if number_input.isnumeric():
    number_parse_integer = int(number_input)
    check_number = number_parse_integer % 2 == 0

    if check_number:
        print("The number enter is pair")
    else:
        print("The number enter is odd")

else:
    print("Not a number integer!!!")