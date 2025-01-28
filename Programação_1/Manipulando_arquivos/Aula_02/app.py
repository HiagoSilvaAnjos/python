# read => "r" => "ler"
# read -> para arquivos simples (ex: senhas, tokens, informações únicas)
with open("C:\\Users\\Hiago Silva\\Documents\\python\\Programação_1\\Manipulando_arquivos\\Aula_02\\email.txt", 'r') as file:
    content = file.read()
    print(content)

# readlines => "r" => "ler linhas"
# readlines -> para arquivos que possuem várias informações
with open("C:\\Users\\Hiago Silva\\Documents\\python\\Programação_1\\Manipulando_arquivos\\Aula_02\\mensagem.txt", 'r', encoding='utf-8') as file:
    content = file.readlines()
    print(content)
    for line in content:
        if "faturamento" in line:
            print(line)

# write => "w" => "escrever"
# write -> substitui o conteúdo do arquivo, se o arquivo não existir, ele cria um novo
with open("C:\\Users\\Hiago Silva\\Documents\\python\\Programação_1\\Manipulando_arquivos\\Aula_02\\new_password.txt", 'w') as file:
    file.write("456789")

# append => "a" => "adicionar"
# append -> adiciona conteúdo ao final do arquivo, se o arquivo não existir, ele cria um novo
with open("C:\\Users\\Hiago Silva\\Documents\\python\\Programação_1\\Manipulando_arquivos\\Aula_02\\email.txt", 'a+') as file:
    # Mover o cursor para o início do arquivo
    file.seek(0)
    emails = file.readlines()
    formater_emails = [email.rstrip() for email in emails]
    

    email_exists = False
    print(formater_emails)
    for email in formater_emails:
        if "test@gmail.com" in email:
            email_exists = True

    if not email_exists:
        file.write("test@gmail.com\n")
    else:
        print("Email já existe")