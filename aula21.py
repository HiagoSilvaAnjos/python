# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None (significa que não existe) que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

entry = input("Digite: 'E' para entrar | 'S' para sair ")
confirm_password = "12345"

if entry == 'E': 
    password = input("Senha: ")
    if password == confirm_password:
        print("Entrou")
    else:
        print("Senha incorreta")
else:
    print("Saiu")

# Avaliação de curto circuito
print(True and True and False)