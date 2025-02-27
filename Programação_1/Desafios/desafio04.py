
def verPrimo (number_list):
    if number_list < 2:
        return False
	
    contador_divisoes = 0 

    for i in range (1 ,number_list+1, 1):
        if number_list % i== 0:
            contador_divisoes+=1
    return contador_divisoes == 2

number_primos = 5
contador= 0
number = 0
list_primos = []

while contador < number_primos:
    if verPrimo(number):
        list_primos.append(number)
        contador+=1
    number+=1

with open('/home/savio/Documentos/curso-python/Programação_1/Desafios/primos.txt', 'w') as file:
    for i in list_primos:
        file.write(f'{i} \n')