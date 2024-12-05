# Dadas as temperaturas que foram registradas diariamente durante uma semana, faça um
# programa que, usando vetores, calcule e mostre a temperatura média e em quantos dias
# dessa semana a temperatura esteve acima da média. Informe também a maior temperatura
# no período
# Entradas:
# ● Vetor [7] de temperaturas (separados por espaços)
# Saída:
# ● temperatura média calculada
# ● total de dias com temperatura acima da média
# ● maior temperatura
# Exemplo de entrada:
# 25 26.8 32 27.5 26.5 28.1 24
# Exemplo de saída:
# 27.1
# 3
# 32

temperaturas_input = input("Digite as temperaturas ex:[28, 29.9, 30, 31, 28, 29, 31]: ").strip()
list_temps = []
temp_media = 0
sum_temps = 0
max_temp = 0
dias_acima_temps = 0


try:

    temps = float(temperaturas_input.split())

    if len(temps) !=  7 :
        print("Nescessário inserir 7 temperaturas.")
    else:

        max_temp = temps[0]

        for temp in temps:
            list_temps.append(float(temp))
            sum_temps += float(temp)

            if temp > max_temp :
                max_temp = temp    

        temp_media = sum_temps / len(temps)

        for temp in list_temps:
            if temp > temp_media :
                dias_acima_temps += 1
        
        print(list_temps)
        print(f"Maior temperatura: {max_temp}")
        print(f"Temperatura média: {temp_media}")
        print(f"Dias com temperatura acima da média: {dias_acima_temps}")
          
except Exception as e:
    print("Formato de entrada inválido.")

