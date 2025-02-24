from math import sqrt
import spacy
from collections import Counter

nlp = spacy.load("pt_core_news_lg")

sentences = "Python é uma linguagem de programação popular para ciência de dados. Muitas pessoas usam a linguagem Python para ciência de dados e machine learning. JavaScript é essencial para desenvolvimento web. Rust é conhecido por sua alta segurança e performance. Next.js é um framework baseado em React para desenvolvimento web. Next.js expande as funcionalidades do React, facilitando o desenvolvimento web."

doc = nlp(sentences)
sentences_list = [sent.text.strip() for sent in doc.sents]

# Tokeniza e remove pontuações e stopwords
sentences_clean = []
for sent in sentences_list:
    set_of_words = [token.text.lower() for token in nlp(sent) if not token.is_punct and not token.is_stop]
    sentences_clean.append(set_of_words)

def squared_sum(x):
    return round(sqrt(sum([a * a for a in x])), 2)

def cos_similarity(x, y):    
    numerator = sum(a * b for a, b in zip(x, y))  
    denominator = squared_sum(x) * squared_sum(y) 
    return round(numerator / float(denominator), 3) if denominator != 0 else 0.0  

juntando_sentencas = []
sentenca_atual = sentences_list[0]  

indice = 0
limite = 0.52

while indice < len(sentences_clean) - 1:
    contagem_palavras01 = Counter(sentences_clean[indice])
    contagem_palavras02 = Counter(sentences_clean[indice + 1])

    palavras_unicas_lista = set(sentences_clean[indice]).union(sentences_clean[indice + 1])

    frequencia_palavras_sentenca01 = [contagem_palavras01[word] for word in palavras_unicas_lista]
    frequencia_palavras_sentenca02 = [contagem_palavras02[word] for word in palavras_unicas_lista]     

    cos_sim = cos_similarity(frequencia_palavras_sentenca01, frequencia_palavras_sentenca02)

    print(f"Similaridade de cosseno entre as sentenças {indice + 1} e {indice + 2}: {cos_sim:.2f}")

    if cos_sim >= limite:
        # Se forem similares, acumula na variável `sentenca_atual`
        sentenca_atual += " " + sentences_list[indice + 1]
    else:
        # Se não forem similares, adiciona a sentença acumulada e inicia uma nova
        juntando_sentencas.append(sentenca_atual)
        sentenca_atual = sentences_list[indice + 1]
    
    indice += 1

# Adiciona a última sentença acumulada à lista
juntando_sentencas.append(sentenca_atual)

print("\nSentenças agrupadas:\n")
for sentenca in range(len(juntando_sentencas)):

    tokens = [token.text.lower() for token in nlp(juntando_sentencas[sentenca]) if not token.is_punct and not token.is_stop]

   
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

        print(f"Parágrafo {sentenca + 1}:") 
        print(f"'{juntando_sentencas[sentenca]}'") 
        print(f"<Tópicos: {', '.join(topicos)}>")

    print()
