# 9. Desafio: Um poderoso mago está cercado por seus inimigos e precisa utilizar sua magia
# para causar dano em área, esse feitiço causa 1 de dano a todos os adversários e se pelo
# menos um inimigo for vencido o mago irá relançar a magia até que nenhum outro possa ser
# derrotado ou que todos já estejam derrotados. Sabe-se de antemão que ele irá enfrentar 10
# inimigos.
# Faça um programa que preencha um vetor com números inteiros representando a vida dos
# inimigos do mago, seu programa deverá então simular o lançamento do feitiço e caso algum
# inimigo seja derrotado (representado pela vida atingir o valor 0) o programa irá relançar a
# magia, ao final da execução deverá ser mostrado na saída padrão a quantidade de inimigos
# que foram derrotados na batalha. Por exemplo, se tiver 3 inimigos com vidas 1, 4 e 3, ao
# lançar a primeira magia um inimigo é derrotado e o vetor fica com 0, 3 e 2. Ao lançar
# novamente o feitiço, não é derrotado nenhum inimigo e termina a batalha.
# Entradas:
# 1. Elementos de vetor com 10 posições representando a vida dos inimigos.
# Saídas:
# 1. Quantidade de inimigos derrotados.
# Entrada:
# 6 7 3 1 2 4 5 8 9 9
# Exemplo de Saída:
# 10