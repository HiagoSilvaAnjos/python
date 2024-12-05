# 6. Uma empresa de ônibus está disponibilizando oito veículos para uma viagem para
# Aparecida do Norte no feriado de 12 de outubro. O funcionário da empresa possui em um
# papel uma tabela com uma linha e oito colunas, onde ele deve escrever o nome da pessoa
# que reservar cada ônibus.
# Obs: antes de colocar os nomes, a tabela tem a palavra "disponivel" em cada célula.
# As pessoas reservam os ônibus informando o número dele (de 0 a 7) e seu primeiro nome.
# Se o número informado não estiver reservado, o nome da pessoa é escrito na tabela, caso
# contrário, ele fica sem reserva de ônibus.
# Faça um programa que tenha um vetor para representar a tabela citada acima. O programa
# deverá receber da entrada padrão uma sequência de nomes e números de ônibus e
# preencher o vetor conforme a tabela é preenchida. O programa deverá também contabilizar
# o número de pedidos de reserva não atendidos. Por fim, o vetor e o número de pedidos não
# atendidos devem ser exibidos na saída padrão.

import os

onibus = ["disponivel"] * 8
pedidos_nao_atendidos = 0
kill_programing = False

print("Digite os nomes e números do ônibus (de 0 a 7) ou 'fim -1' para encerrar:")

while not kill_programing:
    entrada = input().strip()
    
    if entrada == "fim -1":
        kill_programing = True
        continue

    try:
        nome, numero = entrada.split()
        numero = int(numero)
    except:
        os.system("clear")  
        print("Entrada inválida! Use: <nome> <número>")
        continue

    if numero < 0 or numero > 7:
        os.system("clear")
        print("Número inválido! Insira um valor entre 0 e 7.")
        continue

    if onibus[numero] == "disponivel":
        onibus[numero] = nome
    else:
        pedidos_nao_atendidos += 1
        print("Ônibus indisponível!")

os.system("clear")
print("Tabela de Ônibus:")
print(onibus)
print("Pedidos de reserva não atendidos:", pedidos_nao_atendidos)
