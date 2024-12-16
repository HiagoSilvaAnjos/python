# Faça um programa que preencha um vetor com dez números reais, calcule e mostre a
# quantidade de números positivos (incluindo o zero) e a soma dos números negativos desse
# vetor. Imprima os elementos do vetor começando pelo último elemento até o primeiro
# elemento.
# Entrada:
# ● Dez números reais (a serem guardados em um vetor).
# Saída:
# ● Quantidade de números positivos no vetor.
# ● Soma dos números negativos do vetor.
# ● Os elementos do vetor começando pelo último elemento até o primeiro elemento.]

list_values = []
quantity_positives = 0
sum_numbers_negatives = 0

for i in range(10):
    value_input = int(input("Digite 10 números reais para serem guardados em um vetor: "))
    list_values.append(value_input)

    quantity_positives += 1 if value_input >= 0 else 0        
    sum_numbers_negatives += value_input if value_input < 0 else 0          

print(list_values)
print(quantity_positives)
print(sum_numbers_negatives)
print(list_values[::-1])