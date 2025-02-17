from math import sqrt
import spacy
nlp = spacy.load("pt_core_news_lg")

sentences = ["Cachorros gostam de brincar no parque.", "Cachorros gostam de brincar no parque."]

doc01 = nlp(sentences[0])
doc02 = nlp(sentences[1])

embeddings1 = doc01.vector
embeddings2 = doc02.vector

def squared_sum(x):
  """ return 3 rounded square rooted value """
  return round(sqrt(sum([a*a for a in x])),3)


def cos_similarity(x,y):
  """ return cosine similarity between two lists """
 
  numerator = sum(a*b for a,b in zip(x,y))
  denominator = squared_sum(x)*squared_sum(y)
  return round(numerator/float(denominator),3)

cos_sim = cos_similarity(embeddings1, embeddings2)

print(f"Similaridade de cosseno entre os embeddings: {cos_sim:.3f}")