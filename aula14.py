value_A = "Valor de A"
value_B = "Valor de B"
value_C = 1.1

formato = '{valor_one} | {valor_two} | {valor_three: .2f}'.format(
    valor_one = value_A,
    valor_two = value_B,
    valor_three = value_C
)

print(formato)