from math import sqrt
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')

stop_words = set(stopwords.words('portuguese'))

lista_sentecas_limpas = []

texto = "A dog and a cat. A frog and a cat"

sentencas = sent_tokenize(texto.lower())

for indice in range(len(sentencas)):
    palavras_limpas = [palavra for palavra in word_tokenize(sentencas[indice]) if palavra.isalnum() and palavra not in stop_words]
    lista_sentecas_limpas.append((palavras_limpas, indice + 1))

contagem1 = Counter(lista_sentecas_limpas[0][0])
contagem2 = Counter(lista_sentecas_limpas[1][0])

uniqueWords = set(lista_sentecas_limpas[0][0]).union(lista_sentecas_limpas[1][0])

frequence01 = []
frequence02 = []
for word in uniqueWords:
    frequence01.append(contagem1[word])
    frequence02.append(contagem2[word])

# Função para calcular a soma dos quadrados de um vetor, retornando o valor da raiz quadrada
def squared_sum(x):
    """Calcula a soma dos quadrados e retorna o valor da raiz quadrada arredondado para 3 casas decimais"""
    return round(sqrt(sum([a*a for a in x])), 2)

# Função para calcular a similaridade do cosseno entre dois vetores
def cos_similarity(x, y):    
    # O numerador é o produto escalar (dot product) entre os dois vetores
    numerator = sum(a * b for a, b in zip(x, y))
    
    # O denominador é o produto das normas (módulos) dos dois vetores
    denominator = squared_sum(x) * squared_sum(y)
    
    # Retorna a similaridade do cosseno, que é o produto escalar dividido pelo produto das normas
    return round(numerator / float(denominator), 3)

cos_sim = cos_similarity(frequence01, frequence02)

print(f"Similaridade de cosseno entre os embeddings: {cos_sim:.2f}")