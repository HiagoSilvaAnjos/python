import spacy
from collections import defaultdict

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
    palavras1 = set(extrair_palavras_chave(sent1))
    palavras2 = set(extrair_palavras_chave(sent2))
    if not palavras1 or not palavras2:
        return 0
    return len(palavras1 & palavras2) / len(palavras1 | palavras2)

def agrupar_sentencas(sentencas, limite_similaridade=0.3):
    """Agrupa sentenças semelhantes em subtópicos com base na similaridade."""
    grupos = []
    for sentenca in sentencas:
        adicionada = False
        for grupo in grupos:
            if any(calcular_similaridade(sentenca, s) >= limite_similaridade for s in grupo):
                grupo.append(sentenca)
                adicionada = True
                break
        if not adicionada:
            grupos.append([sentenca])
    return grupos

def gerar_rotulo(grupo):
    """Gera um rótulo de até 5 palavras-chave para um grupo de sentenças."""
    palavras = [extrair_palavras_chave(sent) for sent in grupo]
    palavras_flat = [p for sublist in palavras for p in sublist]
    frequencia = defaultdict(int)
    for palavra in palavras_flat:
        frequencia[palavra] += 1
    palavras_ordenadas = sorted(frequencia, key=frequencia.get, reverse=True)
    return palavras_ordenadas[:5]

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