import spacy
import numpy as np

nlp = spacy.load("pt_core_news_lg")

doc1 = nlp("Cachorros gostam de brincar no parque.")
doc2 = nlp("Cachorros gostam de brincar no parque.")

# Similaridade com cosseno (utilizando embeddings)
def cos_similarity(x, y):
    """Calcula a similaridade do cosseno entre dois vetores."""
    numerator = np.dot(x, y)
    denominator = np.linalg.norm(x) * np.linalg.norm(y)
    return round(numerator / denominator, 3)

# Obter embeddings para o cálculo de similaridade com cosseno
embeddings1 = doc1.vector
embeddings2 = doc2.vector

cos_sim = cos_similarity(embeddings1, embeddings2)

print(f"Similaridade de cosseno entre os embeddings: {cos_sim:.3f}")
