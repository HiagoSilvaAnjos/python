entrada = int(input("Digite o valor inicial: "))

cem =  entrada // 100
rest_cem = entrada % 100

cinquenta = rest_cem // 50
rest_ciquenta = rest_cem % 50

vinte = rest_ciquenta // 20
rest_vinte = rest_ciquenta % 20

dez = rest_vinte // 10
rest_dez = rest_vinte % 10

cinco = rest_dez // 5
rest_cinco = rest_dez % 5

dois = rest_cinco // 2
rest_dois = rest_cinco % 2

um = rest_dois

saida = [("Notas de 100", cem), ("Notas de 50", cinquenta), ("Notas de 20", vinte), ("Notas de 10", dez), ("Notas de 5", cinco), ("Notas de 2", dois), ("Notas de 1 real", um)]
with open ("/workspaces/python/Programação_1/revisao_prova03/notas.txt", "w", encoding="utf-8") as arq:
    for i in saida:
        arq.write(f"{i[0]}: {i[1]}\n")