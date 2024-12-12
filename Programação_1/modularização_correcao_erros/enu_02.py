# Enunciado 2: Faça um programa para receber nove números inteiros positivos, armazená-los em um vetor, calcular e exibir no dispositivo de saída padrão aqueles números que são primos e suas respectivas posições no vetor. Se nenhum número primo for fornecido, nenhuma mensagem precisará ser exibida. Utilize um subprograma para verificar se um número é primo. Entradas:

# Nove números inteiros positivos a serem armazenados em um vetor. Saídas:
# Sequência de números primos e suas respectivas posições (índices no vetor).
# Obs.: Aqueles números que forem primos e suas respectivas posições deverão ser exibidos aos pares.

# Exemplo de entrada:

# 7 13 49 23 6 21 78 98

# Exemplo de saída:

# 7 0

# 13 1

# 23 3

# 3 8

#FIXME: este código contém erros
# def verPrimo (n):
# 	contador=0
# 	for i in range (1,n+1):
# 		if n/i==0:
# 			contador+=1
# 	if contador==n:
# 		return True
# 	else:
# 		return False

# #entrada de dados
# lista=[]
# for i in range (len(lista)):
# 	n=int(input())
# 	lista.append(n)


# for i in range (9):
# 	if verPrimo (i)==True:
# 		print (lista[i], i)

#FIXME: correção
def verPrimo (number_list):
    if number_list <= 2:
        return False
	
    contador_divisoes = 0

    for i in range (1 ,number_list+1, 1):
        if number_list % i== 0:
            contador_divisoes+=1
    return contador_divisoes == 2

#entrada de dados
lista=[]
for i in range (3):
	number=int(input("Digite um número inteiro positivo: "))
	lista.append(number)


for i in range (3):
	if verPrimo (lista[i])==True:
		print (f"número primo: {lista[i]} | indice: {i}")
