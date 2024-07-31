from datetime import datetime
from colorama import init, Fore, Style
import os

init()

def get_hour():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

messages = []
users = []

num_users = int(input("Enter number of users: "))
for i in range(num_users):
    user_name = input(f"Enter name for user {i+1}: ")
    users.append(user_name)

user_index = 0

while True:
    os.system("cls" if os.name == "nt" else "clear")  

    print(Fore.CYAN + "_" * 20 + Style.RESET_ALL)

    if len(messages) > 0:
        for message in messages:
            print(Fore.YELLOW + f"{message['name']}:" + Fore.GREEN + f"{message['time']}" + Fore.RESET + f" - {message['description']}")

    current_user = users[user_index]
    print(Fore.BLUE + f"\nCurrent user: {current_user}" + Style.RESET_ALL)
    text = input("Enter your message: ")

    if text.lower() == "exit":
        break

    messages.append({
        "name": current_user,
        "description": text,
        "time": get_hour()
    })

    user_index = (user_index + 1) % num_users
