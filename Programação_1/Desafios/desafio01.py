# 1. Faça um programa que procura um texto dentro de outro texto, sem utilizar qualquer
# função ou método auxiliar (ou seja: a busca deve ser manual).
# O programa deve informar a posição da primeira ocorrência do texto procurado. Caso o
# texto procurado não seja encontrado, a posição informada deverá ser -1 para indicar essa
# situação especial.
# Os textos terão no máximo 254 caracteres. Todos os caracteres do texto serão
# não-brancos.


# Entradas:
# 1. O texto no qual será realizada a busca,
# 2. O texto que será buscado no anterior.


# Saídas:
# 1. a posição em que o texto procurado começou a ser encontrado no outro texto, ou -1
# se ele não for encontrado.

def find_text_position(text, text_search):
    for i in range(len(text)):
        if text[i:i+len(text_search)] == text_search:
            print(text[i:i+len(text_search)])
            return i
    return -1

text = "aabcbcbbacbbaa"
text_search = "cbb"


position = find_text_position(text, text_search)
print(position)  
