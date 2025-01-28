# try:
#     file = open("tecnologias", 'r')
#     content = file.readline()

#     while content:
#         content = content.rstrip()
#         print(content)
#         content = file.readline()
#     file.close()
# except FileNotFoundError:
#     print("Arquivo não encontrado")
# except Exception as e:
#     print(f"Error: {e}")

try:
    with open("/home/savio/Documentos/curso-python/Programação_1/Manipulando_arquivos/Aula/tecnologias", 'r') as file:

        file.seek(0)
        tecnologias = file.readlines()
        formater_tecnologias = [tecnologia.rstrip() for tecnologia in tecnologias]

        print(f"Quantidade de linhas: {len(formater_tecnologias)}")

        for tecnologia in formater_tecnologias:
            print(f"Tecnologia: {tecnologia} | quantidade de caracteres: {len(tecnologia)}")
        
        print()

        file.seek(0)
        content = file.readline()

        while content:
            content = content.rstrip() #remover \n
            print(f"Tecnologia: {content} | quantidade de caracteres: {len(content)}")
            content = file.readline() #ler a proxima linha
except FileNotFoundError:
    print("Arquivo não encontrado")
except Exception as e:
    print(f"Error: {e}")

print()

try:
    with open("/home/savio/Documentos/curso-python/Programação_1/Manipulando_arquivos/Aula/languages", 'w') as languages:
        language = input("Digite uma linguagem de programação: ")

        while language != "java":
            languages.write(language + "\n")
            language = input("Digite uma linguagem de programação: ")
except FileNotFoundError:
    print("Arquivo não encontrado")
except Exception as e:
    print(f"Error: {e}")

with open("/home/savio/Documentos/curso-python/Programação_1/Manipulando_arquivos/Aula/message", 'r', encoding='utf-8') as file:
    content = file.readlines()
    formater_text = [text.rstrip() for text in content]
    print(formater_text)
    for line in formater_text:
        if "faturamento" in line:
            print(line)