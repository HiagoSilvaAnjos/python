from math import sqrt
import spacy
from collections import Counter

nlp = spacy.load("pt_core_news_lg")

sentences = "Python é uma linguagem de programação popular para ciência de dados. Muitas pessoas usam a linguagem Python para ciência de dados e machine learning."

doc = nlp(sentences)
sentences_list = [sent.text for sent in doc.sents]
print(sentences_list)

# Tokeniza e remove pontuações e stopwords
sentences_clean = []
for sent in sentences_list:
    set_of_words = [token.text.lower() for token in nlp(sent) if not token.is_punct and not token.is_stop]
    sentences_clean.append(set_of_words)

# Contagem de palavras
contagem1 = Counter(sentences_clean[0])
contagem2 = Counter(sentences_clean[1])

# União das palavras únicas sem stopwords
uniqueWords = set(sentences_clean[0]).union(sentences_clean[1])

# Frequência das palavras
frequence01 = [contagem1[word] for word in uniqueWords]
frequence02 = [contagem2[word] for word in uniqueWords]

# Função para calcular a soma dos quadrados de um vetor, retornando a raiz quadrada
def squared_sum(x):
    return round(sqrt(sum([a * a for a in x])), 2)

# Função para calcular a similaridade do cosseno entre dois vetores
def cos_similarity(x, y):    
    numerator = sum(a * b for a, b in zip(x, y))  # Produto escalar
    denominator = squared_sum(x) * squared_sum(y)  # Produto das normas
    return round(numerator / float(denominator), 3) if denominator != 0 else 0.0  # Evita divisão por zero

cos_sim = cos_similarity(frequence01, frequence02)

print(f"Similaridade de cosseno entre os embeddings: {cos_sim:.2f}")

if cos_sim > 0.5:
    juntar_sentencas = sentences_list[0] + " " + sentences_list[1]
    print(f"Juntando as sentenças: {juntar_sentencas}")