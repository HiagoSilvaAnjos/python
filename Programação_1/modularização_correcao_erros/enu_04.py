# Problema 1: Acredita-se que a partir de qualquer número positivo é possível criar uma sequência de números que termina em 1 da seguinte forma:

# Se o número for par, o próximo número da sequência será sua metade.
# Se for impar, o próximo será três vezes o número mais um.
# Faça um programa que leia um número positivo, escreva essa sequência de números até o valor 1 e a quantidade de números da sequência (passada por referência para o programa principal). Os valores da sequência devem ser escritos num subprograma. A quantidade de números gerados deve ser escrita no programa principal.

# O planejamento do subprograma e seus parâmetros é parte importante da avaliação neste problema.

# Entradas:

# Um número inteiro positivo.
# Saídas:

# Uma sequência de números conforme as regras acima.
# A quantidade de números da sequência.
# Exemplo de Entrada:

# 13

# Exemplo de Saída:

# 13 40 20 10 5 16 8 4 2 1

# 10

def gerar_sequencia(num, quantidade_ref):
    sequencia = []  
    while num != 1:
        sequencia.append(num)
        if num % 2 == 0:  
            num //= 2
        else:  
            num = 3 * num + 1
    sequencia.append(1)  
    quantidade_ref[0] = len(sequencia)  
    return sequencia

number_input = int(input("Digite um número positivo inteiro: "))
if number_input <= 0:
    print("Por favor, insira um número positivo!")
else:
    quantidade = [0]  
    sequencia = gerar_sequencia(number_input, quantidade)
    for i in sequencia: print(i, end=" ")
    print("Quantidade de números na sequência:", quantidade[0])
