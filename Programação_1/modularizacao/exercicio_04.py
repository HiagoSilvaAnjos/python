# Calcular Fatorial com Def
def calculateFatorial (value):
        fatorial = 1
        for i in range(1, value + 1): fatorial *= i
        return fatorial

number = int(input("Digite um número para calcular fatorial: "))
operator = input("Digite o operador: ")
number_02 = int(input("Digite um segundo número para calcular fatorial: "))

number_fatorial = calculateFatorial(number)
number_02_fatorial = calculateFatorial(number_02)


resultado = number_02_fatorial

print(number_fatorial)
print(number_02_fatorial)
print(f"number_01: {number_fatorial} {operator} {number_02_fatorial} = {resultado}")