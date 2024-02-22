""" TODO:
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

user_firstname_input = input("Enter your first name: ")
length_name_input = len(user_firstname_input)

if length_name_input <= 4:
    print("Your name is short!")

elif length_name_input >= 5 and length_name_input <= 6:
    print("Your first name is normal!")

else:
    print("Your first name is big!")
