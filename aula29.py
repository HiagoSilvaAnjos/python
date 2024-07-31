"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

number_str = input("I will double the number you send: ")

try: # Tentar executar o código
    number_float = float(number_str)
    print(f"The double at number is: {number_float} é {number_float * 2:.2f}")
except: # ocorreu algum erro
    print("The value is not a number!")