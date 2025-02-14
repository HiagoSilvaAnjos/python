# pip install nltk
# pip install spacy
import spacy


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.corpus import wordnet

# Baixar os recursos necessários do NLTK
nltk.download('omw-1.4')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

texto = ""

# Texto de exemplo
try:
    with open("/home/savio/Documentos/curso-python/Programação_1/NLTK/input.txt", "r", encoding="utf-8") as file:
        texto = file.read()

except FileNotFoundError:
    print("Arquivo não encontrado")
print()

# Tokenização de sentenças
sentencas = sent_tokenize(texto.lower())
print("Sentenças:", sentencas)

print()

# Tokenização de palavras
palavras = word_tokenize(texto.lower())
palavras_sem_pontuacao = [palavra for palavra in palavras if palavra.isalnum()]
print("Palavras:", palavras_sem_pontuacao)
print()


# POS Tagging - Usando o Spacy
# Carregar o modelo pré-treinado em português
nlp = spacy.load("pt_core_news_sm")

# Processar o texto
for text_item in sentencas:
    print(f"Sentença: '{text_item}' Tamanho: {len(text_item)}")
    doc = nlp(text_item)
    print("Tokens e suas propriedades:")
    print()
    for token in doc:
        print(doc.similarity(token))
        if token.text.isalnum():
            print(f"Texto: '{token.text}', Tamanho: {len(token.text)}, Lema: {token.lemma_}, POS: {token.pos_}, Tag: {token.tag_}, Dependência: {token.dep_}, Cabeça: {token.head.text}")
    print()

print()

# Remoção de stopwords
stop_words = set(stopwords.words('portuguese'))
print("Stopwords:", stop_words, "Tamanho:", len(stop_words))

print()

palavras_filtradas = [palavra for palavra in palavras if palavra.lower() not in stop_words and palavra.lower().isalnum()]
print("Palavras filtradas:", palavras_filtradas)

print()


"""
FIXME:
Stemming é uma técnica de Processamento de Linguagem Natural (PLN) usada para reduzir palavras à sua raiz (ou stem), removendo sufixos e prefixos. Isso ajuda a normalizar palavras diferentes que compartilham o mesmo significado base.

Por exemplo:

"running" → "run"
"studies" → "studi"
"better" → "better" (algumas palavras podem não ser alteradas)
Essa técnica é útil em buscas e indexação de textos, pois reduz a variação das palavras, facilitando a correspondência entre termos semelhantes.
"""
# Stemming
ps = PorterStemmer()
palavras_stemmed = [ps.stem(palavra) for palavra in palavras_filtradas]
print("Palavras após stemming:", palavras_stemmed)

print()

# Frequência das palavras
frequencia = FreqDist(palavras_filtradas)
print("Frequência das palavras:", frequencia.most_common())
print()

"""
FIXME: O WordNet é um banco de dados lexical da língua inglesa, disponível no nltk, que organiza palavras em conjuntos de sinônimos chamados "synsets" (synonym sets). Ele fornece relações semânticas entre palavras, incluindo sinônimos, antônimos, hiperônimos (termos mais genéricos), hipônimos (termos mais específicos), entre outros.
"""
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
