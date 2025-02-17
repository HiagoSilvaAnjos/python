from math import sqrt
import spacy

nlp = spacy.load("pt_core_news_lg")

sentences = ["Cachorros gostam de brincar no parque.", "Cachorros gostam de brincar no parque."]

# Processa as frases para obter os documentos (objetos Doc do spaCy)
doc01 = nlp(sentences[0])
doc02 = nlp(sentences[1])

# Extrai os embeddings (vetores) das frases
embeddings1 = doc01.vector  # Vetor para a primeira frase
embeddings2 = doc02.vector  # Vetor para a segunda frase

# Função para calcular a soma dos quadrados de um vetor, retornando o valor da raiz quadrada
def squared_sum(x):
    """Calcula a soma dos quadrados e retorna o valor da raiz quadrada arredondado para 3 casas decimais"""
    return round(sqrt(sum([a*a for a in x])), 3)

# Função para calcular a similaridade do cosseno entre dois vetores
def cos_similarity(x, y):    
    # O numerador é o produto escalar (dot product) entre os dois vetores
    numerator = sum(a * b for a, b in zip(x, y))
    
    # O denominador é o produto das normas (módulos) dos dois vetores
    denominator = squared_sum(x) * squared_sum(y)
    
    # Retorna a similaridade do cosseno, que é o produto escalar dividido pelo produto das normas
    return round(numerator / float(denominator), 3)

cos_sim = cos_similarity(embeddings1, embeddings2)

print(f"Similaridade de cosseno entre os embeddings: {cos_sim:.3f}")
