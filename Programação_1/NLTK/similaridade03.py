import spacy
import numpy as np

# Carrega o modelo de linguagem do spaCy para o português
nlp = spacy.load("pt_core_news_lg")

# Frases que serão analisadas
doc1 = nlp("Cachorros gostam de brincar no parque.")
doc2 = nlp("Cachorros gostam de brincar no parque.")

# Função para calcular a similaridade do cosseno entre dois vetores
def cos_similarity(x, y):
    
    # O numerador é o produto escalar (dot product) entre os dois vetores
    numerator = np.dot(x, y)
    
    # O denominador é o produto das normas (módulos) dos dois vetores
    # np.linalg.norm calcula a norma (magnitude) do vetor
    denominator = np.linalg.norm(x) * np.linalg.norm(y)
    
    # Retorna a similaridade do cosseno, que é o produto escalar dividido pelo produto das normas
    return round(numerator / denominator, 3)

# Obter os embeddings dos documentos (representações vetoriais das frases)
embeddings1 = doc1.vector  # Vetor para o primeiro documento
embeddings2 = doc2.vector  # Vetor para o segundo documento

cos_sim = cos_similarity(embeddings1, embeddings2)

print(f"Similaridade de cosseno entre os embeddings: {cos_sim:.3f}")
