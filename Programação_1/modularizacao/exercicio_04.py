def calculateFatorial(value):
    if value < 0:
        raise ValueError("O fatorial não é definido para números negativos.")
    fatorial = 1
    for i in range(1, value + 1):
        fatorial *= i
    return fatorial

try:
    number = int(input("Digite um número para calcular fatorial: "))
    operator = input("Digite o operador (+, -, *, /): ")
    number_02 = int(input("Digite um segundo número para calcular fatorial: "))
    
    number_fatorial = calculateFatorial(number)
    number_02_fatorial = calculateFatorial(number_02)
    
    if operator == "+":
        operation_result = number_fatorial + number_02_fatorial
    elif operator == "-":
        operation_result = number_fatorial - number_02_fatorial
    elif operator == "*":
        operation_result = number_fatorial * number_02_fatorial
    elif operator == "/":
        if number_02_fatorial == 0:
            operation_result = None
            raise ValueError("Erro: Divisão por zero!")
        else:
            operation_result = number_fatorial / number_02_fatorial
    else:
        operation_result = None
        raise ValueError("Operador inválido!")
    

    print(f"\nFatorial de {number}: {number_fatorial}")
    print(f"Fatorial de {number_02}: {number_02_fatorial}")

    if operation_result is not None:
        print(f"{number_fatorial} {operator} {number_02_fatorial} = {operation_result}")
except ValueError as e:
    print(f"Erro: {e}")
