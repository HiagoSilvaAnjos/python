# pip install nltk

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.corpus import wordnet

# Buscar sinônimos em pt-br
from nltk.corpus import wordnet as wn

# Baixar os recursos necessários do NLTK
nltk.download('omw-1.4')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# Texto de exemplo
texto = """A ginasta Jade Barbosa, que obteve três medalhas nos Jogos Pan-Americanos do Rio, em julho, venceu votação na internet e será a representante brasileira no revezamento da tocha olímpica para Pequim-2008. A tocha passará por vinte países, mas o Brasil não estará no percurso olímpico. Por isso, Jade participará do evento em Buenos Aires, na Argentina, única cidade da América do Sul a receber o símbolo dos Jogos.
O revezamento terminará em 8 de agosto, primeiro dia das Olimpíadas de Pequim."""

print()

# Tokenização de sentenças
sentencas = sent_tokenize(texto)
print("Sentenças:", sentencas)

print()

# Tokenização de palavras
palavras = word_tokenize(texto)
print("Palavras:", palavras)

print()

# Remoção de stopwords
stop_words = set(stopwords.words('portuguese'))
print("Stopwords:", stop_words)

print()

palavras_filtradas = [palavra for palavra in palavras if palavra.lower() not in stop_words]
print("Palavras filtradas:", palavras_filtradas)

print()

# Stemming
ps = PorterStemmer()
palavras_stemmed = [ps.stem(palavra) for palavra in palavras_filtradas]
print("Palavras após stemming:", palavras_stemmed)

print()

# Frequência das palavras
frequencia = FreqDist(palavras_filtradas)
print("Frequência das palavras:", frequencia.most_common())

#FIXME: O WordNet é um banco de dados lexical da língua inglesa, disponível no nltk, que organiza palavras em conjuntos de sinônimos chamados "synsets" (synonym sets). Ele fornece relações semânticas entre palavras, incluindo sinônimos, antônimos, hiperônimos (termos mais genéricos), hipônimos (termos mais específicos), entre outros.

print()

# Sinônimos usando WordNet
sinonimos = set()

#FIXME: pecorrer cada palavra
for palavra in palavras_filtradas:
    #FIXME: pecorrer cada synset (conjuntos de sinônimos) da palavra
    for syn in wordnet.synsets(palavra, lang="por"):
        #FIXME: Percorre os sinônimos dentro do synset
        for lemma in syn.lemmas("por"):
            sinonimos.add(lemma.name()) #FIXME: Adiciona o sinônimo na lista
print("Sinônimos:", sinonimos)


# Lista de palavras para buscar sinônimos
# Lista de palavras em português
# palavras_filtradas = ["feliz", "rápido", "loja"]

# # Criando uma lista para armazenar os sinônimos
# sinonimos = set()

# # Percorre cada palavra
# for palavra in palavras_filtradas:
#     # Obtém os synsets (conjuntos de sinônimos) da palavra em português
#     for syn in wn.synsets(palavra, lang="por"):  # "por" indica português
#         # Percorre os sinônimos dentro do synset
#         for lemma in syn.lemmas("por"):
#             sinonimos.add(lemma.name())  # Adiciona o nome do sinônimo

# # Exibe os sinônimos únicos
# print("Sinônimos:", sinonimos)
