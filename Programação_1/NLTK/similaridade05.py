#INSTALE AS DEPENDENCIAS 
# pip install spacy
# python -m spacy download pt_core_news_lg

#MINHAS REFERENCIAS:
"""
1 - https://docs.google.com/presentation/d/1lpWQ6Zh4XyVa2F0VQNYx_g7N3aX2BpeDdOuuzLSaZiY/edit#slide=id.g335352aba55_0_13
2 - https://www.newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
3 - https://www.nltk.org/
4 - https://spacy.io/
5 - https://www.youtube.com/watch?v=Vr9QXpELdrs => Explicação Maravilhosa
"""

from math import sqrt
import spacy
from collections import Counter

# Carregar o modelo pré-treinado em português
nlp = spacy.load("pt_core_news_lg")

sentences = "Python é uma linguagem de programação popular para ciência de dados. Muitas pessoas usam a linguagem Python para ciência de dados e machine learning. JavaScript é essencial para desenvolvimento web. Rust é conhecido por sua alta segurança e performance. Next.js é um framework baseado em React para desenvolvimento web. Next.js expande as funcionalidades do React, facilitando o desenvolvimento web."

# sentences = "Python é uma linguagem de programação popular para ciência de dados. Rust é conhecido por sua alta segurança e performance."

# sentences = "Um cachorro e um gato. Um sapo e um gato"

# sentences = "Python é uma linguagem de programação popular para ciência de dados. Muitas pessoas usam a linguagem Python para ciência de dados e machine learning. Nextjs expande as funcionalidades do React, facilitando o desenvolvimento web."

#FIXME: Quebrando o texto em sentenças
doc = nlp(sentences)
sentences_list = [sent.text.strip() for sent in doc.sents]
print(f"Quebrando texto em sentenças: ")
print(sentences_list)
print()

# Tokeniza e remove pontuações e stopwords

"""
FIXME: Iterar sobre cada sentenca e remover pontuações e stopwords
ex: Entrada:  "Python é uma linguagem de programação popular para ciência de dados."
    Saida: "python linguagem programação popular ciência dados"
"""
sentences_clean = []
for sent in sentences_list:
    set_of_words = [token.text.lower() for token in nlp(sent) if not token.is_punct and not token.is_stop]
    sentences_clean.append(set_of_words)

print(f"Removendo pontuações e stopwords: ")
print(sentences_clean)
print()


# Encontrando o denominador que é o produto escalar (dot product) entre os dois vetores
def squared_sum(x):
    return round(sqrt(sum([a * a for a in x])), 2)

def cos_similarity(x, y):

    # O numerador é o produto escalar (dot product) entre os dois vetores    
    numerator = sum(a * b for a, b in zip(x, y))  

    denominator = squared_sum(x) * squared_sum(y) 

    # Retorna a similaridade do cosseno, que é o produto escalar dividido pelo produto das normas
    return round(numerator / float(denominator), 3) if denominator != 0 else 0.0  

# Juntando sentenças
juntando_sentencas = []

# Iterando sobre as sentenças e calculando a similaridade do cosseno - com início do 0
indice = 0

# Limite de similaridade
limite = 0.52

"""
FIXME: LÓGICA do while: 

        => while indice < len(sentences_clean) - 1:
            => Iterar desde o indice 0 até o (tamanho da lista de sentenças limpas - 1)
             FIXME: Por que?
                Se utilizar  "while indice < len(sentences_clean)": O correrá um erro de indice não encontrado na lista de sentaças limpas, especificamente em => contagem_palavras02 = Counter(sentences_clean[indice + 1])
                Exemplo:
                    Considere a lista de sentenças: ["Python é uma linguagem de programação popular para ciência de dados.", "Muitas pessoas usam a linguagem Python para ciência de dados e machine learning.", "Next.js expande as funcionalidades do React, facilitando o desenvolvimento web."]

                    O len dessa lista seria é 3 e os elementos da lista seriam acessados por índices 0, 1, 2

                    Ao iniciar o while com "while indice < len(sentences_clean)", o loop tentará acessar o índice 3, que não existe na lista de sentenças limpas, pois como a primeira sentença e a segunda são similares, a variável "indice" que inicialmente é 0, passará a ser 2, e ao rodar o while novamente, o indice agora vale 2 e ao chegar na parte na parte: 
                        contagem_palavras02 = Counter(sentences_clean[indice + 1]
                        Onde:
                          o indice vale 2 e ao ser somado com 1 vira 3, porem a lista vai até os indices 0, 1, 2
                          Ou seja: a variável indice tentará acessar o indice 3 que não existe na lista de sentenças limpas, gerando um erro de índice não encontrado na lista de sentenças limpas
                         O resultado será um:
                             IndexError: list index out of range

    FIXME: Lógica dentro do while:
                             
    - Iterar sobre cada sentença da lista de Sentenças limpas => 1
    - Contar a frequência de cada palavra em ambas as sentenças => 2
    - Unifica as palavras em uma lista única => 3
    - Obtem a lista de frequências de cada palavra em cada sentença em relação a lista unificada das duas => 4
    - Calcula a similaridade do cosseno entre as duas contagens => 5
    - Adiciona a sentença à lista de juntando_sentencas se a similaridade do cosseno for maior ou igual ao limite => 6
    - Se não forem similares, adiciona a sentença à lista de juntando_sentencas e incrementa o índice => 7
    - se não for possível adicionar a ultima sentença da listas limpas, adiciona a sentença à lista de juntando_sentencas => 8
    - Se todas as sentenças forem adicionadas à lista de juntando_sentencas, encerra o loop


    MAS, ESSE CPODIGO GERA UM BUG, pois ele só calcula a similaria de 2 em duas sentenças, em outras palavras, se a sentença 1 for similar com a 2, elas são adicionadas a lista de sentenças juntas, porem o código pula para a sentença 3 e 4, não checando se a 2 é similar com a 3.
    Ocasionando que mesmo que a terceira sentença for similar com a 1 e 2, ela não será checada.

    Correção em: similaridade06.py

"""

print(f"Iniciando a Similaridade:")
print()
while indice < len(sentences_clean) -1: #1

    print(f"Pegando a frequencia de cada palavra de cada sentença:")
    print()
    contagem_palavras01 = Counter(sentences_clean[indice]) #2
    print(sentences_clean[indice])
    print(contagem_palavras01)
    print()
    contagem_palavras02 = Counter(sentences_clean[indice + 1]) #2
    print(sentences_clean[indice + 1])
    print(contagem_palavras02)

    print()

    print(f"Juntando as duas senteças: ")
    palavras_unicas_lista = set(sentences_clean[indice]).union(sentences_clean[indice + 1]) #3
    print(palavras_unicas_lista)
    print()

    print(f"Obtendo a frequencia de cada palvra de cada sentença em relação a lista unificada:")
    frequencia_palavras_sentenca01 = [contagem_palavras01[word] for word in palavras_unicas_lista] #4
    print(frequencia_palavras_sentenca01)
    print()
    frequencia_palavras_sentenca02 = [contagem_palavras02[word] for word in palavras_unicas_lista]  #4  
    print(frequencia_palavras_sentenca02)
    print()

    cos_sim = cos_similarity(frequencia_palavras_sentenca01, frequencia_palavras_sentenca02) #5

    print(f"Similaridade de cosseno entre as sentenças {indice + 1} e {indice + 2}: {cos_sim:.2f}")
    print()

    if cos_sim >= limite: #6
        # Juntando as sentenças
        combinar_sentencas = sentences_list[indice] + " " + sentences_list[indice + 1]
        # Adicionando a junção à lista
        juntando_sentencas.append(combinar_sentencas)
        # Atualizando o índice
        indice += 2
    else: #7
        # Adiciona a sentença à lista
        juntando_sentencas.append(sentences_list[indice])
        # Incrementando o índice
        indice += 1

# Se a ultima sentença não foi combinada, junte-a
if indice == len(sentences_clean) - 1: #8
    juntando_sentencas.append(sentences_list[indice])

print()


# Mostrar os tópicos relevantes com As sentenças semelhantes juntas
"""
FIXME: Como encontrar os tópicos relevantes:
    2 FORMAS:

        1. palavras com frequência maior que 1
            Vamos novamente quebrar a sentença em uma lista de palavras sem stopwords e pontuações
            Contar a frequência de cada palavra
            Se a palavra tem uma frequência maior que 1, ela é considerada como relevante e é atribuida dentro da variável chaves_frequentes
            Fazer um join na palavras com maior frequência e exibir como tópico separadas por virgula

        2. Se não existir palavars com frequencia maior que 1
            Vamos pegar palavras relevantes, que são substantivos, verbos e adjetivos, nomes próprios
            Se não existir palavras relevantes, pegar a primeira palavra da sentença
            Exibir a sentença e a palavra relevante como tópico
    
"""

print(f"Saída Final:")
print()

for sentenca in range(len(juntando_sentencas)):

    tokens = [token.text.lower() for token in nlp(juntando_sentencas[sentenca]) if not token.is_punct and not token.is_stop]

    #checar contagem
    contagem_palavras = Counter(tokens)

    # Pegar palavras com frequencia maior que 1
    chaves_frequentes = [chave for chave in contagem_palavras if contagem_palavras[chave] > 1]

    if chaves_frequentes:
        print(f"Parágrafo {sentenca  + 1}:") 
        print(f"{juntando_sentencas[sentenca]}") 
        print(f"<Tópicos: {', '.join(chaves_frequentes)}>")
    else:
        palavras_relevantes = [token.text for token in nlp(" ".join(tokens)) if token.pos_ in ["NOUN", "VERB", "ADJ", "PROPN"]]
        topicos = []
        if palavras_relevantes and len(palavras_relevantes) > 1:
            topicos.append(palavras_relevantes[0])
            topicos.append(palavras_relevantes[1])
        else:
            topicos.append(palavras_relevantes[0])
        # topicos = palavras_relevantes[0] if palavras_relevantes else tokens[0].text.lower()

        print(f"Parágrafo {sentenca + 1}:") 
        print(f"'{juntando_sentencas[sentenca]}'") 
        print(f"<Tópicos: {', '.join(topicos)}>")

    print()
