"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 60  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada


# FIXME => Qualquer variável que você não quer que seja mudada, você deve declarar a variável com letras Maiúsculas

RADAR_ONE = 60 # velocidade máxima no radar 1
LOCAL_ONE = 100 # Local onde está o radar 1
RADAR_RANGE = 1 # A distância em que o radar pega

velocity_veicle_pass_radar_one = velocidade > RADAR_ONE
veicle_pass_radar_one = local_carro >= (LOCAL_ONE - RADAR_RANGE) and local_carro <= (LOCAL_ONE + RADAR_RANGE)
veicle_mult_radar_one = veicle_pass_radar_one and velocity_veicle_pass_radar_one

# if velocity_veicle_pass_radar_one:
#     print("Velocidade do veículo é maior que a permitida!")

if veicle_pass_radar_one:
    print("Veículo passou no radar 1")

    if velocity_veicle_pass_radar_one:
        print("Velocidade do veículo é maior que a permitida!")
        print("Veículo multado por passar o limite de velocidade no radar 1!")

else:
    print("Veículo NÃO passou no radar 1")

