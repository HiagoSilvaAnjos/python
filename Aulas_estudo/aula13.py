# Formatando strings => f(string)

name_person = 'Hiago Silva'
height_person = 1.80
weight_person = 76
imc_person = weight_person / (height_person ** 2) 

line_01 = f"{name_person} Tem {height_person: .2f} de Altura"
line_02 = f"pesa {weight_person: .2f} quilos e seu IMC é"
line_03 = f"{imc_person: .2f}"

print(line_01)
print(line_02)
print(line_03)   