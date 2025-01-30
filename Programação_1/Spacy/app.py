# pip install spacy
# python -m spacy download pt_core_news_sm

import spacy

# Carregar o modelo pré-treinado em português
nlp = spacy.load("pt_core_news_sm")

# Texto de exemplo
texto = "Barack Obama nasceu em Honolulu, no Havaí. Ele foi o 44º presidente dos Estados Unidos."

# Processar o texto
doc = nlp(texto)

# Imprimir tokens e suas propriedades
print("Tokens e suas propriedades:")
for token in doc:
    print(f"Texto: {token.text}, Lema: {token.lemma_}, POS: {token.pos_}, Tag: {token.tag_}, Dependência: {token.dep_}, Cabeça: {token.head.text}")

# Entidades nomeadas
print("\nEntidades nomeadas:")
for ent in doc.ents:
    print(f"Texto: {ent.text}, Rótulo: {ent.label_}")

# Frases
print("\nFrases:")
for sent in doc.sents:
    print(sent.text)

# Função para extrair informações de um texto
def extrair_informacoes(texto):
    doc = nlp(texto)
    tokens = [(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.head.text) for token in doc]
    entidades = [(ent.text, ent.label_) for ent in doc.ents]
    frases = [sent.text for sent in doc.sents]
    return tokens, entidades, frases

# Exemplo de uso da função
texto_exemplo = "Albert Einstein foi um físico teórico que desenvolveu a teoria da relatividade."
tokens, entidades, frases = extrair_informacoes(texto_exemplo)

print("\nTokens extraídos:")
for token in tokens:
    print(token)

print("\nEntidades extraídas:")
for entidade in entidades:
    print(entidade)

print("\nFrases extraídas:")
for frase in frases:
    print(frase)