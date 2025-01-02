# Operadores in e not in
# in => "está entre"
# not in => "não está entre"
# Strings são iteráveis
#  0 1 2 3 4 5 => índices
#  O t á v i o
# -6-5-4-3-2-1 => índices

name = "HiagoZera"
print("hiago" in name or "Hiago" in name or "HIAGO" in name)

print("=" * 60)

print("goZe" not in name)

print("=" * 60)

digit_name = input("Digite seu nome: ")
search = input("Digite o que deseja encontrar: ")

if search in digit_name:
    print(f"'{search}' está presente em {digit_name}")
else: 
    print(f"'{search}' NÃO está presente em {digit_name}")