# RECURSIVIDADE

# Recursividade é uma técnica de programação onde uma função chama a si mesma para resolver um problema. Em Python, ela é usada para resolver problemas que podem ser divididos em subproblemas menores, com base no conceito de dividir para conquistar.

#FIXME: Estrutura Básica de uma Função Recursiva
# Uma função recursiva deve possuir dois elementos fundamentais:

# Caso base: Condição que interrompe a recursão, evitando chamadas infinitas.
# Chamada recursiva: Chamada da própria função com um parâmetro modificado, movendo o problema em direção ao caso base.
# Exemplo Simples: Fatorial
# O cálculo do fatorial de um número é um exemplo clássico de recursividade. 

def fatorial(n):
    if n == 0:  # Caso base
        return 1
    else:
        return n * fatorial(n - 1)  # Chamada recursiva

print(fatorial(5))  # Saída: 120

#FIXME: Como Funciona?
# O caso base interrompe a recursão quando n é igual a 0.
# Para valores maiores que 0, a função continua chamando a si mesma com n - 1, até alcançar o caso base.

#FIXME: Cuidados ao Usar Recursividade
# Pilha de chamadas: Cada chamada recursiva consome memória, pois é armazenada na pilha. Funções muito profundas podem gerar o erro RecursionError em Python.
# Eficiência: Em alguns casos, uma abordagem iterativa pode ser mais eficiente e consumir menos recursos.

#FIXME: USO COMUM:
# Recursividade é amplamente utilizada em algoritmos de:
# Estruturas de dados (ex.: árvores e grafos)
# Busca e ordenação
# Problemas matemáticos como Fibonacci, fatorial, e números combinatórios.