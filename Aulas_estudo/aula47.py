"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

secret_word = "javascript"
character_entry = ""
count_attempts = 0

while True:
    
    letter_enter = input("Enter a letter: ")

    if(len(letter_enter) > 1):
        print("Please enter just one character!")
        continue

    count_attempts += 1

    if(letter_enter in secret_word):
        character_entry += letter_enter

    word_correction = ""
    for letter in secret_word:
        if(letter in character_entry):
            word_correction += letter
        else:
            word_correction += "*"

    print(word_correction)

    if(word_correction == secret_word):
        os.system("clear")
        print("Congratulation!!! you win!")
        print(f"The secret word was: {secret_word}")
        print(f"Total attempts: {count_attempts}")
        count_attempts = 0
        character_entry = ""
        
        play_again = input("Play Again ? S / N: ")

        if play_again == 's' or play_again == 'S':
            os.system("clear")
            continue
        else:
            print("Thanks for playing")
            break

   