def buscar_elemento(vetor, tamanhoLista, itemBuscado):

    for i in range(tamanhoLista):
        if vetor[i] == itemBuscado:
            return itemBuscado 
    return "Não encontrado" 

def main():
    try:
        tamanhoLista = int(input("Digite o tamanho do vetor: "))

        print(f"Digite {tamanhoLista} números para o vetor separados por espaço:")
        vetor_str = input().split()
        vetor = [int(num) for num in vetor_str]  

        if len(vetor) != tamanhoLista:
            print("Erro: O número de elementos não corresponde ao tamanho informado.")
            return

        itemBuscado = int(input("Digite o valor a ser buscado: "))

        posicao = buscar_elemento(vetor, tamanhoLista, itemBuscado)

        print(posicao)
    except ValueError:
        print("Erro: Certifique-se de fornecer apenas números inteiros.")

if __name__ == "__main__":
    main()
