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
    with open("tecnologias", 'r') as file:
        content = file.readline()

        while content:
            content = content.rstrip()
            print(content)
            content = file.readline()
except FileNotFoundError:
    print("Arquivo não encontrado")
except Exception as e:
    print(f"Error: {e}")

print()
print()
print()

try:
    with open("languages", 'w') as languages:
        language = input("Digite uma linguagem de programação: ")

        while language != "java":
            languages.write(language + "\n")
            language = input("Digite uma linguagem de programação: ")
except FileNotFoundError:
    print("Arquivo não encontrado")
except Exception as e:
    print(f"Error: {e}")