# Enunciado 1: Faça um programa que receba um número inteiro n e imprima uma pirâmide contendo n linhas e em cada uma deve conter uma sequência numérica até o número que represente o valor da linha. O subprograma deverá imprimir apenas uma linha por vez. Ou seja, é necessário que o subprograma seja chamada toda vez que for imprimir uma nova linha. Entradas:

# Número inteiro informando a quantidade de linhas
# Saídas:

# n linhas contendo cada uma uma sequência numérica correspondente ao valor da linha.
# Exemplo de Entrada: 5

# Exemplo de Saída:

# 1

# 1 2

# 1 2 3

# 1 2 3 4

# 1 2 3 4 5

#FIXME: este código contém erros
# def imprime (n):
# 	for i in range (n):
# 		print(i, end=" ")
# 	# print(n)

# linhas=int(input())
# for i in range (1, linhas, linhas + 1):
#   imprime(i)

#FIXME: correção
def imprime (number):
	for i in range (1, number + 1, 1):
		print(i, end=" ")
	print()

linhas=int(input("Digite a qauntidade de linhas: "))
for i in range (1, linhas + 1, 1):
  imprime(i)