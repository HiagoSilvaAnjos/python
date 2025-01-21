def buscaRecursiva(vetor_list, item_buscado, inicio, fim):
	if inicio <= fim:
		meio = (inicio + fim) // 2
		if vetor_list[meio] == item_buscado:
			return (True, item_buscado, meio)
		elif item_buscado < vetor_list[meio]:
			return buscaRecursiva(vetor_list, item_buscado, inicio, meio - 1)
		else:
			return buscaRecursiva(vetor_list, item_buscado, meio + 1, fim)
	else:
		return False

vetor_list = [3, 15, 70, 80, 150, 461]
print(buscaRecursiva(vetor_list, 70, 0, (len(vetor_list) - 1)))

# v = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]