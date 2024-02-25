"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

number = 0

while (number < 100):
    number += 1

    # if number > 10 and number < 20:
    #     # print(f"ignore is: {number}")
    #     continue
    
    print(f"number is: {number}")

    if (number % 2 == 0):
        print(f"IS PAIR: {number}")
    else:
        print(f"NOT PAIR: {number}")

    