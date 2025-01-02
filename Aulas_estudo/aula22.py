# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entry = input("Digite: 'E' para entrar | 'S' para sair ")
confirm_password = "12345"

if entry == 'E' or entry == 'e': 
    password = input("Senha: ")
    if password == confirm_password:
        print("Entrou")
    else:
        print("Senha incorreta")
else:
    print("Saiu")

# Avaliação de curto circuito
print(True or True or False)
password = input("Senha: ") or "Sem senha "
print(password)