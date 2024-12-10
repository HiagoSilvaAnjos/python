# Calcular Fatorial com Def
list_numbers_fatorial = []

def calculateFatorial (value):
        fatorial = 1
        for i in range(1, value + 1): fatorial *= i
        return fatorial

for i in range(5):
    try:
        number = int(input("Digite um número para calcular fatorial: "))
        fatorial_number = calculateFatorial(number)
        list_numbers_fatorial.append(fatorial_number)
    except:
        print("Error: Valor inválido")

print(list_numbers_fatorial)