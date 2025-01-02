"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

name = "HIAGOZERA"
price = 1000.985864967329
variant = "%s, o preço foi de %.2f reais" % (name, price)
print(variant)
variant = f"{name}, o preço foi de{price: .2f} reais" 
print(variant)
variant = "{}, o preço foi de {:.2f} reais".format(name, price) 
print(variant)