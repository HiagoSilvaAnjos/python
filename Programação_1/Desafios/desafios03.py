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

def contar_consoantes(palavra):
    consoantes = "bcdfghjklmnpqrstvwxyz"
    counter = 0
    for letra in palavra:
        if letra in consoantes:
            counter += 1
    return counter

def quantity_to_words_nominais_frequency(list_words):
    contadores = {
        "infinitivo": 0,  # Termina em "r"
        "gerundio": 0,    # Termina em "ndo"
        "participio": 0   # Outros casos
    }

    maior_infinitivo = ""
    menor_gerundio = None

    # Processamento das palavras
    for palavra in list_words:
        if palavra.endswith("r"):
            contadores["infinitivo"] += 1
            if len(palavra) > len(maior_infinitivo):
                maior_infinitivo = palavra
        elif palavra.endswith("ndo"):
            contadores["gerundio"] += 1
            if menor_gerundio is None or len(palavra) < len(menor_gerundio):
                menor_gerundio = palavra
        else:
            contadores["participio"] += 1

    forma_mais_frequente = max(contadores.values())
    tamanho_maior_infinitivo = len(maior_infinitivo)
    consoantes_menor_gerundio = contar_consoantes(menor_gerundio)

    return forma_mais_frequente, tamanho_maior_infinitivo, consoantes_menor_gerundio

    
def main():
    vetor_list = obter_lista()
    if vetor_list is None:
        return

    try:
        forma_mais_frequente, tamanho_maior_infinitivo , consoantes_menor_gerundio = quantity_to_words_nominais_frequency(vetor_list)
        print(forma_mais_frequente)
        print(tamanho_maior_infinitivo)
        print(consoantes_menor_gerundio)

    except Exception as e:
        print("Entrada inválida. Digite um número inteiro.")
        print(e)

main()