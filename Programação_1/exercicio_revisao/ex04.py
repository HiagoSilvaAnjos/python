import random

# Inicializando os vetores
vetor_a = []
vetor_b = []

# Gerando números aleatórios para o vetor A e calculando o fatorial para o vetor B
for i in range(5):
    numero_aleatorio = random.randint(1, 10)  # Gerando números aleatórios para o vetor A
    vetor_a.append(numero_aleatorio)
    
    fatorial = 1
    for j in range(2, numero_aleatorio + 1):  # Calculando o fatorial manualmente
        fatorial *= j
    
    vetor_b.append(fatorial)

# Exibindo os resultados
print("Vetor A:", vetor_a)
print("Vetor B (fatoriais):", vetor_b)
