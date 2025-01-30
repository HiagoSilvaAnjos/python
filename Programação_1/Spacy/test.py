import spacy

# Carregar modelo do spaCy
nlp = spacy.load("pt_core_news_sm")

def carregar_texto(nome_arquivo):
    """Lê o arquivo de entrada e retorna o texto."""
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        return f.read()

def segmentar_sentencas(texto):
    """Divide o texto em sentenças."""
    doc = nlp(texto)
    return list(doc.sents)

def extrair_palavras_chave(sentenca):
    """Extrai palavras-chave (substantivos e verbos) da sentença."""
    return [token.text.lower() for token in sentenca if token.pos_ in ["NOUN", "VERB"] and not token.is_stop]

def calcular_similaridade(sent1, sent2):
    """Calcula a similaridade entre duas sentenças com base nas palavras-chave."""
    palavras1 = extrair_palavras_chave(sent1)
    palavras2 = extrair_palavras_chave(sent2)
    if not palavras1 or not palavras2:
        return 0
    interseccao = len([p for p in palavras1 if p in palavras2])
    uniao = len(palavras1) + len(palavras2) - interseccao
    return interseccao / uniao if uniao > 0 else 0

def agrupar_sentencas(sentencas, limite_similaridade=0.3):
    """Agrupa sentenças semelhantes em subtópicos com base na similaridade."""
    grupos = []
    for sentenca in sentencas:
        adicionada = False
        for grupo in grupos:
            for s in grupo:
                similaridade = calcular_similaridade(sentenca, s)
                if similaridade >= limite_similaridade:
                    grupo.append(sentenca)
                    adicionada = True
        if not adicionada:
            grupos.append([sentenca])
    
    return grupos

def gerar_rotulo(grupo):
    """Gera um rótulo de até 5 palavras-chave para um grupo de sentenças."""
    palavras = []
    for sentenca in grupo:
        palavras.extend(extrair_palavras_chave(sentenca))

    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    # Ordenação manual sem uso de max ou sorted
    palavras_ordenadas = []
    while frequencia:
        palavra_mais_frequente = None
        frequencia_mais_alta = 0
        
        # Procurar a palavra com a maior frequência manualmente
        for palavra, freq in frequencia.items():
            if freq > frequencia_mais_alta:
                palavra_mais_frequente = palavra
                frequencia_mais_alta = freq

        palavras_ordenadas.append(palavra_mais_frequente)
        del frequencia[palavra_mais_frequente]  # Remove a palavra da contagem

    # Pegando as 5 palavras mais frequentes
    rotulo = palavras_ordenadas[:5]
    return rotulo

def salvar_saida(grupos, nome_arquivo):
    """Salva os subtópicos e rótulos em um arquivo de saída."""
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        for grupo in grupos:
            for sentenca in grupo:
                f.write(sentenca.text + "\n")
            rotulo = gerar_rotulo(grupo)
            f.write(f"<tópico: {', '.join(rotulo)}>\n\n")

def main(arquivo_entrada, arquivo_saida):
    texto = carregar_texto(arquivo_entrada)
    sentencas = segmentar_sentencas(texto)
    grupos = agrupar_sentencas(sentencas)
    salvar_saida(grupos, arquivo_saida)

# Exemplo de uso
# Substitua 'entrada.txt' pelo caminho real do arquivo de entrada
# E 'saida.txt' pelo arquivo de saída desejado
main("/home/savio/Documentos/curso-python/Programação_1/Spacy/entrada.txt", "/home/savio/Documentos/curso-python/Programação_1/Spacy/saida.txt")
