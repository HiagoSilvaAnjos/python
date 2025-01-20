def buscaRecursiva(v, item, inicio, fim):
	if inicio <= fim:
		meio = (inicio + fim) // 2
		if v[meio] == item:
			return (True, item, meio)
		elif item < v[meio]:
			return buscaRecursiva(v, item, inicio, meio - 1)
		else:
			return buscaRecursiva(v, item, meio + 1, fim)
	else:
		return False

v = [3, 15, 70, 80, 150, 461]
print(buscaRecursiva(v, 70, 0, (len(v) - 1)))

v = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]