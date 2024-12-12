# Enunciado 3. Escreva uma função que encontra o maior elemento de um vetor de 5 inteiros.

# Entradas:

# Cinco números inteiros.
# Saídas:

# O maior dos cinco elementos.
# Exemplo de entradas:

# 12 3 50 20 2

# Exemplo de saídas:

# 50

#FIXME: este código contém erros
# lista=[]
# for i in range (5):
# 	n=int(input())
# 	lista.append(n)

# maior=acharMaior(lista)


# def acharMaior(lista):
# 	maior=lista[0]
# 	for i in range (1,len(lista)):
# 		if lista[i] > maior:
# 			maior=lista[i]

#FIXME: correção

lista=[]
def acharMaior(lista):
	max_value=lista[0]
	for i in range (len(lista)):
		if lista[i] > max_value:
			max_value=lista[i]
	return max_value

for i in range (5):
	number_input=int(input("Digite um número para adicionar a lista: "))
	lista.append(number_input)

maior_value_in_to_list=acharMaior(lista)
print(maior_value_in_to_list)
