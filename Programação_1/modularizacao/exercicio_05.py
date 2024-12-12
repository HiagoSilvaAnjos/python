def buscar_elemento(vetor, n, a):

    for i in range(n):
        if vetor[i] == a:
            return i  
    return "Não encontrado" 

def main():
    try:
        n = int(input("Digite o tamanho do vetor: "))

        print(f"Digite {n} números para o vetor separados por espaço:")
        vetor_str = input().split()
        vetor = [int(num) for num in vetor_str]  

        if len(vetor) != n:
            print("Erro: O número de elementos não corresponde ao tamanho informado.")
            return

        a = int(input("Digite o valor a ser buscado: "))

        posicao = buscar_elemento(vetor, n, a)

        print(posicao)
    except ValueError:
        print("Erro: Certifique-se de fornecer apenas números inteiros.")

if __name__ == "__main__":
    main()
