matriz = [[0, 0, 0], 
          [0, 0, 0],
          [0, 0, 0]]

matriz2 = [[0, 0, 0],
           [0 ,0, 0],
           [0, 0, 0]]

for linhas in range(0, 3):
    for colunas in range(0, 3):
        numero = int(input(f"[MATRIZ A] Digite o número para a posição [{linhas},{colunas}]: "))
        matriz[linhas][colunas] = numero

for linhas in range(0, 3):
    for colunas in range(0, 3):
        numero = int(input(f"[MATRIZ b] Digite o número para a posição [{linhas},{colunas}]: "))
        matriz2[linhas][colunas] = numero

################################################################
#FIXME: Resultados
print()

print(f"Matriz A")
for linhas in range(0, 3): 
    for colunas in range(0, 3):
        print(matriz[linhas][colunas], end=" | ",)
    print()

print(f"Matriz B")
for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(matriz2[linhas][colunas], end=" | ",)
    print()

# Multiplicando as matrizes
resultado = [[0 for _ in range(3)] for _ in range(3)] # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                                                        
print(resultado)

for i in range(3): 
    for j in range(3): 
        for k in range(3): 
            resultado[i][j] += matriz[i][k] * matriz2[k][j]

# Exibindo o resultado da multiplicação
print("\nResultado da Multiplicação:")
for linha in resultado:
    for num in linha:
        print(num, end=" | ")
    print()  
