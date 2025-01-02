text = "O Python é uma linguagem de programação" \
        " multiparadigma " \
        "Python foi criado por Guido van Rossum."

i = 0

numbers_of_letter = 0
letter_frequent = ""

while i < len(text):
    character = text[i]
    most_frequent_letter = text.count(character)

    if character == ' ' or character == '.':
        i += 1
        continue

    if numbers_of_letter < most_frequent_letter:
        numbers_of_letter = most_frequent_letter
        letter_frequent = character

    i += 1

print(text)
print(f"A letra mais frequente na frase é: '{letter_frequent}', aparecendo {numbers_of_letter} vezes!")
