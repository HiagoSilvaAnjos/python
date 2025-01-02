# if / elif / else
# se / se não se / se não

name_user = input("Digite seu nome: ")
conditions = input("Você quer 'entrar' ou 'sair'? ")

if conditions == 'entrar': 
    print(f"Você entrou no sistema {name_user}")
elif conditions == 'sair':
    print("Você saiu do sistema {}".format(name_user))
else:
    print("Você não digitou 'entrar' ou 'sair'")