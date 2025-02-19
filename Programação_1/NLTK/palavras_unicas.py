import nltk
nltk.download('punkt')  # Necessário para usar o word_tokenize

sentenca1 = "Python é uma linguagem poderosa poderosa."
sentenca2 = "Python é fácil de aprender poderosa."

# Tokenizando as sentenças
palavras1 = set(nltk.word_tokenize(sentenca1))
palavras2 = set(nltk.word_tokenize(sentenca2))

# Unindo os conjuntos
palavras_unicas = palavras1.union(palavras2) 

print(palavras_unicas)
