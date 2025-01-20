# vetor_list=[3,70,20,15,88,49]

# try:
#     value_input = int(input("Informe um valor para buscar: "))

#     for indice in range (len(vetor_list)):
#         if vetor_list[indice]== value_input:
#             print(f"valor: {vetor_list[indice]} | indice: {indice}")        
# except:
#     print("Input inválido")

# vetor_list=[3,70,20,15,88,49]
# indice = 0

# try:
#     value_input = int(input("Informe um valor para buscar: "))

#     while indice < len(vetor_list) and vetor_list[indice] != value_input:
#         indice += 1

#     if indice < len(vetor_list):
#         print(indice)  
#     else: 
#         print("Não encontrado")   
# except:
#     print("Input inválido")

# vetor_list=[3,15,70,80,150,461]
# start = 0
# found=False

# try:
#     value_input=int(input("Digite o valor a ser buscado: "))

#     finish = len(vetor_list)-1

#     while start<=finish and not found: 

#         meio = (start + finish)//2
#         if vetor_list[meio] == value_input:
#             found=True
#         else:
#             if value_input < vetor_list[meio]:
#                 finish = meio-1
#             else:
#                 start=meio+1

#     if found:
#         print(f"Encontrado: {found} | Valor: {vetor_list[meio]} | Indice: {meio}")
#     else:
#         print(f"Não Encontrado")
# except:
#      print("Input inválido")

# def buscaRecursiva(v, item, inicio, fim):
# 	if inicio <= fim:
# 		meio = (inicio + fim) // 2
# 		if v[meio] == item:
# 			return (True, item, meio)
# 		elif item < v[meio]:
# 			return buscaRecursiva(v, item, inicio, meio - 1)
# 		else:
# 			return buscaRecursiva(v, item, meio + 1, fim)
# 	else:
# 		return False

# v = [3, 15, 70, 80, 150, 461]
# print(buscaRecursiva(v, 70, 0, (len(v) - 1)))

# v = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]

