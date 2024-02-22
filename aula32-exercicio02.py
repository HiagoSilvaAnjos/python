""" TODO:
    FIXME: Considere a hora apenas com valores inteiros! ex: 6, 19, 22...
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
user_input = input("What is your name? ")
checked_input_name = type(user_input) == str and len(user_input) != 0

if checked_input_name:
    name = user_input
else:
    name = "Pessoa"

value_hour_str = input("What time is it? ")

if value_hour_str.isdigit():

    value_hour_int = int(value_hour_str)

    if value_hour_int >= 0 and value_hour_int <= 11:
        print(f"Good morning! {name}")
    elif value_hour_int >= 12 and value_hour_int <= 17:
        print(f"Good afternoon! {name}")
    else:
        print(f"Good night! {name}")

else:   
    print("Value hour is invalid (hour entry 0 - 23).")
