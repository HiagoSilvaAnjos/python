# Entradas:
# 1. Quantidade de verbos a serem informados.
# 2. Sequência de verbos em uma das formas nominais (uma palavra por linha).
# Saídas:
# 1. A quantidade de verbos da forma nominal que apareceu mais vezes.
# 2. O número de letras da maior palavra no infinitivo.
# 3. O número de consoantes da menor palavra no gerúndio.
# Exemplo de Entrada:
# 4
# andando
# cantar
# seguindo
# cansado
# Exemplo de Saída:
# 2
# 6
# 4

def obter_lista():
    try:
        length_array = int(input("Digite a quantidade de palavras a serem armazenados: "))
        vetor_list = []
        
        print("Digite os as palavras:")
        for i in range(length_array):
            number_input = input(f"Palavra {i+1}: ")
            vetor_list.append(number_input)
        
        return vetor_list
    except:
        print("Entrada inválida. Digite um número inteiro.")
        return None
    
def test_word(list_words):
    quantity_de_nominais_apareceu_mais_vezes = 0
    total_letras_maior_nominal = 0
    total_cosoantes_menor_palavras_gerundio = 0 #ndo

    list_nominais = []

    for palavra in list_words:
        if "ndo" in palavra or palavra[-1] == "r":
            list_nominais.append(palavra)


    return print(list_nominais)
    
def main():
    vetor_list = obter_lista()
    if vetor_list is None:
        return

    try:
        
        test_word(vetor_list)

        

    except Exception as e:
        print("Entrada inválida. Digite um número inteiro.")
        print(e)

main()