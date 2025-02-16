import spacy

nlp = spacy.load("pt_core_news_lg")

doc1 = nlp("Arroz tem um gosto muito bom.")
doc2 = nlp("Cachorros gostam de brincar no parque.")

print(doc1)

# Filtrando apenas substantivos e verbos para comparação
def filtrar_tokens(doc):
    return " ".join([token.text for token in doc if token.pos_ in ["NOUN", "VERB"]])

doc1_filtrado = filtrar_tokens(doc1)
doc2_filtrado = filtrar_tokens(doc2)

print(f"Texto original 1: {doc1}")
print(f"Texto original 2: {doc2}")
print(f"Texto filtrado 1: {doc1_filtrado}")
print(f"Texto filtrado 2: {doc2_filtrado}")

# Similaridade com frases completas
similaridade_completa = doc1.similarity(doc2)

# Similaridade com frases filtradas
similaridade_filtrada = doc1_filtrado.similarity(doc2_filtrado)

print(f"Similaridade completa: {similaridade_completa:.2f}")
print(f"Similaridade filtrada (apenas substantivos e verbos): {similaridade_filtrada:.2f}")
