# Problema 2: Você foi designado para fazer um programa que converte unidades de distância, que pode ser de metros para centímetros ou vice-versa. Para isso, seu programa deve ter duas funções, uma para converter de metros para centímetros e outra para converter o inverso.

# Cada função deve receber a distância como parâmetro (número real) e retornar a distância convertida.

# ATENÇÃO! As funções de conversão devem ser utilizadas no programa principal, onde serão lidos os valores da distância e da unidade para qual a distância deve ser convertida. No programa principal, depois de utilizada a função correta deverá ser mostrada na tela a distância convertida.

# OBS: Caso seja fornecida uma unidade inválida, o programa deverá exibir a palavra ERRO como resposta.

# Entradas:

# Distância (real);
# Unidade para qual deverá ser (minúsculo, singular e sem acento) convertida
# Saída:

# Distância convertida, seguida da abreviação da unidade (m ou cm). O valor e a identiﬁcação da unidade devem estar separados.
# -Exemplo de Entrada:

# 10

# centimetro

# Exemplo de Saída:

# 1000 cm

# Exemplo de Entrada 2:

# 250

# metro

# Exemplo de Saída 2:

# 2.5 m

# Exemplo de Entrada 3:

# 45.7

# VOLT

# Exemplo de Saída 3:

# ERRO

def converter_metro(value_centimeter):
    value_converter = value_centimeter / 100
    return f"{value_converter} m"

def converter_centimeter(value_metro):
    value_converter = value_metro * 100
    return f"{value_converter} cm"

try:
    value_input = float(input("Digite o valor que deseja converter: "))
    option_converter = input("Digite a opção de coversão desejada [metro ou centimetro]: ")
    if option_converter not in ["metro", "centimetro"]:
        raise ValueError()
    result_operation = (converter_metro(value_input) if option_converter == "metro" else converter_centimeter(value_input))
    print(result_operation)
except:
    print("ERROR")