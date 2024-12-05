# 2. Faça um programa que preencha um vetor com dez números reais, calcule e mostre a
# quantidade de números positivos (incluindo o zero) e a soma dos números negativos desse
# vetor. Imprima os elementos do vetor começando pelo último elemento até o primeiro
# elemento.
# Entrada:
# ● Dez números reais (a serem guardados em um vetor).
# Saída:
# ● Quantidade de números positivos no vetor.
# ● Soma dos números negativos do vetor.
# ● Os elementos do vetor começando pelo último elemento até o primeiro elemento

list_numbers = []
qtd_numbers_positive = 0
sum_negative_numbers = 0

for i in range(10):
    number = float(input("Digite um número: "))
    list_numbers.append(number)

for i in range(len(list_numbers)):

    if list_numbers[i] > 0:
        qtd_numbers_positive += 1

    if list_numbers[i] < 0:
        sum_negative_numbers += list_numbers[i]

print(f"Quantidade de números positivos: {qtd_numbers_positive}")
print(f"Soma dos números negativos: {sum_negative_numbers}")
print(list_numbers[::-1])


