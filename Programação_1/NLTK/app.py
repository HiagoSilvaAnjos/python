# pip install nltk
# pip install spacy
# pip install colorama
# python -m spacy download pt_core_news_sm

# IMPORTANDO AS LIBS
import spacy
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.corpus import wordnet
from colorama import Fore, Style, init

# Inicializa o colorama para Windows
init(autoreset=True)

# Baixar os recursos necessários do NLTK
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

texto = ""

# FIXME: Windows
try:
    with open("C:\\Users\\Hiago Silva\\Documents\\python\\Programação_1\\NLTK\\input.txt", "r", encoding="utf-8") as file:
        texto = file.read()

except FileNotFoundError:
    print(Fore.RED + "Arquivo não encontrado")
print()

lista_sentecas = []

# Tokenização de sentenças
sentencas = sent_tokenize(texto.lower())

# Criar uma lista separada para cada sentença
for indice in range(len(sentencas)):
    lista_sentecas.append({"sentenca": sentencas[indice], "paragrafo": indice + 1})

print(Fore.CYAN + Style.BRIGHT + "Tokenização de Sentenças:")
for sentence_list in lista_sentecas:
    print(Fore.YELLOW + f"Parágrafo {sentence_list['paragrafo']}: " + Fore.WHITE + sentence_list["sentenca"])
print()

# Tokenização de palavras
palavras = word_tokenize(texto.lower())
palavras_sem_pontuacao = [palavra for palavra in palavras if palavra.isalnum()]

print(Fore.CYAN + Style.BRIGHT + "Tokenização de Palavras (Geral):")
print(Fore.WHITE + str(palavras_sem_pontuacao))
print()

# Tokenização de palavras em cada sentença
for sentence in lista_sentecas:
    palavras_tokenizadas = word_tokenize(sentence["sentenca"].lower())
    palavras_sem_pontuacao = [palavra for palavra in palavras_tokenizadas if palavra.isalnum()]
    print(Fore.CYAN + Style.BRIGHT + f"Palavras Tokenizadas da lista {sentence['paragrafo']}:")
    print(palavras_sem_pontuacao)
    print()
print()

# POS Tagging - Usando o Spacy
nlp = spacy.load("pt_core_news_lg")

print(Fore.MAGENTA + Style.BRIGHT + "Análise POS Tagging (Spacy):")
for text_item in lista_sentecas:
    doc = nlp(text_item['sentenca'])
    print(Fore.YELLOW + f"Sentença {text_item['paragrafo']}: " + Fore.WHITE + text_item['sentenca'])
    for token in doc:
        if token.text.isalnum():
            print(Fore.GREEN + f"  Texto: {token.text}, Lema: {token.lemma_}, POS: {token.pos_}")
    print()

# Remoção de stopwords
stop_words = set(stopwords.words('portuguese'))
palavras_filtradas_geral = [palavra for palavra in palavras if palavra.lower() not in stop_words and palavra.isalnum()]

print(Fore.CYAN + Style.BRIGHT + "Palavras Filtradas (Sem Stopwords):")
print(Fore.WHITE + str(palavras_filtradas_geral))
print()

# Remoção stopwords de cada sentenca
for sentenca in lista_sentecas:
    print(Fore.CYAN + Style.BRIGHT + f"Remoção stopwords de:  {Fore.YELLOW + sentenca['sentenca']}")
    palavras_tokenizadas = word_tokenize(sentenca["sentenca"].lower())
    palavras_sem_pontuacao = [palavra for palavra in palavras_tokenizadas if palavra.isalnum()]
    palavras_filtradas = [palavra for palavra in palavras_sem_pontuacao if palavra not in stop_words]
    print(Fore.WHITE  +"Palavras filtradas:", palavras_filtradas)
    print()
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
palavras_stemmed = [ps.stem(palavra) for palavra in palavras_filtradas_geral]

print(Fore.CYAN + Style.BRIGHT + "Palavras após Stemming:")
print(Fore.WHITE + str(palavras_stemmed))
print()

# Frequência das palavras
frequencia = FreqDist(palavras_filtradas_geral)

print(Fore.CYAN + Style.BRIGHT + "Frequência das Palavras (Geral):")
print(Fore.WHITE + str(frequencia.most_common()))
print()

# Frequência das palavras por sentença
for sentence in lista_sentecas:
    palavras_tokenizadas = word_tokenize(sentence["sentenca"].lower())
    palavras_sem_pontuacao = [palavra for palavra in palavras_tokenizadas if palavra.isalnum()]
    palavras_filtradas = [palavra for palavra in palavras_sem_pontuacao if palavra not in stop_words]
    
    frequencia = FreqDist(palavras_filtradas)

    print(Fore.YELLOW + f"Frequência das palavras da sentença {sentence['paragrafo']}:")
    print(Fore.WHITE + str(frequencia.most_common()))
    print()

# Sinônimos usando WordNet - Geral
sinonimos_gerais = set()
for palavra in palavras_filtradas_geral:
    for syn in wordnet.synsets(palavra, lang="por"):
        for lemma in syn.lemmas("por"):
            sinonimos_gerais.add(lemma.name())

print(Fore.CYAN + Style.BRIGHT + "Sinônimos Gerais:")
print(Fore.WHITE + str(sinonimos_gerais))
print()

# Sinônimos de cada sentença
for sentenca in lista_sentecas:
    sinonimos_sentenca = set()
    palavras_tokenizadas = word_tokenize(sentenca["sentenca"].lower())
    palavras_sem_pontuacao = [palavra for palavra in palavras_tokenizadas if palavra.isalnum()]
    palavras_filtradas = [palavra for palavra in palavras_sem_pontuacao if palavra not in stop_words]

    for palavra in palavras_filtradas:
        for syn in wordnet.synsets(palavra, lang="por"):
            for lemma in syn.lemmas("por"):
                sinonimos_sentenca.add(lemma.name())

    print(Fore.YELLOW + f"Sinônimos da sentença {sentenca['paragrafo']}:")
    sinonimos_lista = list(sinonimos_sentenca)
    print(Fore.WHITE + f"{sinonimos_lista}")