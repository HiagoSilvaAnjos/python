"""

        FIXME: Calculadora com while

"""

template_calc = """
    ==> Calculadora Python <== 

    Options: 
    "+" ==> Sum;
    "-" ==> Sub;
    "*" ==> Multiply;
    "/" ==> Divide;

"""

while True:

    print(template_calc)
    operator = input("Enter the type of operation: ")
    number_one = input("Enter first number: ")
    number_two = input("Enter second number: ")

    numbers_validation = None
    operators_valids = "+-*/"

    try:
        convert_number_one = float(number_one)
        convert_number_two = float(number_two)
        numbers_validation = True

    except Exception as error:
        numbers_validation = None

    if(numbers_validation is None):
        print("One or both numbers are invalid!")
        continue

    if operator not in operators_valids:
        print(f"INVALID OPERATOR!")
        continue

    if len(operator) > 1:
        print(f"INVALID OPERATOR!")
        continue

    ################################################################

    print("creating your account...")

    if(operator == "+"):
        sum = convert_number_one + convert_number_two
        print(f"Opção soma: {convert_number_one} + {convert_number_two} = {sum}")
    elif(operator == "-"):
        sub = convert_number_one - convert_number_two
        print(f"Opção subtração: {convert_number_one} - {convert_number_two} = {sub}")
    elif(operator == "*"):
        multiply = convert_number_one * convert_number_two
        print(f"Opção multiplicação: {convert_number_one} * {convert_number_two} = {multiply}")
    else:
        division = convert_number_one / convert_number_two
        print(f"Opção divisão: {convert_number_one} / {convert_number_two} = {division}")

    ################################################################

    exit = input("To exit? ").lower().startswith('s')

    if exit:
        break
    else:
        continue