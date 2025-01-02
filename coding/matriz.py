# Inicializando as matrizes 3x3
matriz = [[0, 0, 0], 
          [0, 0, 0], 
          [0, 0, 0]]

matriz2 = [[0, 0, 0],
           [0 ,0, 0], 
           [0, 0, 0]]

# Entrada de dados para a Matriz A e B
for linhas in range(0, 3):
    for colunas in range(0, 3):
        numero = int(input(f"[MATRIZ A] Digite o número para a posição [{linhas},{colunas}]: "))
        matriz[linhas][colunas] = numero

for linhas in range(0, 3):
    for colunas in range(0, 3):
        numero = int(input(f"[MATRIZ B] Digite o número para a posição [{linhas},{colunas}]: "))
        matriz2[linhas][colunas] = numero

################################################################
# Exibindo as matrizes
print("\nMatriz A:")
for linhas in range(0, 3): 
    for colunas in range(0, 3):
        print(matriz[linhas][colunas], end=" | ")
    print()

print("\nMatriz B:")
for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(matriz2[linhas][colunas], end=" | ")
    print()

################################################################
# Somando as matrizes
soma = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3): 
    for j in range(3): 
        soma[i][j] = matriz[i][j] + matriz2[i][j]

# Exibindo o resultado da soma
print("\nResultado da Soma:")
for linha in soma:
    for num in linha:
        print(num, end=" | ")
    print()

################################################################
# Multiplicação de matrizes 3x3
resultado_mult = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3): 
    for j in range(3): 
        for k in range(3): 
            resultado_mult[i][j] += matriz[i][k] * matriz2[k][j]

# Exibindo o resultado da multiplicação 3x3
print("\nResultado da Multiplicação 3x3:")
for linha in resultado_mult:
    for num in linha:
        print(num, end=" | ")
    print()

################################################################
# Extraindo a diagonal principal da matriz A
diagonal_principal = []
for i in range(3):
    diagonal_principal.append(matriz[i][i])

# Exibindo a diagonal principal
print("\nDiagonal Principal da Matriz A:")
for num in diagonal_principal:
    print(num, end=" | ")
print()

################################################################
# Multiplicação de matrizes 3x2
# Exemplo de matriz B (3x2)
matriz2_3x2 = [[0, 0], 
               [0, 0], 
               [0, 0]]

for linhas in range(0, 3):
    for colunas in range(0, 2):
        numero = int(input(f"[MATRIZ B 3x2] Digite o número para a posição [{linhas},{colunas}]: "))
        matriz2_3x2[linhas][colunas] = numero

for linha in matriz2_3x2:
    for coluna in linha:
        print(coluna, end=" | ")
    print()

resultado_mult_3x2 = [[0 for _ in range(2)] for _ in range(3)] # Resultado será 3x2

for i in range(3): 
    for j in range(2): 
        for k in range(3): 
            resultado_mult_3x2[i][j] += matriz[i][k] * matriz2_3x2[k][j]

# Exibindo o resultado da multiplicação 3x2
print("\nResultado da Multiplicação 3x2:")
for linha in resultado_mult_3x2:
    for num in linha:
        print(num, end=" | ")
    print()

################################################################
# Tentativa de extrair a "diagonal" da matriz multiplicada 3x2
# Aqui, a diagonal só pode existir até o segundo elemento [0,0] e [1,1]
print("\nDiagonal da Matriz Multiplicada (até onde possível):")
for i in range(min(2, len(resultado_mult_3x2))):
    print(resultado_mult_3x2[i][i], end=" | ")
print()
