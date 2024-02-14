# Operador lógico " not "
# Usado para inverter expressões
# not true => vira false 
# not false => vira true

print(not True) # false
print(not False) # true

name = input("Name: ")

if not name or name == " ":
    print("Campo vazio") 
else:
    print(f"My name is {name}")