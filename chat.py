from datetime import datetime

def get_hour():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

import os

messages = []
users = []

# Adicionar usuários ao chat
num_users = int(input("Enter number of users: "))
for i in range(num_users):
    user_name = input(f"Enter name for user {i+1}: ")
    users.append(user_name)

user_index = 0

while True:
    os.system("cls" if os.name == "nt" else "clear")  

    print("_________Enter 'exit' to end chat________")

    if len(messages) > 0:
        for message in messages:
            print(f"{message['name']}:{message['time']} - {message['description']}")

    current_user = users[user_index]
    print(f"\nUser: {current_user}")
    text = input("Enter your message: ")

    if text.lower() == "exit":
        break

    messages.append({
        "name": current_user,
        "description": text,
        "time": get_hour()
    })

    # Alternar para o próximo usuário
    user_index = (user_index + 1) % num_users
