def calculateMaiorPalavra (palavra_01, palavra_02):
    tamanho_palavra_A = len(palavra_01)
    tamanho_palavra_B = len(palavra_02)

    if tamanho_palavra_A > tamanho_palavra_B: return palavra_01
    if tamanho_palavra_B > tamanho_palavra_A: return palavra_02
    
    return palavra_01

print(calculateMaiorPalavra("test", "testing"))