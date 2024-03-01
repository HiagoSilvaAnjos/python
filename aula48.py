"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""  
#        +01234
#        -54321  
string = "ABCDE" # 5 caracteres (len)
# print(boll([])) # falsy

listItens = [123, True, "Hiagozera", 1.3, ["list dentro de outra list"]]
print(listItens)

print(30 * "=")

for item in listItens:

    if (type(item) == list):
        print(item[0])
    else:
        print(item)