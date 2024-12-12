def imprimir_linha(linha):
    
    for i in range(1, linha + 1):
        print(i, end=" ")
    print()  

def main():
    try:
        n = int(input("Digite o número de linhas da pirâmide: "))

        if n <= 0:
            print("Erro: O número de linhas deve ser maior que 0.")
            return

        for linha in range(1, n + 1):
            imprimir_linha(linha)
    except ValueError:
        print("Erro: Certifique-se de fornecer um número inteiro válido.")

if __name__ == "__main__":
    main()
