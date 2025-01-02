# Inicializando as matrizes 3x3
matriz = [[0, 0, 0], 
          [0, 0, 0], 
          [0, 0, 0]]


# Entrada de dados para a Matriz A e B
for linhas in range(0, 3):
    for colunas in range(0, 3):
        numero = int(input(f"[MATRIZ A] Digite o número para a posição [{linhas},{colunas}]: "))
        matriz[linhas][colunas] = numero

for linhas in range(0,3):
    for colunas in range(0,3):
        print(matriz[linhas][colunas], end = '|')
    print()

for linhas in matriz:

    if linhas[1] == 0 and linhas[2] == 0:
        print(f'Linha {matriz.index(linhas)+1} possui dois zeros.')