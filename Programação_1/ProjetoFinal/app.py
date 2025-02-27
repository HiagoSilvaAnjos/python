import spacy
from collections import Counter
from math import sqrt
nlp = spacy.load("pt_core_news_lg")

caminho_relativo_entrada = "/home/savio/Documentos/curso-python/Programação_1/ProjetoFinal/texto_entrada.txt"
caminho_relativo_saida = "/home/savio/Documentos/curso-python/Programação_1/ProjetoFinal/texto_saida.txt"

#HELPER FUNCTIONS
def remover_stopwords_pontuacao(sentenca_tokenizada):  
       return [token.text for token in nlp(sentenca_tokenizada) if not token.is_punct and not token.is_stop]

def squared_sum(x):
    return round(sqrt(sum([a * a for a in x])), 2)

def similaridade_do_cossseno(x, y):    
    numerador = sum(a * b for a, b in zip(x, y))  
    denominador = squared_sum(x) * squared_sum(y) 
    return round(numerador / float(denominador), 3) if denominador != 0 else 0.0  

#MAIN FUNCTIONS
def abrir_arquivo(caminho_relativo):
    try:
        with open(caminho_relativo, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    
def processar_texto(texto):
    doc = nlp(texto)
    sentencas_tokenizadas = [sent.text.strip() for sent in doc.sents]

    sentencas_limpas = []
    for sentenca in sentencas_tokenizadas:
        sentenca_limpa = remover_stopwords_pontuacao(sentenca)
        sentencas_limpas.append(sentenca_limpa)

    return (sentencas_limpas,sentencas_tokenizadas)

def calcular_similaridade(sentencas_processadas, sentencas_originais, indice = 0, limite = 0.4):
    sentenca_atual_de_memoria = str(sentencas_originais[0])
    lista_sentencas_concatenadas = []
    
    while indice < len(sentencas_processadas) - 1:

        palavras_unicas_lista = list(set(sentencas_processadas[indice] + sentencas_processadas[indice + 1]))

        frequencia_palavras_sentenca01 = [0] * len(palavras_unicas_lista)
        frequencia_palavras_sentenca02 = [0] * len(palavras_unicas_lista) 

        for token in sentencas_processadas[indice]: frequencia_palavras_sentenca01[palavras_unicas_lista.index(token)] +=1

        for token in sentencas_processadas[indice + 1]: frequencia_palavras_sentenca02[palavras_unicas_lista.index(token)] +=1

        cos_sim = similaridade_do_cossseno(frequencia_palavras_sentenca01, frequencia_palavras_sentenca02)

        # print(f"Similaridade de cosseno entre as sentenças {indice + 1} e {indice + 2}: {cos_sim:.2f}")

        if cos_sim >= limite:
            sentenca_atual_de_memoria += " " + sentencas_originais[indice + 1]
        else:
            lista_sentencas_concatenadas.append(sentenca_atual_de_memoria)
            sentenca_atual_de_memoria = str(sentencas_originais[indice + 1])
        
        indice += 1
    
    if indice == len(sentencas_processadas) - 1: 
        lista_sentencas_concatenadas.append(sentenca_atual_de_memoria)

    return lista_sentencas_concatenadas

def pegar_topico(texto_concatenado):
    tokens = remover_stopwords_pontuacao(texto_concatenado)
    
    contagem_palavras = Counter(tokens)
    chaves_frequentes = [chave for chave in contagem_palavras if contagem_palavras[chave] > 1]
    
    if chaves_frequentes:
        topicos = f"<Tópicos: {', '.join(chaves_frequentes)}>"
        return (texto_concatenado, topicos)
    else:
        palavras_relevantes = [token.text for token in nlp(" ".join(tokens)) if token.pos_ in ["VERB", "ADJ", "PROPN", "NOUN"]]

        if palavras_relevantes and len(palavras_relevantes) > 1:
            topicos = []
            topicos.append(str(palavras_relevantes[0]))
            topicos.append(str(palavras_relevantes[1]))

            return (texto_concatenado, f"<Tópicos: {', '.join(topicos)}>")
        else:
            topico = texto_concatenado[0]
            return (texto_concatenado, f"<Tópicos: {topico}>")
        
def criar_novo_arquivo(lista_sentencas_completas):
    with open(caminho_relativo_saida, "w", encoding="utf-8") as paragrafos:
        for paragrafo in lista_sentencas_completas:
            paragrafos.write(f"{paragrafo[0] } \n")
            paragrafos.write(f"{paragrafo[1] } \n")
            paragrafos.write("\n")

def start(): 
    try:
        # Nível 1
        texto = abrir_arquivo(caminho_relativo_entrada)
        texto_processado = processar_texto(texto)

        # Nível 2
        sentencas_concatenadas = calcular_similaridade(texto_processado[0], texto_processado[1])

        #Nível 3
        sentencas_completas = []
        for sentenca in sentencas_concatenadas:
            texto_topico = pegar_topico(sentenca)
            sentencas_completas.append(texto_topico)
            
        criar_novo_arquivo(sentencas_completas)

        print("Arquivo de texto processado com sucesso!")
    except Exception as e:
        print(f"Erro ao processar o texto: {e}")

start()