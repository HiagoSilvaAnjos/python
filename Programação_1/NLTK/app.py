# pip install nltk

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.corpus import wordnet

# Baixar os recursos necessários do NLTK
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# Texto de exemplo
texto = "Olá! Bem-vindo ao tutorial do NLTK. Este é um exemplo de processamento de linguagem natural."

# Tokenização de sentenças
sentencas = sent_tokenize(texto)
print("Sentenças:", sentencas)

# Tokenização de palavras
palavras = word_tokenize(texto)
print("Palavras:", palavras)

# Remoção de stopwords
stop_words = set(stopwords.words('portuguese'))
palavras_filtradas = [palavra for palavra in palavras if palavra.lower() not in stop_words]
print("Palavras filtradas:", palavras_filtradas)

# Stemming
ps = PorterStemmer()
palavras_stemmed = [ps.stem(palavra) for palavra in palavras_filtradas]
print("Palavras após stemming:", palavras_stemmed)

# Frequência das palavras
frequencia = FreqDist(palavras_filtradas)
print("Frequência das palavras:", frequencia.most_common())

# Sinônimos usando WordNet
sinonimos = []
for palavra in palavras_filtradas:
    for syn in wordnet.synsets(palavra):
        for lemma in syn.lemmas():
            sinonimos.append(lemma.name())
print("Sinônimos:", set(sinonimos))