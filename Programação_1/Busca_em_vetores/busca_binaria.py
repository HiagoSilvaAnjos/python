vetor_list=[3,15,70,80,150,461]
start = 0
found=False

try:
    value_input=int(input("Digite o valor a ser buscado: "))

    finish = len(vetor_list)-1

    while start<=finish and not found: 

        meio_vetor = (start + finish)//2
        if vetor_list[meio_vetor] == value_input:
            found=True
        else:
            if value_input < vetor_list[meio_vetor]:
                finish = meio_vetor-1
            else:
                start=meio_vetor+1

    if found:
        print(f"Encontrado: {found} | Valor: {vetor_list[meio_vetor]} | Indice: {meio_vetor}")
    else:
        print(f"Não Encontrado")
except:
     print("Input inválido")