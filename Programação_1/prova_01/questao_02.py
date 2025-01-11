#Hiago Silva - Questão 02

kill_programin = False
list_earnings_person = []
media_earnings = 0
sum_total_earnings = 0
quantity_total_person_earnings = 0

media_children = 0
sum_total_children = 0
quantity_total_person_children = 0

max_earning = 0

earnings_até_1000 = 0

while not kill_programin:

    try:
        earning_person = float(input("Insira o salário do habitante ou um salário negativo para terminar: "))

        if earning_person < 0:
            kill_programin = True
            continue

        quantity_children = int(input("Insira a quantidade de filhos do habitante: "))
        quantity_total_person_children += 1
        quantity_total_person_earnings += 1
        list_earnings_person.append((earning_person, quantity_children))
    except:
        print("ENTRADA INVÁLIDA")


# GANHO MÉDIO DE SALÁRIO
for person in list_earnings_person: sum_total_earnings += person[0]
media_earnings = sum_total_earnings / quantity_total_person_earnings
print(f"Média de salários dos habitantes: {media_earnings:0.2f}")

# MÉDIA DO NÚMERO DE FILHOS
for person in list_earnings_person: sum_total_children += person[1]
media_children = sum_total_children / quantity_total_person_children
print(f"Média de filhos por habitante: {media_children:0.2f}")

# GANHO MÁXIMO DE SALÁRIO
max_earning = list_earnings_person[0][0]
for person in list_earnings_person:
    if person[0] > max_earning:
        max_earning = person[0]

print(f"Salário máximo ganho por habitante: {max_earning: 0.2f}")


# # PERCENTUAL DE SALÁRIOS ACIMA DE 100
for person in list_earnings_person: 
    if person[0] <= 1000: earnings_até_1000 += 1

percentage = (earnings_até_1000 * 100) / quantity_total_person_earnings
print(f"A porcentagem de habitantes que ganham no mínimo 1000 é:{percentage: 0.2f}%")