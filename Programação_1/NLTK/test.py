import spacy

nlp = spacy.load("pt_core_news_lg")

doc1 = nlp("Arroz tem um gosto muito bom.")
doc2 = nlp("Feijão tem um gosto muito bom.")

# Similarity of two documents
print(doc1, "<->", doc2, doc2.similarity(doc1))
# Similarity of tokens and spans
# french_fries = doc1[2:4]
# burgers = doc1[5]
# print(french_fries, "<->", burgers, french_fries.similarity(burgers))