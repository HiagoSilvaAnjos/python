#Hiago Silva - Questão 02

kill_programin = False
list_earnings_person = []

# GANHO MÉDIO DE SALÁRIO
def calculate_media_earnings(persons):
    sum_earnings = 0
    for person in persons:
        sum_earnings += person[0]

    return sum_earnings / len(persons)


# MÉDIA DO NÚMERO DE FILHOS
def calculate_media_childrens(persons):
    sum_childrens = 0
    for person in persons:
        sum_childrens += person[1]

    return sum_childrens / len(persons)

# GANHO MÁXIMO DE SALÁRIO
def find_max_earning(persons):
    max_earning = persons[0][0]
    for person in persons:
        if person[0] > max_earning:
            max_earning = person[0]

    return max_earning

# # PERCENTUAL DE SALÁRIOS ACIMA DE 100
def calculate_percentage_over_100(persons):
    count_over_100 = 0
    for person in persons:
        if person[0] > 100:
            count_over_100 += 1

    return (count_over_100 / len(persons)) * 100

while not kill_programin:
    try:
        earning_person = float(input("Insira o salário do habitante ou um salário negativo para terminar: "))
        if earning_person < 0:
            kill_programin = True
            continue

        quantity_children = int(input("Insira a quantidade de filhos do habitante: "))

        if quantity_children < 0:
            print("QUANTIDADE DE FILHOS INVÁLIDA")
            continue

        list_earnings_person.append((earning_person, quantity_children))
    except:
        print("ENTRADA INVÁLIDA")

if list_earnings_person:
    print("Vetor de salários:", list_earnings_person)
    print("Média de salários:", calculate_media_earnings(list_earnings_person))
    print("Média de filhos:", calculate_media_childrens(list_earnings_person))
    print("Salário máximo:", find_max_earning(list_earnings_person))
    print("Percentual de salários acima de 100:", calculate_percentage_over_100(list_earnings_person))